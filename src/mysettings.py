import os

azure_openai_api_key_name = "AZURE_OPENAI_API_KEY"
azure_openai_url_name = "AZURE_OPENAI_URL"
bing_api_key_name = "BING_API_KEY"

llm_config = {"config_list": [
    {
        "model": "gpt-4o",
        "api_type": "azure",
        # To use this code, you must set the environment variable AZURE_OPENAI_API_KEY
        # Open a terminal within the devcontainer and run the following command:
        # export AZURE_OPENAI_API_KEY=<your Azure OpenAI API key>
        "api_key": os.environ.get(azure_openai_api_key_name),
        "base_url": os.environ.get(azure_openai_url_name),
        "api_version": "2024-08-01-preview"
    }
]}

llm_websurfer = {
    "temperature": 0,
    "cache_seed": None,
    "config_list": [
        {
            "model": "gpt-4o",
            "api_type": "azure",
            # To use this code, you must set the environment variable AZURE_OPENAI_API_KEY
            # Open a terminal within the devcontainer and run the following command:
            # export AZURE_OPENAI_API_KEY=<your Azure OpenAI API key>
            "api_key": os.environ.get(azure_openai_api_key_name),
            "base_url": os.environ.get(azure_openai_url_name),
            "api_version": "2024-08-01-preview"
        }
    ]}

browser_config = {
    "viewport_size": 4096,
    "bing_api_key": os.environ.get(bing_api_key_name),
}

generated_directory = "./generated"

if os.environ.get(bing_api_key_name) is None:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("WARNING: Bing API key not found. Some examples won't work.")
    print(f"Set the environment variable {bing_api_key_name}")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if os.environ.get(azure_openai_api_key_name) is None:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("WARNING: Azure OpenAI API key not found. None of the examples will work.")
    print(f"Set the environment variable {azure_openai_api_key_name}")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if os.environ.get(azure_openai_url_name) is None:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("WARNING: Azure OpenAI API URL not found. None of the examples will work.")
    print(f"Set the environment variable {azure_openai_url_name}")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
