from langchain.llms import Groq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm = Groq(model="openai/gpt-oss-120b",temperature = 0.7)

prompt = PromptTemplate(
    input_variables = ['topic'],
    template = "Suggest a catchy blog title about {topic}"
)
topic = input('Enter a Topic : ')

formatted_prompt = prompt.format(topic=topic)

blog_title = llm.predict(formatted_prompt)

print("Generated Blog Title : ",blog_title)