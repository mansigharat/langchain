from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.3-70B-Instruct",
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = "fact_1",description = 'fact_1 about the topic'),
    ResponseSchema(name = "fact_2",description = 'fact_2 about the topic'),
    ResponseSchema(name = "fact_3",description = 'fact_3 about the topic'),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give 3 fact about {topic} \n {format_instruction}",
    input_variable = ['topic'],
    partial_variables = {'format_instruction' : parser.get_format_instruction()}
)

chain = template | model | parser
final = chain.invoke({'topic' :"black hole"})

print(final)
