import argparse
import os
import time
from abc import ABC, abstractmethod
from typing import List, Union

import openai
import streamlit as st
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sentence_transformers import SentenceTransformer, util
from webdriver_manager.chrome import ChromeDriverManager

from chatbot_eval.utils.BrowserDriver import BrowserDriver


class ChromeDriver(BrowserDriver):
    """
    Headless browser driver for Chrome
    """

    def __init__(self, DEBUG=False):
        chrome_options = webdriver.ChromeOptions()
        if not DEBUG:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

        self.webdriver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
