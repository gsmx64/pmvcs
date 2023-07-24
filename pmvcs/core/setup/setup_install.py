""" Setup Install file for Python MVC Shell Framework Package """
from pathlib import Path


class SetupInstall():
    """ Class for PMVCS Setup Install """

    def __init__(self, setup: object) -> None:
        """
        Init the PMVCS Setup Install requirements
        """
        self.setup = setup

    def install_app(self) -> None:
        """
        Inits the installation, configuration and data for the app
        """
        if self.setup.no_lang == 'NO_LANG':
            self.setup.clean_screen()
            print(self.setup.get_intro())
            setup_lang = input(
                f'{self.setup.lang_setup.get("SETUP_INSERT_LANGUAGE")} ').lower()
            if setup_lang in ['en', 'es']:
                self.setup.lang_setup.tag = f'{setup_lang}'
            else:
                self.setup.lang_setup.tag = 'en'
            self.setup.lang_setup.update

        self.setup.clean_screen()
        print(self.setup.get_intro())
        app_name = input(
            f'{self.setup.lang_setup.get("SETUP_INSERT_APP_NAME")} ')

        self.setup.clean_screen()
        print(self.setup.get_intro())
        app_folder_name = input(
            f'{self.setup.lang_setup.get("SETUP_INSERT_APP_FOLDER")} ').lower()

        self.setup.clean_screen()
        print(self.setup.get_intro())
        print(f'{self.setup.lang_setup.get("SETUP_ENABLE_DEBUG")}\n', end='')
        app_debug = input(
            f'{self.setup.lang_setup.get("SETUP_YES_OR_NO")} ').lower()

        self.setup.clean_screen()
        print(self.setup.get_intro())
        print(f'{self.setup.lang_setup.get("SETUP_ENABLE_INFO")}\n', end='')
        app_info = input(
            f'{self.setup.lang_setup.get("SETUP_YES_OR_NO")} ').lower()

        self.setup.clean_screen()
        print(self.setup.get_intro())
        print(f'{self.setup.lang_setup.get("SETUP_ENABLE_MULTILANG")}\n', end='')
        app_multi_lang = input(
            f'{self.setup.lang_setup.get("SETUP_YES_OR_NO")} ').lower()

        self.setup.clean_screen()
        print(self.setup.get_intro())
        print(f'{self.setup.lang_setup.get("SETUP_SET_DEF_LANG")}\n', end='')
        app_def_lang = input(
            f'{self.setup.lang_setup.get("SETUP_SET_DEF_LANG_VALUES")}  ')

        kwargs = {'app_name': app_name,
                  'app_folder_name': app_folder_name,
                  'app_debug': app_debug,
                  'app_info': app_info,
                  'app_multi_lang': app_multi_lang,
                  'app_def_lang': app_def_lang}
        self.setup.install_config_file(**kwargs)

        self._mkdir_app_folders(app_folder_name)

        self.setup.clean_screen()
        print(self.setup.get_intro())
        print(f'{self.setup.lang_setup.get("SETUP_INSTALL_OPTIONS")}\n', end='')
        app_menu = input(
            (f'{self.setup.lang_setup.get("SETUP_INSTALL_OPTIONS_VALUES")} ')).lower()
        print()

        while app_menu in ['e', 'm', 's']:
            if app_menu == 'e':
                self.setup.install_example(app_folder_name)
                input(f'{self.setup.lang_setup.get("SETUP_PRESS_A_KEY_CONTINUE")} ')
                break

            if app_menu == 's':
                app_no_menu = input('Insert module name: ')
                self.setup.install_unique_module(app_folder_name, app_no_menu)
                input(f'{self.setup.lang_setup.get("SETUP_PRESS_A_KEY_CONTINUE")} ')
                break

            if app_menu == 'm':
                self.setup.install_defaults(app_folder_name)
                print()

                while True:
                    self.setup.install_multiple_module(app_folder_name, input(
                        f'{self.setup.lang_setup.get("SETUP_INSERT_MODULE")} '))
                    input(
                        f'{self.setup.lang_setup.get("SETUP_PRESS_A_KEY_CONTINUE")} ')

                    self.setup.clean_screen()
                    print(self.setup.get_intro())
                    print(
                        f'{self.setup.lang_setup.get("SETUP_INSERT_ANOTHER_MODULE")}\n',
                        end='')
                    add_another_module_input = input(
                        f'{self.setup.lang_setup.get("SETUP_YES_OR_NO")} ').lower()
                    print()

                    if add_another_module_input not in ['y', 's']:
                        break
                break

        self.setup.clean_screen()
        print(self.setup.get_exit())

    def _mkdir_app_folders(self, app_folder_name: str, path='') -> None:
        """
        Makes a folder in selected path if exists
        """
        new_app_path = Path(f'{self.setup.home_path}/{app_folder_name}/{path}')
        if not new_app_path.exists():
            new_app_path.mkdir()
