""" Abstract Base Model file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractBaseModel(ABC):
    """ Class for PMVCS Abstract Base Model """

    @property
    @abstractmethod
    def section(self) -> str:
        """
        Returns only a section
        """
        pass

    @section.setter
    @abstractmethod
    def section(self, section=None) -> None:
        """
        Sets a section
        """
        pass

    @abstractmethod
    def path_exists(self, path: str) -> bool:
        """
        Returns True or False if file path exists
        """
        pass

    @property
    @abstractmethod
    def file_path(self) -> str:
        """
        Returns file path
        """
        pass

    @file_path.setter
    @abstractmethod
    def file_path(self, file_path: str) -> None:
        """
        Sets the file path
        """
        pass

    @property
    @abstractmethod
    def _set_file_path(self) -> None:
        """
        Sets the file path, default None
        """
        pass

    @property
    @abstractmethod
    def update(self) -> None:
        """
        Calls for update the file path
        """
        pass

    @property
    @abstractmethod
    def data(self) -> object:
        """
        Reads parser data, return configparser.ConfigParser()
        """
        pass

    @abstractmethod
    def get(self, key, section=None, types='str') -> str:
        """
        Gets a data value from a given key
        """
        pass

    @abstractmethod
    def to_dict(self, read_dict=False) -> dict:
        """
        Returns data to dictionary
        """
        pass
