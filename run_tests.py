import csv
from langchain_community.vectorstores import FAISS

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.embeddings import get_embedding_model
from rag.llm import get_llm
from rag.pipeline import RAGPipeline

INPUT = "Data/Test CSV/test.csv"
OUTPUT = "Data/Test CSV/results.csv"

# Setup (main.py lo laage)
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

# Questions read chesi test cheyyadam
with open(INPUT, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

results = []
for r in rows:
    qid, q = r["question_id"], r["question"]
    try:
        response = rag.ask(q)
        answer = response["answer"]
        sources = str(response["sources"])
    except Exception as e:
        answer, sources = f"ERROR: {e}", ""

    print(f"{qid}: {q}\n-> {answer}\n")
    results.append({
        "question_id": qid,
        "question": q,
        "answer": answer,
        "sources": sources,
    })

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["question_id", "question", "answer", "sources"])
    w.writeheader()
    w.writerows(results)

print("Done. Results saved to", OUTPUT)