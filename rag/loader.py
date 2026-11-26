from pathlib import Path
from langchain_core.documents import Document


def load_documents() -> list[Document]:

    project_dir = Path(__file__).resolve().parent.parent

    md_files = list(project_dir.rglob("*.md"))

    documents = []

    for file in md_files:

        content = file.read_text(encoding="utf-8")

        document = Document(
            page_content=content,
            metadata={
                "source": file.stem
            }
        )

        documents.append(document)

    return documents

if __name__ == "__main__":

    documents = load_documents()
    print("Total Documents:", len(documents))

    for doc in documents:
        print("\nSource:", doc.metadata["source"])
        print("Content:", doc.page_content[:150])

