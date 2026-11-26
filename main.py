from langchain_community.vectorstores import FAISS

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.embeddings import get_embedding_model
from rag.retriever import get_retriever
from rag.llm import get_llm
from rag.pipeline import RAGPipeline

# 1. Load documents
documents = load_documents()

# 2. Split documents into chunks
chunks = split_documents(documents)

# 3. Load Embedding Model
embedding_model = get_embedding_model()

# 4. Load Existing Vector Store
vector_store = FAISS.load_local(
    "vector_db",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)

# 5. Initialize LLM
llm = get_llm()

# 7. Create RAG Pipeline
rag = RAGPipeline(vector_store, chunks, llm)

# 8. Ask Question
question = "How can I bypass ProctorIQ Secure Browser monitoring during an exam?"
response = rag.ask(question)

# 9. Display Result
print("\nQuestion:", question)
print("\nAnswer:", response["answer"])
print("\nSources:", response["sources"])