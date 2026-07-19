from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions = 300)

documents = [
    "Sachin Tendulkar is widely regarded as one of the greatest batsmen in cricket history, having scored 100 international centuries across his career.",
    "MS Dhoni captained India to victory in the 2011 Cricket World Cup and is known for his calm decision-making under pressure.",
    "Virat Kohli has been one of the most consistent run-scorers in modern cricket, known for his aggressive batting and fitness standards.",
    "Rohit Sharma holds the record for the highest individual score in ODI cricket, with 264 runs in a single innings.",
    "Jasprit Bumrah is known for his unorthodox bowling action and has become one of the most feared fast bowlers in world cricket."
]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index , score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is : " , score)
