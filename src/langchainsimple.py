import os

os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://aiserviceseastus2arhallen.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = "a00bdade72f74b5f90fdc522da0bdc4f"

from langchain_openai import AzureOpenAI

llm = AzureOpenAI(
    deployment_name="gpt-4o-mini",
)

llm.invoke("Tell me a joke")


