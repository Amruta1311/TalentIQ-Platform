def rank(scores):
    return sorted(scores, key=lambda x: x["score"], reverse=True)