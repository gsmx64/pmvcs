""" Base Controller file for PMVCS APP """
from app.interfaces.base_controller import AbstractBaseController
from pmvcs.core.views.sample import SampleView


class BaseController(AbstractBaseController):
    """ Class for Base Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init Base Controller requirements
        """
        self.lang = kwargs['pmvcs_lang']
        self.cfg = kwargs['pmvcs_cfg']
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

        self.pmvcs_view.input_pause()

        return False
