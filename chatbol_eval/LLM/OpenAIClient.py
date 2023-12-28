import openai

from chatbot_eval.LLM.LargeLanguageModel import LargeLanguageModel


class OpenAIClient(LargeLanguageModel):
    """
    Connector Client using the OpenAI API to complete the chat

    Ref: https://platform.openai.com/docs/guides/chat/introduction
    """

    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def send_user_prompt(self, user_messages, system_messages: list = None):
        # print('um', user_messages, system_messages)
        messages = []
        if system_messages is not None:
            for system_msg in system_messages:
                messages.append({"role": "system", "content": system_msg})

        if isinstance(user_messages, str):
            messages.append({"role": "user", "content": user_messages})
        else:
            for user_msg in user_messages:
                messages.append({"role": "user", "content": user_msg})
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response
