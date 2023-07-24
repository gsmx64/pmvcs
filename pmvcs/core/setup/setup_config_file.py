""" Setup Config File file for Python MVC Shell Framework Package """
from pathlib import Path
from importlib.resources import files

from pmvcs.core.setup.setup_files import SetupFiles
from pmvcs.core.setup.setup_parser import SetupParser


class SetupConfigFile():
    """ Class for PMVCS Setup Config File """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Config File requirements
        """
        self.setup = setup
        self.setup_files = SetupFiles(setup)
        self.setup_parser = SetupParser()

    def install_config_file(self, **kwargs) -> None:
        """
        Installs default configuration file and edits the options
        """
        cfg_file = files('pmvcs').joinpath('setup/config.ini')

        try:
            if cfg_file.is_file():
                self.setup_files.copy_file('', 'config.ini', '')

                cfg_file = Path(f'{self.setup.home_path}/config.ini')
                if cfg_file.is_file():
                    parser = self.setup_parser.parser_access(cfg_file)

                    if kwargs['app_name']:
                        app_name = kwargs['app_name']
                    else:
                        app_name = 'MyApp'
                    self.setup_parser.parser_write(
                        parser, "DEFAULT", "DEFAULT_TITLE",
                        app_name, cfg_file)

                    if kwargs['app_folder_name']:
                        app_folder_name = kwargs['app_folder_name']
                    else:
                        app_folder_name = 'app'
                    self.setup_parser.parser_write(
                        parser, "DEFAULT", "APP_FOLDER",
                        app_folder_name, cfg_file)

                    if kwargs['app_debug'] in ['y', 's']:
                        app_debug = 'True'
                    else:
                        app_debug = 'False'
                    self.setup_parser.parser_write(
                        parser, "DEFAULT", "DEBUG",
                        app_debug, cfg_file)

                    if kwargs['app_info'] == 'n':
                        app_info = 'False'
                    else:
                        app_info = 'True'
                    self.setup_parser.parser_write(
                        parser, "DEFAULT", "VIEW_ABOUT_ON_EXIT",
                        app_info, cfg_file)

                    if kwargs['app_multi_lang'] == 'n':
                        app_multi_lang = 'False'
                    else:
                        app_multi_lang = 'True'
                    self.setup_parser.parser_write(
                        parser, "LANGUAGE", "MULTI_LANGUAGE",
                        app_multi_lang, cfg_file)

                    if kwargs['app_def_lang'] == '2':
                        app_def_lang = 'es'
                    else:
                        app_def_lang = 'en'
                    self.setup_parser.parser_write(
                        parser, "LANGUAGE", "DEFAULT_LANGUAGE",
                        app_def_lang, cfg_file)
            else:
                raise FileNotFoundError(
                    self.setup.lang_setup.get("SETUP_ERROR_CFG_NOT_FOUND"))
        except FileNotFoundError as error:
            print(self.setup.lang_setup.sprintf(
                "SETUP_ERROR_CFG_NOT_COPIED", error))
