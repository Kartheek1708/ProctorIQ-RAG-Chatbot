from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n","\n"," ",""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    from rag.loader import load_documents
    documents = load_documents()
    chunks = split_documents(documents)

    print("Total Documents: ", len(documents))
    print("Total Chunks: ", len(chunks))    