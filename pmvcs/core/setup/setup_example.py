""" Setup Example file for Python MVC Shell Framework Package """
from pmvcs.core.setup.setup_files import SetupFiles


class SetupExample():
    """ Class for PMVCS Setup Example """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Example requirements
        """
        self.setup = setup
        self.setup_files = SetupFiles(setup)

    def install_example(self, app_folder_name: str) -> None:
        """
        Installs default and example data
        """
        self.setup.install_defaults(app_folder_name)

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_EXAMPLES", self.setup.home_path, app_folder_name)}')
        self.setup_files.copy_files('example', app_folder_name)

        print(f'>>> {self.setup.lang_setup.sprintf("SETUP_EDITING_FILES", self.setup.home_path, app_folder_name)}')
        self.setup_files.edit_files(
            f'{self.setup.home_path}/{app_folder_name}/',
            'from app.', f'from {app_folder_name}.')
