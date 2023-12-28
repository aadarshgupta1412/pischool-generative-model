import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from chatbot_eval.chatbots import ChatBot
from chatbot_eval.utils import BrowserDriver


class ClientBot(ChatBot):
    """
    Class to connect with the Chatbot interactively
    using selenium libraryp
    """

    def __init__(self, driver: BrowserDriver, name, uri, scripts):
        self.driver = driver.webdriver
        self.host = None
        self.shadow_root = None
        self.uri = uri
        self.scripts = scripts
        self.jobs = []
        self.name = name

    def _open_chat_box(self):
        """
        Click on the chatbot in the shadow root to start the conversation
        """
        # print('scripts', self.scripts)
        if self.scripts["start_conv"]:
            time.sleep(5)
            self.driver.execute_script(self.scripts["start_conv"], self.host)

    def load(self):
        self.driver.get(self.uri)  # Open the Webpage
        time.sleep(10)  # Wait for 10 seconds, for the website to load

        self.host = WebDriverWait(
            self.driver, 20
        ).until(  # finding the host (parent of shadow root)
            EC.presence_of_element_located((By.TAG_NAME, "apply-widget"))
        )
        self._open_chat_box()

    def send_user_message(self, message):
        self.jobs = []
        element = self.driver.execute_script(self.scripts["open_text_area"], self.host)
        # element = self.shadow_root.find_element(By.TAG_NAME, "textarea")
        element.send_keys(message)
        element.send_keys(Keys.RETURN)
        time.sleep(10)  # Wait for the response to come

        messages = self.driver.execute_script(
            self.scripts["read_last_message"], self.host
        )
        response = messages.get_attribute("innerHTML")

        self.jobs = self.driver.execute_script(self.scripts["jobs_script"], self.host)

        return response + "\n" + " ".join(self.jobs)

    def list_all_messages(self):
        messages = []
        test_id_mapping = {"message_lbl_theirs": "user", "message_lbl_ours": "bot"}

        chat_area = self.driver.execute_script(
            self.scripts.list_all_messages, self.host
        )

        # chat_area = self.shadow_root.find_element(By.CLASS_NAME, "me-messages__inner")
        msg_elements = chat_area.find_elements_by_xpath("*")
        for msg_element in msg_elements:
            data_test_id = msg_element.get_attribute("data-testid")
            text_element = msg_element.find_element(By.CLASS_NAME, "ae8f46")
            text = text_element.get_attribute("innerText")

            role = test_id_mapping[data_test_id]
            messages.append({"role": role, "message": text})

        return messages
