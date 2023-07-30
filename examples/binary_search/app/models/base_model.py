""" Base Model file for PMVCS APP """
from app.interfaces.base_model import AbstractBaseModel


class BaseModel(AbstractBaseModel):
    """ Class for Base Model """
    _data = ''

    def __init__(self, **kwargs) -> None:
        """
        Init Base Model requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_helper = kwargs['pmvcs_helper']
