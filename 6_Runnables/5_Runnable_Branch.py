from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-120b")
prompt1 = PromptTemplate(
    template = 'Write defined report on {topic} in paragraph'
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}'
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model,parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , branch_chain)

result = final_chain.invoke({'topic':'Russia vs Ukraine'})
print(result)