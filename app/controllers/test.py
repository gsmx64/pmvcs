""" Test Controller file for PMVCS APP """


class TestController():
    """ Class for Test Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init Test Controller requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']
        self.menus = kwargs['pmvcs_menus']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_helper = kwargs['pmvcs_helper']

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        print('>>> Insert your code here!')

        self.pmvcs_view.input_pause()
        self.pmvcs_view.clean_screen()

        return self.menus.go_to_exit()
