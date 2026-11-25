# Step 3: read the file and split into chunks
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split("\n\n")
chunks = [c.strip() for c in chunks if c.strip()]

print("Total chunks:", len(chunks))
for i, chunk in enumerate(chunks):
    print(i, "->", chunk)

# Step 4: find the best chunk for a question
import re

stop_words = {"what", "is", "a", "an", "the", "of", "to", "in", "and", "are", "for", "how", "it"}

def get_words(text):
    words = re.findall(r"\w+", text.lower())
    return set(words) - stop_words

def search(question):
    q_words = get_words(question)
    best_chunk = None
    best_score = 0
    for chunk in chunks:
        score = len(q_words & get_words(chunk))
        if score > best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk

questions = [
    "What is SQLite?",
    "How do I start the server?",
    "What does CRUD mean?",
    "Which tool tracks code changes?",
    "Which software helps me version my code?",
]
for q in questions:
    print("\nQuestion:", q)
    print("Answer chunk:", search(q))
