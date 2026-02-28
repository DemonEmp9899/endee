from embedding import get_embedding
from endee_client import search_vector

def retrieve_similar(ticket_text: str):
    """
    Convert new ticket into embedding
    Search similar tickets in Endee
    """
    embedding = get_embedding(ticket_text)
    results = search_vector("support_index", embedding, top_k=3)
    return results