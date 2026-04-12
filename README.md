
# 🧠 AI Interview Prep Coach with Mem0 Memory

This project demonstrates how to build an AI agent with both short-term and long-term memory using [Mem0](https://github.com/mem0ai/mem0), [LangChain](https://python.langchain.com/), and [Groq](https://groq.com/). The agent acts as an interview preparation coach, remembering your answers and preferences across sessions.

---

## Features

- **Conversational UI**: Chat with an AI interview coach in your browser (Streamlit app)
- **Personalized Memory**: Remembers your answers, feedback, and preferences across sessions
- **Memory Engine**: Uses Mem0 for memory extraction, storage, and retrieval (vector DB: Qdrant)
- **LLM Integration**: Uses Groq (Llama-3) for interview questions and Gemini for embeddings

---

## How It Works

1. **User interacts** with the AI via a chat interface (Streamlit)
2. **Messages** are sent to the memory engine (Mem0), which extracts and stores relevant memories
3. **Memories** are retrieved and provided as context to the LLM (Groq/Llama-3) for personalized responses
4. **All conversations** are stored in a vector database (Qdrant) for long-term recall

### Memory Types
- **Short-term memory**: Session-based, remembers the current conversation
- **Long-term memory**: User-based, persists across sessions (using `user_id`)

---

## Project Structure

```
memory_in_agents/
├── app.py                # Streamlit UI for chat
├── main.py               # Simple CLI entry point
├── memory_agent.py       # Core logic: memory engine, LLM chain, chat function
├── MEMORY.md             # Theory and concepts of memory in AI agents
├── pyproject.toml        # Python dependencies
├── notebooks/
│   └── experiment.ipynb  # Example notebook for experiments
└── README.md             # This documentation
```

---

## Setup & Installation

1. **Clone the repo**
	```bash
	git clone <repo-url>
	cd memory_in_agents
	```

2. **Create a virtual environment**
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	# or
	pip install -e .
	```

4. **Set up API keys**
	- Copy `.env.example` to `.env` and add your keys for `GROQ_API_KEY` and `GEMINI_API_KEY`.

---

## Running the App

### Streamlit Web UI

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### CLI Demo

```bash
python main.py
```

---

## Main Files Explained
---

## Guardrails (Input & Output Safety)

This project includes basic guardrails to improve safety and reliability:

- **Input validation**: User messages are checked for emptiness, excessive length, and forbidden/unsafe words before being sent to the AI.
- **Output safety checks**: Assistant responses are scanned for unsafe phrases (e.g., related to harm, illegal activity, sensitive info) and blocked if detected.

These checks can be extended for stricter or more advanced safety requirements.
- **app.py**: Streamlit web interface for chatting with the AI coach. Handles user input, session state, and displays stored memories.
- **memory_agent.py**: Implements the memory engine using Mem0, integrates with Groq LLM and Gemini embedder, and provides the `chat()` function.
- **main.py**: Simple CLI entry point (prints a hello message; extend as needed).
- **qdrant_data/**: Stores vector database files for persistent memory.
- **notebooks/experiment.ipynb**: Jupyter notebook for experimenting with memory and retrieval.

---

## How Mem0 Memory Engine Works

1. Receives user messages and extracts memories using an LLM
2. Resolves conflicts (e.g., updates preferences if changed)
3. Stores memories in a vector DB (Qdrant)
4. Retrieves relevant memories for each new query
5. Combines graph and vector search results for best context

See [MEMORY.md](MEMORY.md) for a deep dive into memory concepts and parameters.


## Credits

- [Mem0](https://github.com/mem0ai/mem0)
- [LangChain](https://python.langchain.com/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)

