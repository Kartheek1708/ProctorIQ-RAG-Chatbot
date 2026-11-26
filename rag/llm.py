import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.1,
        max_tokens=500,
        api_key=api_key
    )    


    return llm


if __name__ == "__main__":

    llm = get_llm()

    response = llm.invoke(
        "What is ProctorIQ Secure Browser? Explain in two sentences."
    )    

    print("LLM Response:")
    print(response.content)