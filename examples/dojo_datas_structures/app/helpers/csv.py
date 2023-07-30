""" CSV Helper file for Dojo_Datastructures """
import csv
import os
from pathlib import Path

from pmvcs.core.helpers.base_helper import BaseHelper


class CsvHelper(BaseHelper):
    """ Class for Csv Helper """
    _data = ''
    _file_name = ''
    _file_extension = 'csv'

    def __init__(self, **kwargs) -> None:
        """
        Init Csv Helper requirements
        """
        super().__init__(**kwargs)

        self._data = kwargs['data']
        self._file_name = f"{kwargs['file_name']}.{self._file_extension}"

    @property
    def file_path(self) -> Path:
        """
        Returns file path
        """
        current_path = Path.cwd()
        return current_path / self.pmvcs_cfg.get("APP_FOLDER", "DEFAULT") / 'static' / 'csv' / self._file_name

    @property
    def field_names(self) -> list:
        """
        Returns field names
        """
        if isinstance(self._data, dict):
            return self._data[0].keys()

        return list(self._data[0])

    def raw_read_file(self) -> str:
        """
        Reads a csv file
        """
        output = []

        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                for row in file.readlines():
                    output.append(row)

            return ''.join(output)
        except Exception as error:
            return error

    def record_file(self) -> str:
        """
        Records a csv file
        """
        if os.name == 'nt':
            newline_value = ''
        else:
            newline_value = '\n'

        table_list = []

        if isinstance(self._data, dict):
            table_list = self._data.values()
        else:
            table_list = self._data

        try:
            with open(self.file_path, 'w', newline=newline_value, encoding="utf-8") as file:
                writer = csv.DictWriter(file, self.field_names, delimiter=',')
                writer.writeheader()
                writer.writerows(table_list)

            return self.pmvcs_lang.sprintf("LANG_FILE_SAVED_TO", self._file_extension, self.file_path)
        except Exception as error:
            return error
