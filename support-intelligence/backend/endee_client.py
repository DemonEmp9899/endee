import requests
import msgpack

BASE_URL = "http://localhost:8080"

def insert_vector(index_name: str, vector_id: str, embedding: list, metadata: dict):
    response = requests.post(
        f"{BASE_URL}/api/v1/index/{index_name}/vector/insert",
        json={
            "id": vector_id,
            "vector": embedding,
            "metadata": metadata
        }
    )

    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    # If response body is empty, just return success
    if response.text.strip() == "":
        return {"status": "inserted (empty response from Endee)"}

    try:
        return response.json()
    except:
        return {"raw_response": response.text}
    

def search_vector(index_name: str, embedding: list, top_k: int = 3):
    response = requests.post(
        f"{BASE_URL}/api/v1/index/{index_name}/search",
        json={
            "vector": embedding,
            "k": top_k,
            "with_metadata": True
        }
    )

    print("Search Status:", response.status_code)

    try:
        # 🔥 decode msgpack instead of JSON
        decoded = msgpack.unpackb(response.content, raw=False)
        return decoded
    except Exception as e:
        return {
            "error": "Failed to decode msgpack",
            "exception": str(e)
        }