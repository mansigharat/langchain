from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a Linked in post about {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model = "openai/gpt-oss-120b")

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_Chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination' : RunnableSequence(prompt2,model,parser)
})

final_chain =  RunnableSequence(joke_gen_chain,parallel_Chain)

result =final_chain.invoke({'topic':'AI'})

print(result)