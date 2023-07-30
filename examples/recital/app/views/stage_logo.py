""" Stage Logo View for Recital """
from pathlib import Path

from pmvcs.core.views.base_view import BaseView


class StageLogo(BaseView):
    """ Returns a orderer ramdom list from 3 optional modes. """

    def __init__(self, **kwargs) -> None:
        """
        Init Stage View requirements
        """
        super().__init__(**kwargs)

    def get_logo(self) -> str:
        """
        Returns a stage logo in ascii art from a text file
        inside /app/static/txt
        """
        try:
            content = []
            current_path = Path.cwd()
            txt_path = current_path/self.cfg.get("APP_FOLDER", "DEFAULT")/'static'/'txt'/'stage_logo.txt'

            with open(txt_path, 'r', encoding="utf-8") as file:
                content = file.read()
                file.close()

                return content
        except FileNotFoundError as error:
            print(self.lang.sprintf("LANG_ERROR_READING_TXT", txt_path),
                f'Error: {error}')
            return None
        except KeyError as error:
            print(self.lang.sprintf("LANG_ERROR_READING_TXT", txt_path),
                f'Error: {error}')
            return None

    def dummy_func(self):
        """ Dummy DocString"""
        return None
