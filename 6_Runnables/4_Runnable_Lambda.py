from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template = 'Generate a joke about {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model = "openai/gpt-oss-120b")

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
})
final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic' : "Brother and Sister"}))