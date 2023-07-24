""" Base View file for PMVCS APP """
from app.interfaces.base_view import AbstractBaseView


class BaseView(AbstractBaseView):
    """ Class for Base View """

    def __init__(self, **kwargs) -> None:
        """
        Init Base View requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_helper = kwargs['pmvcs_helper']
