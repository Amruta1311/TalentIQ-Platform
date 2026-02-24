from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import torch
from sentence_transformers import SentenceTransformer

# Create app
app = FastAPI(title="TalentIQ Platform")

# Load model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("all-MiniLM-L6-v2", device=device)


class MatchRequest(BaseModel):
    resume: str
    job: str


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/match")
def match(req: MatchRequest):

    r_emb = model.encode(req.resume)
    j_emb = model.encode(req.job)

    score = cosine(r_emb, j_emb)

    return {
        "match_score": round(float(score) * 100, 2),
        "device": device,
        "status": "success"
    }