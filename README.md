# RAG API

A simple Retrieval-Augmented Generation (RAG) project built with Python and FastAPI.

## What It Does
Takes a question, finds the most relevant text chunk using embeddings (meaning-based search), and builds a prompt that can be sent to an LLM.

## Features
- Reads text from data.txt and splits it into chunks
- Creates embeddings with sentence-transformers (all-MiniLM-L6-v2)
- Finds the best matching chunk using cosine similarity
- POST /ask returns the question, best chunk, similarity score and the prompt

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic
- sentence-transformers

## How to Run
1. Create and activate a virtual environment:
   
   python -m venv .venv
   .venv\Scripts\activate
   
2. Install dependencies:
   
   pip install fastapi uvicorn sentence-transformers
   
3. Start the server:
   
   uvicorn api:app --port 8001
   
4. Open the docs: http://127.0.0.1:8001/docs

## Example Request
json
{
  "question": "Which software helps me version my code?"
}


## Example Response
json
{
  "question": "Which software helps me version my code?",
  "answer_chunk": "Git is a tool to track code changes. ...",
  "score": 0.48,
  "prompt": "Answer the question using only the context below. ..."
}


## Next Steps
- Connect an LLM to generate natural-language answers from the prompt