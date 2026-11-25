import os
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from google import genai

app = FastAPI(title="RAG API")

with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

model = SentenceTransformer("all-MiniLM-L6-v2")
chunk_emb = model.encode(chunks, convert_to_tensor=True)

# API key ని environment variable నుంచి తీసుకుంటాం (code లో రాయం)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    q_emb = model.encode(q.question, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, chunk_emb)[0]
    best = int(scores.argmax())
    context = chunks[best]
    prompt = (
        "Answer the question using only the context below.\n\n"
        f"Context: {context}\n\n"
        f"Question: {q.question}\n"
        "Answer:"
    )
    try:
        resp = client.models.generate_content(
            model="gemini-3.5-flash", contents=prompt
        )
        answer = resp.text
    except Exception as e:
        answer = f"LLM error: {e}"
    return {
        "question": q.question,
        "answer": answer,
        "answer_chunk": context,
        "score": round(float(scores[best]), 2),
        "prompt": prompt,
    }