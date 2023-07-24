""" Setup Menus file for Python MVC Shell Framework Package """
from pathlib import Path

from pmvcs.core.setup.setup_parser import SetupParser


class SetupMenus():
    """ Class for PMVCS Setup Menus """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Menus requirements
        """
        self.setup = setup
        self.setup_parser = SetupParser()

    def install_multiple_module_setup(self) -> None:
        """
        Installs menu options for multiple modules
        """
        if self.setup.no_lang == 'NO_LANG':
            self.setup.clean_screen()
            print(self.setup.get_intro())
            setup_lang = input(f'{self.setup.lang_setup.get("SETUP_INSERT_LANGUAGE")} ').lower()
            if setup_lang in ['en', 'es']:
                self.setup.lang_setup.tag = f'{setup_lang}'
            else:
                self.setup.lang_setup.tag = 'en'
            self.setup.lang_setup.update

        self.setup.clean_screen()
        print(self.setup.get_intro())

        app_folder_name = input(f'[>] {self.setup.lang_setup.get("SETUP_CURRENT_APP_FOLDER")} \n').lower()
        print()

        if self._verify_menu_path(app_folder_name).is_file():
            while self._verify_menu_path(app_folder_name).is_file():
                print(self.get_current_modules_menu(app_folder_name))
                input(f'{self.setup.lang_setup.get("SETUP_PRESS_A_KEY_CONTINUE")} \n')

                self.setup.install_multiple_module(app_folder_name, input(f'{self.setup.lang_setup.get("SETUP_INSERT_MODULE")} '))
                input(f'{self.setup.lang_setup.get("SETUP_PRESS_A_KEY_CONTINUE")} ')

                self.setup.clean_screen()
                print(self.setup.get_intro())
                print(f'{self.setup.lang_setup.get("SETUP_INSERT_ANOTHER_MODULE")}\n', end='')
                add_another_module_input = input(f'{self.setup.lang_setup.get("SETUP_YES_OR_NO")} ').lower()
                print()

                if add_another_module_input not in ['y', 's']:
                    break
        else:
            input(f'>>> {self.setup.lang_setup.get("SETUP_APP_FOLDER_NOT_EXISTS")}\n')

        self.setup.clean_screen()
        print(self.setup.get_exit())

    def get_current_modules_menu(self, app_folder_name: str) -> str:
        """
        Returns current modules in menu
        """
        return_data = '[>] Current Menus\n'
        menu_file = self._verify_menu_path(app_folder_name)
        parser = self.setup_parser.parser_access(menu_file)
        temp_list = list(parser.items("MENUS"))

        for index, module in temp_list:
            module = eval(module)
            return_data += f"[{index}] {module['text']} --> {module['call']}\n"

        return return_data

    def _verify_menu_path(self, app_folder_name: str) -> str:
        """
        Returns current modules in menu
        """
        path = f'{self.setup.home_path}/{app_folder_name}'
        path += f'/languages/{self.setup.lang_setup.tag}.menus.ini'
        return Path(path)
