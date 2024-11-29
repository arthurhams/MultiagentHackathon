import os
from langchain_azure_dynamic_sessions import SessionsPythonREPLTool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain_openai import AzureOpenAI





# get the management endpoint from the session pool in the Azure portal
tool = SessionsPythonREPLTool(pool_management_endpoint=os.environ.get("POOL_MANAGEMENT_ENDPOINT"))

openai_api_key = "a00bdade72f74b5f90fdc522da0bdc4f"
local_llm_endpoint = "https://aiserviceseastus2arhallen.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview"

# Initialize LLM and memory
from langchain.llms import AzureOpenAI
llm = AzureOpenAI(deployment_name="td2", model_name="text-davinci-002")


prompt = "Generate code to calculate 2*2"
tools=[tool]
react_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

react_agent_executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True, handle_parsing_errors=True)

react_agent_executor.invoke({"input": "What is the current time in Vancouver, Canada?"})