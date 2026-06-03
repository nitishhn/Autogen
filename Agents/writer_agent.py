import os
import autogen
from dotenv import load_dotenv
load_dotenv()

config_list = [
    {
        "model": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        "api_type": "azure",
        "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "api_key": os.getenv("AZURE_OPENAI_KEY"),
        "api_version": "2025-01-01-preview",
    }
]


