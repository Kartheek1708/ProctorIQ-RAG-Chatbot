from langchain_core.output_parsers import StrOutputParser
from rag.prompt import RAG_PROMPT
from rag.hybrid_retriever import get_hybrid_results

def format_context(documents):
    context = ""

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")

        context += f"""
        Source: {source}
        Content: {doc.page_content}

        """

    return context

class RAGPipeline:

    def __init__(self, vector_store, chunks, llm):
        self.vector_store = vector_store
        self.chunks = chunks

        self.chain  = (
            RAG_PROMPT | llm | StrOutputParser()
        )    

    def ask(self, question):

        # Hybrid Retrieval
        documents = get_hybrid_results(
            self.vector_store,
            self.chunks,
            question,
            k=10
        )

        #Step 2: Format retrieved documents
        context = format_context(documents)

        print("\n========== RETRIEVED CONTEXT ==========")

        for i, doc in enumerate(documents, 1):
            print(f"\nChunk {i}")
            print("Source:", doc.metadata.get("source"))
            print("Content:", doc.page_content)

        print("\n========== END CONTEXT ==========\n")


        # Step 3: Generate answer using LLM
        answer = self.chain.invoke({
            "context": context,
            "question": question
        })

        # Step 4: Collect source documents
        sources = list(set(
            doc.metadata.get("source", "Unknown")
            for doc in documents
        ))

        # Step 5: Return answer and sources
        return {
            "answer": answer,
            "sources": sources
        }