""" Setup Model file for Python MVC Shell Framework Package """
# from pmvcs.core.interfaces.setup import AbstractSetupModel
# AbstractSetupModel
from pathlib import Path

from pmvcs.core.models.language import Language
from pmvcs.core.setup.setup_install import SetupInstall
from pmvcs.core.setup.setup_config_file import SetupConfigFile
from pmvcs.core.setup.setup_defaults import SetupDefaults
from pmvcs.core.setup.setup_example import SetupExample
from pmvcs.core.setup.setup_extras import SetupExtras, LangDummy
from pmvcs.core.setup.setup_menus import SetupMenus
from pmvcs.core.setup.setup_multiple import SetupMultiple
from pmvcs.core.setup.setup_unique import SetupUnique


class SetupModel():
    """ Class for PMVCS Setup Model """

    def __init__(self, current_language: str) -> None:
        """
        Init the PMVCS Base Model requirements
        """
        self.home_path = Path.cwd()
        cfg_dummy = LangDummy()

        self.lang_setup = Language(cfg_dummy)

        if current_language == 'es':
            self.no_lang = None
            self.lang_setup.tag = 'es'
        elif current_language == 'en':
            self.no_lang = None
            self.lang_setup.tag = 'en'
        else:
            self.no_lang = 'NO_LANG'
            self.lang_setup.tag = 'en'
        self.lang_setup.update

    def install_app(self) -> str:
        """
        Returns only a section
        """
        SetupInstall(self).install_app()

    def install_config_file(self, **kwargs) -> str:
        """
        Returns only a section
        """
        SetupConfigFile(self).install_config_file(**kwargs)

    def install_defaults(self, app_folder_name: str) -> None:
        """
        Returns only a section
        """
        SetupDefaults(self).install_defaults(app_folder_name)

    def install_example(self, app_folder_name: str) -> None:
        """
        Returns only a section
        """
        SetupExample(self).install_example(app_folder_name)

    def install_unique_module(self, app_folder_name: str,
                              app_no_menu: str) -> None:
        """
        Returns only a section
        """
        SetupUnique(self).install_unique_module(app_folder_name, app_no_menu)

    def install_multiple_module(self, app_folder_name: str,
                                module_name: str) -> None:
        """
        Returns only a section
        """
        SetupMultiple(self).install_multiple_module(
            app_folder_name, module_name)

    def install_multiple_module_setup(self) -> None:
        """
        Returns only a section
        """
        SetupMenus(self).install_multiple_module_setup()

    def get_intro(self) -> str:
        """
        Function to get intro view message
        """
        return SetupExtras(self).get_intro()

    def get_exit(self) -> str:
        """
        Function to get exit view message
        """
        return SetupExtras(self).get_exit()

    def clean_screen(self) -> None:
        """
        Makes a screen clear in view. Calls cls for Windows
        and clear for Unix/Linux
        """
        SetupExtras(self).clean_screen()
