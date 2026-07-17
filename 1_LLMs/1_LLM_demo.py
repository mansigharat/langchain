from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
)


result = llm.invoke("What is the capital of India?")

print(result.content)