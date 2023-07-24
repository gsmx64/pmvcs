""" Abstract Base Controller file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractBaseController(ABC):
    """ Class for PMVCS Abstract Base Controller """

    @abstractmethod
    def execute(self, task: str) -> object:
        """
        Executes the PMVCS Base Controller
        """
        pass

    @abstractmethod
    def _current_language(self, key_input: str) -> str:
        """
        Function to return current short language tag from input
        """
        pass

    @abstractmethod
    def _get_menus_controller(self, menus_list: list, **kwargs) -> object:
        """
        Returns the PMVCS Menus Controller
        """
        pass
