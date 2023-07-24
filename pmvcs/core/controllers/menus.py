""" Menus Controller file for Python MVC Shell Framework Package """
from pmvcs.core.interfaces.menus import AbstractMenusController


class MenusController(AbstractMenusController):
    """ Class for PMVCS Menus Controller """
    _menus = {}

    def __init__(self, menus: dict, **kwargs: dict) -> None:
        """
        Init PMVCS Menus Controller requirements
        """
        self._menus = menus
        self.pmvcs_cfg = kwargs['pmvcs_cfg']
        self.pmvcs_lang = kwargs['pmvcs_lang']
        self.pmvcs_about = kwargs['pmvcs_about']
        self.pmvcs_model = kwargs['pmvcs_model']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_controller = kwargs['pmvcs_controller']
        self.pmvcs_helper = kwargs['pmvcs_helper']
        self.router = kwargs['pmvcs_router']

    def go_to_menu(self) -> object:
        """
        Function to build the first level menu options
        """
        print(self.pmvcs_view.get_intro())

        for key, value in self._get_values().items():
            print(self.pmvcs_view.get_menu_options(key, value['text']))

        self.pmvcs_view.line_brake()
        option = self.pmvcs_view.input_options()

        if option.upper() in self._menus.keys() or option.lower() in self._menus.keys():

            if option.lower() == 'q':
                return self.go_to_exit()

            task = self._get_controller_name(option)

            while self.go_to_option(task):
                break
            self.pmvcs_view.clean_screen()
            return self.go_to_menu()

        self.pmvcs_view.clean_screen()
        return self.go_to_menu()

    def go_to_exit(self) -> object:
        """
        Shows exit
        """
        output = self.pmvcs_view.get_exit()
        output += self.pmvcs_view.line_brake(False)
        if self.pmvcs_cfg.get('VIEW_ABOUT_ON_EXIT', 'DEFAULT', 'boolean'):
            for key, value in self.pmvcs_about.to_dict().items():
                output += f'{key}: {value}\n'
        print(output)

    def go_to_option(self, task: str) -> object:
        """
        Executes the selected controller defined in task
        """
        kwargs = {'pmvcs_lang': self.pmvcs_lang,
                  'pmvcs_cfg': self.pmvcs_cfg,
                  'pmvcs_about': self.pmvcs_about,
                  'pmvcs_menus': self,
                  'pmvcs_view': self.pmvcs_view,
                  # (Disabled for now)
                  # 'pmvcs_model': self.pmvcs_model,
                  # 'pmvcs_controller': self.pmvcs_controller,
                  'pmvcs_helper': self.pmvcs_helper}
        controller = self.router.import_module(task, 'Controller', **kwargs)

        return controller.execute()

    def _get_controller_name(self, option: str) -> str:
        """
        Returns controller`s name from menu ini file
        selected in the input
        """
        return str(self._menus[option]['call'])

    def _get_values(self) -> dict:
        """
        Returns a dict with menu values and quit option for menu
        """
        values = self._menus
        values['Q'] = {'text': self.pmvcs_lang.get(
            'LANG_QUIT_LEYEND'), 'call': 'quit'}

        return values
