# 🤖 Customer Support Intelligence System  
### Retrieval-Augmented Generation (RAG) using Endee Vector Database

---

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Intelligence System using **Endee** as the core vector database.

The system enables:

- 🔍 Semantic search over historical support tickets  
- 🧠 Retrieval of similar issues using vector similarity  
- 🤖 AI-generated responses using an LLM (OpenRouter GPT-4o-mini)  
- 🖥 Interactive UI using Streamlit  

Endee is used as the high-performance vector search engine powering the semantic retrieval layer.

---

## 🚨 Problem Statement

Customer support teams frequently handle repetitive queries such as:

- Payment failures  
- Refund requests  
- Login issues  
- Order tracking problems  

Traditional keyword-based search systems:
- ❌ Fail to capture semantic similarity  
- ❌ Miss relevant past tickets  
- ❌ Increase resolution time  

This project solves the problem using:

- Transformer-based embeddings (MiniLM)
- High-speed vector search (Endee)
- LLM-based resolution generation

---

## 🏗 System Architecture
```
User
↓
Streamlit UI
↓
FastAPI Backend
↓
MiniLM Embedding Model (384-dim)
↓
Endee Vector Database
↓
Top-K Similar Tickets
↓
OpenRouter LLM (GPT-4o-mini)
↓
AI-Generated Resolution
```


---

## 🧠 Technical Stack

| Component | Technology |
|------------|------------|
| Backend API | FastAPI |
| Vector Database | Endee |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| LLM | OpenRouter (GPT-4o-mini) |
| UI | Streamlit |
| Containerization | Docker |

---

## ⚙️ How Endee Is Used

1. An index is created with dimension **384** (matching MiniLM embeddings).
2. Support ticket text is converted into vector embeddings.
3. Vectors are inserted into Endee via:
```
POST /api/v1/index/{index_name}/vector/insert
```

4. Semantic similarity search is performed via:
```
POST /api/v1/index/{index_name}/search
```

5. Search responses are decoded from **MsgPack** format.
6. Top-K results are passed to the LLM for response generation.

Endee acts as the **core semantic retrieval engine** of this system.

---

## 🚀 Features

- ✅ Add support tickets
- ✅ Semantic search (vector-based)
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ AI auto-resolution
- ✅ Streamlit interactive UI
- ✅ Dashboard endpoint

---

## 📂 Project Structure
```
endee/
│
├── support-intelligence/
│ ├── backend/
│ │ ├── main.py
│ │ ├── embedding.py
│ │ ├── endee_client.py
│ │ ├── llm.py
│ │ └── requirements.txt
│ │
│ ├── app.py
│ └── README.md
```


---

## 🔧 Setup Instructions

### 1️⃣ Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee/support-intelligence
```
2️⃣ Start Endee (Docker)
From the root endee/ folder:
```
docker compose up -d
```
Ensure Endee is running at:
```
http://localhost:8080
```
3️⃣ Create Index

Create an index with dimension 384 using the Endee API or UI.

4️⃣ Backend Setup
Navigate to backend folder:
```
cd support-intelligence/backend
pip install -r requirements.txt
```
Create a .env file:
```
OPENROUTER_API_KEY=your_openrouter_key_here
```
Run backend:
```
uvicorn main:app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```

5️⃣ Run Streamlit UI

From support-intelligence folder:
```
streamlit run app.py
```
UI will open at:
```
http://localhost:8501
```

🔍 Example Workflow

1. Add support tickets
2. Search semantically similar tickets
3. Generate AI-powered resolution
4. View similarity score
5. Monitor dashboard

🧪 Demonstrated AI Use Case

This project demonstrates:

✅ Semantic Search

✅ Retrieval-Augmented Generation (RAG)

✅ Vector search as the core AI component

Vector similarity search using Endee is central to the architecture.

🔐 Environment Variables

The following variable is required:
```
OPENROUTER_API_KEY
```
.env is excluded via .gitignore.
📈 Future Improvements

1. Metadata-based resolution retrieval
2. Similarity threshold filtering
3. Ticket clustering
4. Sentiment classification
5. Production deployment

🏁 Conclusion

1. This project demonstrates practical integration of:
2. High-performance vector search (Endee)
3. Transformer-based embeddings
4. Retrieval-Augmented Generation
5. LLM-based response synthesis
6. Full-stack AI system design

It highlights real-world usage of vector databases in AI applications.


