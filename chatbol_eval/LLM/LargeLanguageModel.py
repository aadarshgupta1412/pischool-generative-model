from abc import ABC, abstractmethod
from typing import List, Union


class LargeLanguageModel(ABC):
    """
    Abstract class to interact with Large Language Models
    """

    @abstractmethod
    def send_user_prompt(
        self, user_messages: Union[str, List[str]], system_messages: List[str] = None
    ):
        """
        Abstract method for sending a prompt to the LLM and receive a response
        """
