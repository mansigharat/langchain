from langchain_groq import ChatGroq
from dotenv import load_dotenv
      
load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 1.5,
        model_kwargs={
        "max_completion_tokens": 200
    }
)

result = model.invoke("Write name of any 5 flowers")
print(result.content)