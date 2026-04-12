"""Streamlit UI for the Mem0 + LangChain interview prep assistant."""

import streamlit as st
from memory_agent import chat, get_all_memories

st.set_page_config(page_title="AI Interview Prep Coach", page_icon="🧠")
st.title("🧠 AI Interview Prep Coach")
st.caption("Powered by LangChain + Mem0 + Groq — remembers you across sessions.")

with st.sidebar:
    st.header("Session")
    user_id = st.text_input("User ID", value="alice")
    st.markdown("---")
    if st.button("Show stored memories"):
        st.write(get_all_memories(user_id))
    st.markdown("---")
    if st.button("Clear transcript"):
        st.session_state.pop("messages", None)
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Tell me about your prep, or answer my question...")
if user_input is not None:
    # --- Guardrails: Basic input validation ---
    MAX_INPUT_LENGTH = 500
    forbidden_words = ["hack", "attack", "kill", "suicide", "password", "credit card"]
    errors = []
    if not user_input.strip():
        errors.append("Input cannot be empty.")
    if len(user_input) > MAX_INPUT_LENGTH:
        errors.append(f"Input too long (>{MAX_INPUT_LENGTH} chars). Please shorten your message.")
    if any(word in user_input.lower() for word in forbidden_words):
        errors.append("Input contains unsafe or forbidden words.")

    if errors:
        st.warning("\n".join(errors))
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = chat(user_id=user_id, user_message=user_input)
            # --- Guardrails: Output safety check ---
            unsafe_phrases = ["illegal", "harm", "suicide", "kill", "password", "credit card"]
            if any(word in reply.lower() for word in unsafe_phrases):
                st.error("The assistant's response was blocked due to unsafe content.")
                reply = "[Response blocked due to safety policy.]"
            else:
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})