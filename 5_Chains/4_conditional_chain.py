from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()

classification_prompt = PromptTemplate(
    template="""Classify the sentiment of the following feedback. Feedback:{feedback} {format_instructions}""",
    input_variables=["feedback"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()},
)

classifier_chain = classification_prompt | model | pydantic_parser

positive_prompt = PromptTemplate(
    template="""Write a polite response to this positive feedback.Feedback:{feedback}""",
    input_variables=["feedback"],
)

negative_prompt = PromptTemplate(
    template="""Write a polite apology and response to this negative feedback.Feedback:{feedback}""",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive",positive_prompt | model | str_parser,
    ),
    (lambda x: x["sentiment"] == "negative",negative_prompt | model | str_parser,
    ),
    RunnableLambda(lambda x: "Could not determine sentiment."),
)

full_chain = (
    RunnableLambda(
        lambda x: {"feedback": x["feedback"],"sentiment": classifier_chain.invoke({"feedback": x["feedback"]}).sentiment,})| branch_chain
)

result = full_chain.invoke(
    {"feedback": "This smartphone's screen is broken."})

print(result)
