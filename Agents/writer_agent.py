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

llm_config = {
    "config_list": config_list,
    "temperature": 0.5,
    "timeout": 120,
}

writer = autogen.AssistantAgent(
    name="writer",
    system_message="You write clear and professional content.",
    llm_config=llm_config,
)

reviewer = autogen.AssistantAgent(
    name="reviewer",
    system_message="You review content for clarity, grammar, and completeness.",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config=False,
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, writer, reviewer],
    messages=[],
    max_round=6,
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
)

user_proxy.initiate_chat(
    manager,
    message="Create a short email to a client explaining a one-day project delay in a professional tone."
)