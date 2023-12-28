import os

import openai
from static import ResponseFormat, get_evaluation_prompt

DEBUG = os.getenv("DEBUG") == "true"


class Conversation:
    def __init__(self, client, llm, st=None, conv_length=5):
        self.client = client
        self.llm = llm
        self.conv_length = conv_length
        self.num_messages = 0
        self.messages = []
        self.successful_conversations = 0.0
        self.total_conversations = 0.0
        self.streamlit = st

        if st is None:
            raise Exception("Conversation should be run with OpenAI client")

    def benchmark(self, start_prompt_list):
        seeds = start_prompt_list.split(",")
        self.converse(seeds, 0)

    def converse(self, seeds, index):
        if index >= len(seeds):
            return

        self.num_messages = 0
        self.messages = []
        start_prompt = seeds[index]

        self.messages.clear()
        chatgpt_init_message = f"Imagine you are a job applicant at ${self.client.name}, and you are supposed to converse with the {self.client.name} chatbot on {self.client.name} jobs page. Begin with asking questions related to {start_prompt}."
        self.prompt_chatgpt(chatgpt_init_message)

        evaluation_prompt = get_evaluation_prompt(self.conv_length)
        gpt3_response = openai.ChatCompletion.create(
            model=self.llm.model,
            messages=[
                *self.messages,
                {"role": "system", "content": evaluation_prompt},
            ],
        )

        final_response = gpt3_response.choices[0].message.content

        self.total_conversations += 1
        if "DONE!" in final_response:
            self.successful_conversations += 1
        self.streamlit.write("Result: ", final_response)

        if DEBUG:
            self.streamlit.markdown("## Debug Messages:")
            self.streamlit.write(self.messages)

        self.converse(seeds, index + 1)

    def get_efficiency(self):
        return self.successful_conversations / self.total_conversations

    def parse_chatgpt_response(self, input):
        try:
            res = input.split("OR")[0].split("Andrew:")[1].split("Olivia:")
            chatgpt_query = res[0].strip()
            return chatgpt_query
        except:
            print("LLM response parsing failed for input", input)

    def prompt_chatgpt(self, query, response=None):
        if self.num_messages >= self.conv_length:
            return

        chatgpt_query = ""

        if self.num_messages > 0:
            chatgpt_query += (
                "ChatBot responded for your previous question, which was:\n "
                + query
                + ". And the chatbots response was, "
                + response
                + ". Ask a followup question \n"
            )
        else:
            chatgpt_query += query

        chatgpt_query += ResponseFormat
        chatgpt_response = (
            self.llm.send_user_prompt(chatgpt_query).choices[0].message.content
        )

        # Parse the response here
        query_for_chatbot = self.parse_chatgpt_response(chatgpt_response)
        # Querying the chatbot
        chatbot_response = self.prompt_chatbot(query_for_chatbot)

        self.streamlit.write("Andrew: \n", query_for_chatbot)
        self.streamlit.write("Olivia: \n", chatbot_response, unsafe_allow_html=True)
        self.messages.append({"role": "assistant", "content": query_for_chatbot})
        self.messages.append({"role": "user", "content": chatbot_response})
        self.streamlit.markdown("""---""")

        self.num_messages += 1
        self.prompt_chatgpt(query_for_chatbot, chatbot_response)

    def prompt_chatbot(self, message):
        return self.client.send_user_message(message)
