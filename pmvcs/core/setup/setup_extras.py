""" Setup Extras file for Python MVC Shell Framework Package """
import os

from pmvcs.core.decorators.decorators_views import decorate_intro


class SetupExtras():
    """ Class for PMVCS Setup Extras """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Extras requirements
        """
        self.setup = setup

    @decorate_intro(num_lines=3)
    def get_intro(self, dummy='') -> str:
        """
        Function to get setup intro view message
        """
        title = '-------Python MVC Shell Framework Package--------'
        padding_left = int(5)
        return title.center(padding_left) + '\n'

    @decorate_intro(num_lines=1)
    def get_exit(self, dummy='') -> str:
        """
        Function to get setup exit view message
        """
        self.setup.clean_screen()
        exit_text = f' >>> {self.setup.lang_setup.get("SETUP_FINISHED")} \n'
        exit_text += f' >>> {self.setup.lang_setup.get("SETUP_THANKS")} \n'
        exit_text += '-' * 49 + ' \n'
        exit_text += '(c) 2023 Gonzalo Mahserdjian (GSMx64) \n'
        return exit_text

    def clean_screen(self) -> None:
        """
        Makes a screen clear in view. Calls cls for Windows
        and clear for Unix/Linux
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


class LangDummy():
    """ Dummy Class """

    def get(self, key, section):
        """ Dummy Method """
        pass
