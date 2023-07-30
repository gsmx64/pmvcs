""" Base Model file for PMVCS APP """
from app.interfaces.base_model import AbstractBaseModel


class BaseModel(AbstractBaseModel):
    """ Class for Base Model """
    _data = ''

    def __init__(self, **kwargs) -> None:
        """
        Init Base Model requirements
        """
        self.pmvcs_cfg = kwargs['pmvcs_cfg']
        self.pmvcs_lang = kwargs['pmvcs_lang']
        self.pmvcs_helper = kwargs['pmvcs_helper']
        
        self.kwargs = { 'pmvcs_cfg': kwargs['pmvcs_cfg'],
                        'pmvcs_lang': kwargs['pmvcs_lang'],
                        'pmvcs_helper': kwargs['pmvcs_helper']}

        self._data = self.data

    @property
    def data(self) -> dict:
        """
        Returns getter for data (dict)
        """
        return self._data

    @data.setter
    def data(self, data: dict) -> list:
        """
        Returns setter for data (dict)
        """
        self._data = data

    def make_export(self, section: str, formats: str, output: str) -> dict:
        """
        Splits export between screen or file (dict)
        """
        if output == 'screen':
            return self.make_export_to_screen(section, formats)

        if output == 'file':
            return self.make_export_to_file(section, formats)

        raise Exception(self.pmvcs_lang.get("LANG_ERROR_NO_OUTPUT"))

    def make_export_to_screen(self, section: str, formats: str) -> dict:
        """
        Return screen export (dict)
        """
        screen = self.pmvcs_helper.load_helper('screen', **self.kwargs)

        if formats == 'table':
            return screen.to_string_table(self._prepare_export(section))

        if formats == 'dictionary':
            return screen.to_string_dict(self._prepare_export(section))

        if formats == 'csv':
            return screen.to_string_csv(self._prepare_export(section))

        if formats == 'json':
            return screen.to_string_json(self._prepare_export(section))

        raise Exception(self.pmvcs_lang.get("LANG_ERROR_NO_FORMAT"))

    def make_export_to_file(self, section: str, formats: str) -> dict:
        """
        Return file export (dict)
        """
        export = self.pmvcs_helper.load_helper('export', **self.kwargs)
        file_name = input(self.pmvcs_lang.get("LANG_INSERT_FILE_NAME"))

        if formats == 'table':
            return export.save_to_table(self._prepare_export(section), file_name)

        if formats == 'dictionary':
            return export.save_to_dict(self._prepare_export(section), file_name)

        if formats == 'csv':
            return export.save_to_csv(self._prepare_export(section), file_name)

        if formats == 'json':
            return export.save_to_json(self._prepare_export(section), file_name)

        raise Exception(self.pmvcs_lang.get("LANG_ERROR_NO_FORMAT"))

    def _prepare_export(self, section: str) -> list | dict:
        """
        Prepare data for export (dict)
        """
        keys = self._formater_decode(section)

        return self._formater_encode(keys)

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        return []

    def _formater_encode(self, datas: list) -> list | dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        return datas
