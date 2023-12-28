import os

import streamlit as st
from dotenv import load_dotenv
from helpers import Conversation, config_parser
from static import SeleniumScripts

from chatbot_eval.chatbots import ClientBot
from chatbot_eval.LLM import OpenAIClient
from chatbot_eval.utils import ChromeDriver

# Load eenvironment variables from .env
load_dotenv()
DEBUG = os.getenv("DEBUG") == "true"

# Parse command line arguments
args = config_parser.parse_args()
conv_length = args.conversation_length

if "but_a" not in st.session_state:
    st.session_state.driver = ChromeDriver(DEBUG=DEBUG)
    st.session_state.chat_gpt = OpenAIClient(api_key=os.getenv("OPENAI_KEY"))
    st.session_state.client = ClientBot(
        st.session_state.driver, "McDonalds", "https://jobs.mchire.com", SeleniumScripts
    )
    st.session_state.client.load()

# Streamlit App Widgets
st.title("Evaluating Chatbots with LLMs")
title = st.text_input("Ask a Question to the Chatbot", "Perks at your organisation")
button = st.button("Submit", key="but_a")
conversation_instance = Conversation(
    st.session_state.client, st.session_state.chat_gpt, st
)

# Streamlit App Logic
if button:
    conversation_instance.benchmark(title)
