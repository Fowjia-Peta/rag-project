from sentence_transformers import SentenceTransformer, util

# 1. read file and make chunks (same as before)
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# 2. load model and turn every chunk into numbers (embeddings)
model = SentenceTransformer("all-MiniLM-L6-v2")
chunk_emb = model.encode(chunks, convert_to_tensor=True)

# 3. search by meaning
def search(question):
    q_emb = model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, chunk_emb)[0]
    best = int(scores.argmax())
    return chunks[best], float(scores[best])

questions = [
    "What is SQLite?",
    "How do I start the server?",
    "What does CRUD mean?",
    "Which tool tracks code changes?",
    "Which software helps me version my code?",
]
for q in questions:
    chunk, score = search(q)
    print("\nQuestion:", q)
    print("Answer chunk:", chunk)
    print("Score:", round(score, 2))