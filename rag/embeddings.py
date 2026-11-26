
from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model

if __name__ == "__main__":
    embedding_model = get_embedding_model()

    text = "How to install ProctorIQ Secure Browser?"

    vector = embedding_model.embed_query(text)

    print("Embedding Dimensions: ", len(vector))
    print("Embedding Vector: ", vector[:10])    