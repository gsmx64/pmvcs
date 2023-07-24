""" Setup Multiple file for Python MVC Shell Framework Package """
from pathlib import Path

from pmvcs.core.setup.setup_files import SetupFiles
from pmvcs.core.setup.setup_parser import SetupParser


class SetupMultiple():
    """ Class for PMVCS Setup Multiple """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Multiple requirements
        """
        self.setup = setup
        self.setup_files = SetupFiles(setup)
        self.setup_parser = SetupParser()

    def install_multiple_module(self, app_folder_name: str,
                                module_name: str) -> None:
        """
        Installs multiple modules with menu to select each one
        """
        module_name = module_name.lower()
        app_path = f'{self.setup.home_path}/{app_folder_name}/'

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_CUSTOM_MODULE", self.setup.home_path, app_folder_name, "controllers")}')
        self.setup_files.copy_file('modules_base', 'controllers/controller.py', app_folder_name)
        self.setup_files.rename_file(f'{app_path}controllers/', 'controller.py', f'{module_name}.py')

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_CUSTOM_MODULE", self.setup.home_path, app_folder_name, "models")}')
        self.setup_files.copy_file('modules_base', 'models/model.py', app_folder_name)
        self.setup_files.rename_file(f'{app_path}models/', 'model.py', f'{module_name}.py')

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_CUSTOM_MODULE", self.setup.home_path, app_folder_name, "views")}')
        self.setup_files.copy_file('modules_base', 'views/view.py', app_folder_name)
        self.setup_files.rename_file(f'{app_path}views/', 'view.py', f'{module_name}.py')

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_EDITING_MODULES_FILES", self.setup.home_path, app_folder_name, module_name)}')
        module_class = self.setup_files.to_camelcase(module_name)
        module_class_spaced = self.setup_files.to_camelcase(module_name, True)

        print(f'app_path: {app_path}')
        self.setup_files.edit_files(app_path, 'from app.', f'from {app_folder_name}.')
        self.setup_files.edit_files(app_path, 'example_one', module_name)
        self.setup_files.edit_files(app_path, 'ExampleOne', module_class)
        self.setup_files.edit_files(app_path, 'Example One', module_class_spaced)

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_EDITING_MODULES_MENUS", self.setup.home_path, app_folder_name, module_name)}')
        cfg_file = Path(f'{app_path}languages/en.menus.ini')
        if cfg_file.is_file():
            parser = self.setup_parser.parser_access(cfg_file)
            temp_list = list(parser.items("MENUS"))

            try:
                next_key = str(int(temp_list[-1][0]) + 1)
            except IndexError:
                next_key = '1'

            value = f"['text': '{module_class_spaced}', 'call': '{module_name}']".replace('[', '{').replace(']', '}')
            self.setup_parser.parser_write(parser, "MENUS", next_key, value, cfg_file)

        cfg_file = Path(f'{app_path}languages/es.menus.ini')
        if cfg_file.is_file():
            parser = self.setup_parser.parser_access(cfg_file)
            temp_list = list(parser.items("MENUS"))

            try:
                next_key = str(int(temp_list[-1][0]) + 1)
            except IndexError:
                next_key = '1'

            value = f"['text': '{module_class_spaced}', 'call': '{module_name}']".replace('[', '{').replace(']', '}')
            self.setup_parser.parser_write(parser, "MENUS", next_key, value, cfg_file)
