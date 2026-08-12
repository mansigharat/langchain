from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"7_Document_loaders\India.pdf")

docs = loader.load()

# print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)