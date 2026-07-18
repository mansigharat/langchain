from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'M:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = dict(
        tempurature = 0.5,
        max_new_tokens = 100
    )
)
model = ChatHuggingFace(llm = llm)