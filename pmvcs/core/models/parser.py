""" Parser Model file for Py MVC Prompt Package """
import os
import configparser

from pmvcs.core.models.base_model import BaseModel


class Parser(BaseModel):
    """ Class for PMVCS Parser Model """
    _file_path = ''
    _only_section = ''

    def __init__(self) -> None:
        """
        Init PMVCS Parser Model requirements
        """
        if self.section:
            self._only_section = self.section

    def path_exists(self, path: str) -> bool:
        """
        Returns True or False if file path exists
        """
        return os.path.exists(path)

    @property
    def file_path(self) -> str:
        """
        Returns file path
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Sets the file path
        """
        if self._set_file_path:
            self._file_path = self._set_file_path
        else:
            self._file_path = file_path

    @property
    def _set_file_path(self) -> None:
        """
        Sets the file path, default None
        """
        return None

    @property
    def update(self) -> None:
        """
        Calls for update the file path
        """
        return None

    @property
    def data(self) -> configparser.ConfigParser:
        """
        Reads parser data, return configparser.ConfigParser()
        """
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.sections()
        parser.read(self.file_path, 'UTF-8')

        return parser

    def get(self, key, section=None, types='str') -> str:
        """
        Gets a data value from a given key
        """
        if section is None and self._only_section:
            section = self._only_section

        if types == 'int':
            return self.data.getint(section, key)

        if types == 'float':
            return self.data.getfloat(section, key)

        if types == 'boolean':
            return self.data.getboolean(section, key)

        if types == 'list':
            evals = eval(self.data.get(section, key))
            if isinstance(evals, list):
                return list(evals)

        if types == 'dict':
            evals = eval(self.data.get(section, key))
            if isinstance(evals, dict):
                return dict(evals)

        return self.data.get(section, key).replace("\\n", "\n")

    def to_dict(self, read_dict=False) -> dict:
        """
        Returns data to dictionary
        """
        data_dict = {}

        if self._only_section:
            for key, value in self.data.items(self._only_section):
                if read_dict:
                    data_dict[key] = eval(value)
                else:
                    data_dict[key] = value
        else:
            for section in self.data.sections():
                data_dict[section] = {}
                for key, value in self.data.items(section):
                    if read_dict:
                        data_dict[section][key] = eval(value)
                    else:
                        data_dict[section][key] = value

        return data_dict
