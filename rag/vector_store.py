from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embedding_model):

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


if __name__ == "__main__":
    from rag.loader import load_documents
    from rag.chunker import split_documents
    from rag.embeddings import get_embedding_model

    documents = load_documents()

    chunks = split_documents(documents)

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    vector_store.save_local("vector_db")

    print("vector Store Created Successfully!")
    print("Total Vectors: ", vector_store.index.ntotal)