""" Abstract Base View file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractBaseView(ABC):
    """ Class for PMVCS Abstract Base View """

    @abstractmethod
    def get_intro(self, dummy='') -> str:
        """
        Function to get intro view message
        """
        pass

    @abstractmethod
    def get_exit(self, dummy='') -> str:
        """
        Function to get exit view message
        """
        pass

    @abstractmethod
    def line_brake(self, prints=True) -> str:
        """
        Function to get a linebrake in view
        """
        pass

    @abstractmethod
    def clean_screen(self) -> None:
        """
        Makes a screen clear in view. Calls cls for Windows
        and clear for Unix/Linux
        """
        pass

    @abstractmethod
    def input_start(self) -> str:
        """
        Returns the select option input
        """
        pass

    @abstractmethod
    def input_pause(self) -> str:
        """
        Returns the intro press a key pause
        """
        pass

    @abstractmethod
    def input_options(self) -> str:
        """
        Returns the select option input
        """
        pass

    @abstractmethod
    def input_generic(self, text: str) -> str:
        """
        Returns the pause option to repeat binary search
        """
        pass

    @abstractmethod
    def input_language(self, text_options) -> str:
        """
        Returns the select option input
        """
        pass

    @abstractmethod
    def get_menu_options(self, key: str, value: str) -> str:
        """
        Function to get menu options view formated
        """
        pass
