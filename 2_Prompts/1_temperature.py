from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

result = model.invoke("write 5 lines of poem on flower")

print(result.content)


# temperature = 0 -> same/predictable output (good for facts, code, data tasks)
# temperature = 0.7 to 1.0 -> varied/creative output (good for poems, stories, brainstorming)
# temperature > 1.2 -> too random, output quality drops, avoid unless testing
