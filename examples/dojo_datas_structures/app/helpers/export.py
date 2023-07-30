""" Export Helper file for Dojo_Datastructures """
from pmvcs.core.helpers.base_helper import BaseHelper


class ExportHelper(BaseHelper):
    """ Class for Export Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init Export Helper requirements
        """
        super().__init__(**kwargs)

        self.pmvcs_helper = kwargs['pmvcs_helper']
        self.kwargs = { 'pmvcs_cfg': self.pmvcs_cfg,
                        'pmvcs_lang': self.pmvcs_lang,
                        'pmvcs_helper': self}

    def save_to_table(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a txt file in table format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        table_helper = self.pmvcs_helper.load_helper('table', **kwargs2)
        table_helper.record_file()

        return table_helper.record_file()

    def save_to_csv(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a csv file format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        csv_helper = self.pmvcs_helper.load_helper('csv', **kwargs2)

        return csv_helper.record_file()

    def save_to_dict(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a txt file in dict format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        dict_helper = self.pmvcs_helper.load_helper('dict', **kwargs2)

        return dict_helper.record_file()

    def save_to_json(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a json file format
        """
        kwargs2 = {'data': data,
                  'file_name': 'temp_file'}
        kwargs2.update(self.kwargs)
        json_helper = self.pmvcs_helper.load_helper('json', **kwargs2)

        return json_helper.record_file()
