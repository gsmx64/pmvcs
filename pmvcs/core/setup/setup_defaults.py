""" Setup Defaults file for Python MVC Shell Framework Package """
from pmvcs.core.setup.setup_files import SetupFiles


class SetupDefaults():
    """ Class for PMVCS Setup Defaults """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Defaults requirements
        """
        self.setup = setup
        self.setup_files = SetupFiles(setup)

    def install_defaults(self, app_folder_name: str) -> None:
        """
        Installs default files
        """
        print(
            f'>>> {self.setup.lang_setup.sprintf("SETUP_COPYING_DEFAULTS", self.setup.home_path, app_folder_name)}')
        self.setup_files.copy_files('defaults', app_folder_name)
