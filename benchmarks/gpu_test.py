import time
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Test resume data" * 100

start = time.time()
model.encode(text)
print("Latency:", time.time() - start)