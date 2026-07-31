from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)

topic = input("Enter a Topic: ")

chain = prompt | llm

response = chain.invoke({"topic": topic})

print("Generated Blog Title:", response.content)