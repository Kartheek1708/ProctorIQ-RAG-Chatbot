from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.embeddings import get_embedding_model
from rag.llm import get_llm
from rag.pipeline import RAGPipeline
from langchain_community.vectorstores import FAISS

app = FastAPI(title="ProctorIQ API")

# Allow React frontend to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class ChatRequest(BaseModel):
    question: str

# Initialize RAG components once when the server starts
documents = load_documents()
chunks = split_documents(documents)
embedding_model = get_embedding_model()

vector_store = FAISS.load_local(
    "vector_db",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)

llm = get_llm()
rag = RAGPipeline(vector_store, chunks, llm)


@app.get("/")
def home():
    return {"message": "ProctorIQ API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = rag.ask(request.question)

    return {
        "answer": response["answer"],
        "sources": response["sources"],
    }