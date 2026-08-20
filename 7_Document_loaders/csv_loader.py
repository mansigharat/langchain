from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = r'7_Document_loaders\sample-simple.csv')

docs = loader.load()

print(len(docs))

print(docs[1])
