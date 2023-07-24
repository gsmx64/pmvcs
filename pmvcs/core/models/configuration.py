""" Configuration Model file for Python MVC Shell Framework Package """
from pmvcs.core.models.parser import Parser


class Configuration(Parser):
    """ Class for PMVCS Configuration Model """

    def __init__(self) -> None:
        """
        Init PMVCS Configuration Model requirements
        """
        self._only_section = ''
        self._file_path = self._set_file_path

    @property
    def cfg(self) -> object:
        """
        Returns the language configparser.ConfigParser
        """
        return self.data

    @property
    def _set_file_path(self) -> str:
        """
        Sets the file path
        """
        return 'config.ini'
