from fastapi import FastAPI
from pydantic import BaseModel
from embedding import get_embedding
from endee_client import insert_vector , search_vector
from retrieval import retrieve_similar
from llm import generate_resolution
app = FastAPI()

INDEX_NAME = "support_index"
DIMENSION = 384  # MiniLM embedding size


# ---------- Models ----------
class Ticket(BaseModel):
    ticket_id: str
    text: str
    resolution: str


class SearchQuery(BaseModel):
    text: str

class SearchRequest(BaseModel):
    text: str



# ---------- Routes ----------
@app.get("/")
def home():
    return {"message": "Customer Support Intelligence System Running 🚀"}


@app.post("/add_ticket/")
def add_ticket(ticket: Ticket):
    embedding = get_embedding(ticket.text)

    metadata = {
        "resolution": ticket.resolution
    }

    response = insert_vector(
        INDEX_NAME,
        ticket.ticket_id,
        embedding,
        metadata
    )

    return response


@app.post("/search_ticket/")
def search_ticket(request: SearchRequest):

    embedding = get_embedding(request.text)
    results = search_vector("support_index", embedding)

    formatted = []

    for item in results:
        score = item[0]
        ticket_id = item[1]

        formatted.append({
            "ticket_id": ticket_id,
            "similarity_score": score
        })

    return {"matches": formatted}


@app.post("/auto_resolve/")
def auto_resolve(request: SearchRequest):

    embedding = get_embedding(request.text)
    results = search_vector("support_index", embedding)

    formatted = []
    past_resolutions = []

    for item in results:
        score = item[0]
        ticket_id = item[1]

        formatted.append({
            "ticket_id": ticket_id,
            "similarity_score": score
        })

        # Here you would fetch resolution from metadata if stored
        past_resolutions.append("Refund will be processed in 24 hours")

    ai_response = generate_resolution(request.text, past_resolutions)

    return {
        "matches": formatted,
        "ai_generated_response": ai_response
    }

@app.get("/dashboard/")
def dashboard():

    # You can expand this later
    return {
        "total_tickets": 1,
        "vector_dimension": 384,
        "model_used": "all-MiniLM-L6-v2",
        "index_name": "support_index"
    }