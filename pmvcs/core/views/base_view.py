""" Base View file for Python MVC Shell Framework Package """
import os

from pmvcs.core.interfaces.base_view import AbstractBaseView
from pmvcs.core.decorators.decorators_views import decorate_intro


class BaseView(AbstractBaseView):
    """ Class for PMVCS Base View """

    def __init__(self, **kwargs) -> None:
        """
        Init the PMVCS Base View requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']

    @decorate_intro(num_lines=3)
    def get_intro(self, dummy='') -> str:
        """
        Returns intro view message
        """
        title = self.cfg.get("DEFAULT_TITLE", "DEFAULT")
        padding_left = self.cfg.get("PADDING_LEFT", "DEFAULT", "int")

        return title.center(padding_left) + '\n'

    @decorate_intro(num_lines=1)
    def get_exit(self, dummy='') -> str:
        """
        Returns exit view message
        """
        self.clean_screen()
        return f' >>> {self.lang.get("LANG_EXIT_PROGRAM")} \n'

    def line_brake(self, prints: bool = True) -> str | None:
        """
        Retuns a linebrake in view
        """
        if prints:
            print('\n', end='')
            return ''

        return '\n'

    def clean_screen(self) -> None:
        """
        Makes a screen clear in view. Calls cls for Windows
        and clear for Unix/Linux
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def input_start(self) -> str:
        """
        Returns the intro input with pause
        """
        return input(f'{self.lang.get("LANG_INPUT_PRESS_A_KEY_START")} ')

    def input_pause(self) -> str:
        """
        Returns the input press a key with pause
        """
        return input(f'{self.lang.get("LANG_INPUT_PRESS_A_KEY_CONTINUE")} ')

    def input_options(self) -> str:
        """
        Returns the select option input
        """
        return input(f'{self.lang.get("LANG_INPUT_SELECT_OPTION")} ')

    def input_generic(self, text: str) -> str:
        """
        Returns a generic input with passed legend
        """
        return input(text)

    def input_language(self, text_options: str) -> str:
        """
        Returns the select language input
        """
        return input(f'{self.lang.sprintf("LANG_SELECT_LANGUAGE", text_options)} ')

    def get_menu_options(self, key: str, value: str) -> str:
        """
        Function to get menu options view formated
        """
        return f'[{key}] {value} '

    @staticmethod
    def test() -> str:
        """
        Testing function
        """
        return 'Hello from PMVCS Base View!'
