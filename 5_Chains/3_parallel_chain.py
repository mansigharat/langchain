from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="openai/gpt-oss-120b")
model2 = ChatGroq(model="openai/gpt-oss-120b")

prompt1 = PromptTemplate(
    template = ("Generate short and simple notes from the following text \n {text}"),
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = ("Generate short 5  questions on following \n {text}"),
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = ('Merge the provided notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}'),
    input_variables = ['notes' , 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """# Model Context Protocol (MCP)

**Model Context Protocol (MCP)** is an open standard that allows AI models to securely connect with external tools, applications, databases, and APIs through a single, standardized interface. Instead of building a custom integration for every service, developers can use MCP to make AI agents communicate with different systems in a consistent way.

Think of MCP as the **"USB-C for AI applications."** Just as one USB-C port can connect many different devices, MCP enables one AI model to interact with multiple tools without requiring separate integrations for each one.

### Why MCP Matters

* **Standardized communication** between AI models and external tools.
* **Reusable integrations**, reducing development time.
* **Secure access** to data and services.
* **Interoperability** across different AI frameworks and applications.
* **Scalable architecture** for building production-ready AI agents.

### Key Components

* **MCP Client:** The AI application or agent that requests information or actions.
* **MCP Server:** Provides access to tools, APIs, databases, or resources.
* **Resources:** Data sources such as documents, files, or databases.
* **Tools:** Functions the AI can execute, such as sending emails, querying databases, or calling APIs.
* **Prompts:** Reusable prompt templates exposed through the MCP server.

### Benefits of MCP

* Eliminates the need for custom integrations for every tool.
* Makes AI agents more modular and maintainable.
* Enables seamless connection with enterprise systems.
* Improves consistency across AI applications.
* Supports rapid development of intelligent, tool-using agents.

### Common Use Cases

* AI assistants accessing company documents.
* Customer support agents retrieving CRM information.
* Coding assistants interacting with Git repositories.
* AI agents automating workflows across multiple SaaS platforms.
* Research assistants searching databases and summarizing information.

### In Simple Words

MCP is a common language that helps AI models talk to external tools and services. Instead of learning a different way to connect to every application, an AI agent uses MCP to access them all through one standard protocol, making development faster, easier, and more reliable.
"""
result = chain.invoke({'text' : text})
print(result)

chain.get_graph().print_ascii()