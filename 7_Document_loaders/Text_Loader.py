from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b")

prompt = PromptTemplate(
    template = "Write a summary for the following poem \n {poem}",
    input_variables = ['poem']
)

parser = StrOutputParser()

loader = TextLoader(r"7_Document_loaders\poem_india.txt",encoding = 'utf-8')

docs  = loader.load()

print(docs)

print(type(docs))  #list

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})
print(result)