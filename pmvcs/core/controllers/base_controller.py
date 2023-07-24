""" Base Controller file for Python MVC Shell Framework Package """
from pmvcs.core.interfaces.base_controller import AbstractBaseController
from pmvcs.core.controllers.menus import MenusController


class BaseController(AbstractBaseController):
    """ Class for PMVCS Base Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init the PMVCS Base Controller requirements
        """
        self.pmvcs_cfg = kwargs['pmvcs_cfg']
        self.pmvcs_lang = kwargs['pmvcs_lang']
        self.pmvcs_about = kwargs['pmvcs_about']
        self.pmvcs_model = kwargs['pmvcs_model']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_helper = kwargs['pmvcs_helper']
        self.pmvcs_menus_model = kwargs['pmvcs_menus_model']
        self.pmvcs_router = kwargs['pmvcs_router']

        kwargs['pmvcs_controller'] = self
        self.pmvcs_menus_controller = self._get_menus_controller(
            self.pmvcs_menus_model.to_dict(True), **kwargs)

    def execute(self, task: str) -> object:
        """
        Executes the PMVCS Base Controller
        """
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        if self.pmvcs_cfg.get('MULTI_LANGUAGE', 'LANGUAGE', 'boolean'):
            curr_lang_input = self.pmvcs_view.input_language(
                self._supported_languages())
            curr_lang = self._current_language(curr_lang_input)

            self.pmvcs_lang.tag = curr_lang
            self.pmvcs_lang.update

            self.pmvcs_about.tag = curr_lang
            self.pmvcs_about.update

            self.pmvcs_menus_model.tag = curr_lang
            self.pmvcs_menus_model.update

        self.pmvcs_view.input_start()
        self.pmvcs_view.clean_screen()

        if task == 'default':
            return self.pmvcs_menus_controller.go_to_menu()

        return self.pmvcs_menus_controller.go_to_option(task)

    def _current_language(self, key_input: str) -> str:
        """
        Return current short language tag from input
        """
        lang_dict = self._dict_languages()

        for key, value in enumerate(lang_dict, start=1):
            if int(key_input) == key:
                return value

        return self.pmvcs_cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')

    def _supported_languages(self) -> str:
        """
        Returns supported languages for selection input
        """
        return_string = ''
        lang_list = self._dict_languages()

        for key, value in enumerate(lang_list, start=1):
            return_string += f'\n({key}) {lang_list[value]}'

        return f'{return_string}\n'

    def _dict_languages(self) -> dict:
        """
        Returns supported languages in a dictionary
        Dict = {'lang.tag': 'lang_name'}
        """
        return self.pmvcs_cfg.get('SUPPORTED_LANGUAGES', 'LANGUAGE', 'dict')

    def _get_menus_controller(self, menus_list: list, **kwargs) -> object:
        """
        Returns the PMVCS Menus Controller
        """
        return MenusController(menus_list, **kwargs)

    @staticmethod
    def test() -> str:
        """
        Testing function
        """
        return 'Hello from PMVCS Base Controller!'
