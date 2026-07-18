from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "M:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/SmolLM2-360M-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)