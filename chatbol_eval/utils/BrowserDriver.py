from abc import ABC, abstractmethod


class BrowserDriver(ABC):
    """
    Abstract Class to load the browser driver
    """

    @abstractmethod
    def __init__(self):
        """
        Start the browser with arguments
        """
