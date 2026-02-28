from sentence_transformers import SentenceTransformer

# Load model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    """
    Convert text into embedding vector
    """
    return model.encode(text).tolist()