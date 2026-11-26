from langchain_community.vectorstores import FAISS

def get_retriever(vector_store):

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 10}
    )

    return retriever


if __name__ == "__main__":
    from rag.embeddings import get_embedding_model

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        "vector_db",
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )    

    retriever = get_retriever(vector_store)

    question = "How can I install ProctorIQ on Windows?"

    results = retriever.invoke(question)

    print("Total Retrieved Chunks:", len(results))

    for i, doc in enumerate(results):

        print(f"\nChunk {i + 1}")
        print("Source:", doc.metadata["source"])
        print("Content:", doc.page_content[:300])