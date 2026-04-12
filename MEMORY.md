# Understanding Memory in AI Agent using Memori

## Why memory is needed
Memory is important since without that we will have to everytime remind the AI system the entire context of our conversation which can exceed the context window that may lead to hallucinated responses or the LLM might crash.

## Memory is of 2 types:

1. **Short term memory**: Temporary Memory storing conversation per session
2. **Long term memory**: Stores conversation across multiple sessions.

## How Memori stores data
1. After receiving all messages it passes to llm and create memories
2. It also resolves the conflicts between differnt memories so that latest truth remains (example: day 1 - I love basketbatall, next day - I love football. In this case it will store football).
3. These memories get stored in a vector database and a graph database (graph database is not enabled by default).

These memories can be later updated or deleted using the memory id which is assigned for each memory or we can also use an LLM which does this work but it might create a conflict as to which memory to be modifed/removed.

## Some Important concepts/parameters of Mem0
1. Messages - The conversation of user and assistant from which memories need to be extracted.
2. Infer - By default this is set to **True**. This parameter by default uses an LLM to extract memories from the raw messages.
3. Metadata - Optional filters like `Eg: {category: 'movie_recommedations'}` can be used for messages which can improve the quality of retrieval.
4. User/Session Identifiers: It is used for maintaing the long term and short term memory with respect to an entity/user. Some key parameters are
- user_id: Used to maintain long term memory with respect to a user.
- session_id: Used to maintain the memory for a particular session basically preserving the short term memory.
- run_id: can be alternatively uses with session_id

## When to add memory for an AI Application.
1. A new user preference is shared
2. A decision or suggestion is made
3. A goal/task is completed
4. A new entity is introduced
5. A user gives feedback or suggestion

## Working of Mem0 Memory Engine
1. The query along with the scope goes to the memory engine
2. The memory engine first validates the session and apply the filters if provided through metadata.
3. The memory engine then performs 2 types of search out of which first is the graph search where in it finds relevant entity and their relationships and secondly it embeds the query and perform a vector search on the vector database. 
4. Once both the results are obtained the memory engine combines both of them into one and presents the final response.