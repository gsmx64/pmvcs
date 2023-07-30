""" Screen Helper file for Dojo_Datastructures """
from pmvcs.core.helpers.base_helper import BaseHelper


class ScreenHelper(BaseHelper):
    """ Class for Screen Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init Screen Helper requirements
        """
        super().__init__(**kwargs)

        self.pmvcs_helper = kwargs['pmvcs_helper']
        self.kwargs = { 'pmvcs_cfg': kwargs['pmvcs_cfg'],
                        'pmvcs_lang': kwargs['pmvcs_lang'],
                        'pmvcs_helper': kwargs['pmvcs_helper']}

    def to_string_table(self, data: dict) -> str:
        """
        Show data at screen in table format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        table_helper = self.pmvcs_helper.load_helper('table', **kwargs2)
        table_helper.record_file()

        return table_helper.on_screen()

    def to_string_csv(self, data: dict) -> str:
        """
        Show data at screen in csv format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        csv_helper = self.pmvcs_helper.load_helper('csv', **kwargs2)
        csv_helper.record_file()

        return csv_helper.raw_read_file()

    def to_string_dict(self, data: dict) -> str:
        """
        Show data at screen in dict format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        dict_helper = self.pmvcs_helper.load_helper('dict', **kwargs2)

        return dict_helper.on_screen()

    def to_string_json(self, data: dict) -> str:
        """
        Show data at screen in json format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        json_helper = self.pmvcs_helper.load_helper('json', **kwargs2)
        json_helper.record_file()

        return json_helper.raw_read_file()
