import re 
from rank_bm25 import BM25Okapi

def tokenize(text):
    return re.findall(r"\w+", text.lower())


def create_bm25_retriever(chunks):
    tokenized_chunks = [
        tokenize(chunk.page_content)
        for chunk in chunks
    ]    

    bm25 = BM25Okapi(tokenized_chunks)

    return bm25

def search_bm25(bm25, chunks, question, k=5):
    tokenized_question = tokenize(question)

    scores = bm25.get_scores(tokenized_question)

    ranked_indices = scores.argsort()[::-1][:k]

    results = [
        chunks[index]
        for index in ranked_indices
        if scores[index] > 0
    ]

    return results

if __name__ == "__main__":

    from rag.loader import load_documents
    from rag.chunker import split_documents

    # Step 1: Load documents
    documents = load_documents()

    # Step 2: Create chunks
    chunks = split_documents(documents)

    # Step 3: Create BM25 index
    bm25 = create_bm25_retriever(chunks)

    # Step 4: User question
    question = "How to install ProctorIQ on Windows?"

    # Step 5: Search using BM25
    results = search_bm25(
        bm25, 
        chunks,
        question,
        k=5
    )

    # Step 6: Display results
    print("Total Retrieved Chunks:", len(results))

    for i, doc in enumerate(results, 1):
        print(f"\nChunk {i}")
        print("Source:", doc.metadata["source"])
        print("Content:", doc.page_content[:300])