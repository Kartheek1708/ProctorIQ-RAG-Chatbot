from rag.bm25_retriever import create_bm25_retriever, search_bm25

def reciprocal_rank_fusion(result_list, k=60):

    fused_scores = {}

    for results in result_list:
        for rank, doc in enumerate(results, 1):

            doc_id = doc.page_content

            if doc_id not in fused_scores:
                fused_scores[doc_id] = {
                    "score":0,
                    "document": doc
                }

            fused_scores[doc_id]["score"] += 1 / (k + rank)

    
    ranked_results = sorted(
        fused_scores.values(), 
        key=lambda x: x["score"],
        reverse=True
    )

    return [item["document"] for item in ranked_results]


def get_hybrid_results(vector_store, chunks, question, k=5):
    # FAISS vector search
    faiss_results = vector_store.similarity_search(
        question,
        k=k
    )

    # BM25 keyword search
    bm25 = create_bm25_retriever(chunks)

    bm25_results = search_bm25(
        bm25,
        chunks,
        question,
        k=k
    )

    # Combine both results using RRF
    hybrid_results = reciprocal_rank_fusion(
        [faiss_results, bm25_results]
    )

    return hybrid_results[:k]



if __name__ == "__main__":

    from rag.loader import load_documents
    from rag.chunker import split_documents
    from rag.embeddings import get_embedding_model
    from langchain_community.vectorstores import FAISS

    # Step 1: Load documents
    documents = load_documents()

    # Step 2: Create chunks
    chunks = split_documents(documents)

    # Step 3: Load embedding model
    embedding_model = get_embedding_model()

    # Step 4: Load existing FAISS vector store
    vector_store = FAISS.load_local(
        "vector_db",
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )

    # Step 5: Ask a question
    question = "How to install ProctorIQ on Windows?"

    # Step 6: Get hybrid results
    results = get_hybrid_results(
        vector_store,
        chunks,
        question,
        k=5
    )

    # Step 7: Display results
    print("Total Hybrid Results:", len(results))

    for i, doc in enumerate(results, 1):
        print(f"\nChunk {i}")
        print("Source:", doc.metadata["source"])
        print("Content:", doc.page_content[:300])    