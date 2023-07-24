""" Abstract Menus Controller file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractMenusController(ABC):
    """ Class for PMVCS Abstract Menus Controller """
    _menus = {}

    def go_to_menu(self) -> object:
        """
        Function to build the first level menu options
        """
        pass

    def go_to_exit(self) -> object:
        """
        Shows exit
        """
        pass

    def go_to_option(self, task: str) -> object:
        """
        Executes the selected controller defined in task
        """
        pass

    def _get_controller_name(self, option: str) -> str:
        """
        Returns controller`s name from menu ini file
        selected in the input
        """
        pass

    def _get_values(self) -> dict:
        """
        Returns a dict with menu values and quit option for menu
        """
        pass
