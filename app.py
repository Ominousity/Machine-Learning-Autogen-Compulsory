import autogen

config_list = [
    {
        "model": "open-mistral-nemo",
        "api_key": "",
        "max_tokens": 100,
        "base_url": "https://api.mistral.ai/v1",
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="Developer",
    llm_config=llm_config,
    system_message="REPLY TERMINATE IF THE TASK HAS BEEN SOLED AT FULL SATISFACTION. You are the one responsible for coding the actual task",
)

assistant2 = autogen.AssistantAgent(
    name="Tester",
    llm_config=llm_config,
    system_message="REPLY TERMINATE IF THE TASK HAS BEEN SOLED AT FULL SATISFACTION. You are the one responsible for testing the code before showing it to the user",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=1,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": True},
    llm_config=llm_config,
    system_message="REPLY TERMINATE IF THE TASK HAS BEEN SOLED AT FULL SATISFACTION.",
)

task = "make a function to add two numbers together"

user_proxy.initiate_chat(assistant, assistant2, message=task)
