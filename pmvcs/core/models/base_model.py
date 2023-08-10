""" Base Model file for Python MVC Shell Framework Package """
from pmvcs.core.interfaces.base_model import AbstractBaseModel


class BaseModel(AbstractBaseModel):
    """ Class for PMVCS Base Model """

    def __init__(self, **kwargs) -> None:
        """
        Init the PMVCS Base Model requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']

    @property
    def section(self) -> str:
        """
        Returns only a section
        """
        return self._only_section

    @section.setter
    def section(self, section=None) -> None:
        """
        Sets a section
        """
        self._only_section = section

    def path_exists(self, path: str):
        """
        Returns True or False if file path exists
        """
        pass

    @property
    def file_path(self) -> str:
        """
        Returns file path
        """
        pass

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Sets the file path
        """
        pass

    @property
    def _set_file_path(self) -> None:
        """
        Sets the file path, default None
        """
        pass

    @property
    def update(self) -> None:
        """
        Calls for update the file path
        """
        pass

    @property
    def data(self) -> object:
        """
        Reads parser data, return configparser.ConfigParser()
        """
        pass

    def get(self, key: str, section: str = None,
            types: str = 'str') -> str:
        """
        Gets a data value from a given key
        """
        pass

    def to_dict(self, read_dict: bool = False) -> dict:
        """
        Returns data to dictionary
        """
        pass

    @staticmethod
    def test() -> str:
        """
        Testing function
        """
        return 'Hello from PMVCS Base Model!'
