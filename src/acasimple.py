from langchain_azure_dynamic_sessions import SessionsPythonREPLTool

tool = SessionsPythonREPLTool(pool_management_endpoint="https://swedencentral.dynamicsessions.io/subscriptions/763346f1-8c3e-4968-a752-83afba56900f/resourceGroups/historrg2/sessionPools/historacasessionpool2")
tool.invoke("6 * 7")