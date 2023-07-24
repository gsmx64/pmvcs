""" Setup Unique file for Python MVC Shell Framework Package """
from pmvcs.core.setup.setup_files import SetupFiles


class SetupUnique():
    """ Class for PMVCS Setup Unique """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Unique requirements
        """
        self.setup = setup
        self.setup_files = SetupFiles(setup)

    def install_unique_module(self, app_folder_name: str,
                              app_no_menu: str) -> None:
        """
        Installs unique and custom module (no menu)
        """
        self.setup.install_defaults(app_folder_name)
        app_no_menu = app_no_menu.lower()
        app_path = f'{self.setup.home_path}/{app_folder_name}/'

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_UNIQUE", self.setup.home_path, app_folder_name)}')
        self.setup_files.copy_file(
            'module_unique', 'controllers/unique.py', app_folder_name)

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_EDITING_FILES", self.setup.home_path, app_folder_name)}')
        self.setup_files.rename_file(
            f'{app_path}controllers/', 'unique.py', f'{app_no_menu}.py')
        self.setup_files.edit_files(
            f'{app_path}', 'from app.', f'from {app_folder_name}.')

        module_class = self.setup_files.to_camelcase(app_no_menu)
        module_class_spaced = self.setup_files.to_camelcase(app_no_menu, True)
        self.setup_files.edit_file(
            f'{app_path}controllers/{app_no_menu}.py',
            'UniqueController', f'{module_class}Controller')
        self.setup_files.edit_file(
            f'{app_path}controllers/{app_no_menu}.py',
            'Unique Controller', f'{module_class_spaced} Controller')

        self.setup_files.edit_file(
            f'{self.setup.home_path}/{app_folder_name}.py',
            'app.create_app()', f"app.create_app('{app_no_menu}')")
