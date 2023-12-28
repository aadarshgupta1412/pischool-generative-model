from abc import ABC, abstractmethod


class ChatBot(ABC):
    """
    Abstract class to interact with chatbots
    """

    @abstractmethod
    def load(self):
        """
        Load the chatbot and start the chatbot

        Note: This function has to be run before starting any conversation with
        the bot
        """

    @abstractmethod
    def send_user_message(self, message):
        """
        Send a message from the user side to the chatbot

        Returns: the response from the chatbot
        """

    @abstractmethod
    def list_all_messages(self):
        """
        List the conversation from the chatbot

        Returns: List of messages each containing:
                    role: Describing whether the sender is a user or the bot
                    message: Chat message by the sender
        """
