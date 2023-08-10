""" About Model file for Python MVC Shell Framework Package """
from pmvcs.core.models.parser import Parser


class About(Parser):
    """ Class for PMVCS About Model """
    _tag = 'en'

    def __init__(self, cfg: object) -> None:
        """
        Init PMVCS About Model requirements
        """
        self.cfg = cfg
        self._only_section = 'ABOUT'
        self._file_path = self._set_file_path

    @property
    def tag(self) -> str:
        """
        Returns default language name tag
        """
        return self._tag

    @tag.setter
    def tag(self, tag: str = 'en') -> None:
        """
        Set default language name tag, (en) for default
        """
        self._tag = tag.lower()

    @property
    def _set_file_path(self) -> str:
        """
        Sets the file path
        """
        path = self.cfg.get("APP_FOLDER", "DEFAULT")
        path += f'/languages/{self.tag}.about.ini'

        if self.path_exists(path) is False:
            raise FileNotFoundError(
                f'[>] ERROR: Language file not found {path}') from None

        return path

    @property
    def update(self) -> None:
        """
        Calls for update the file path
        """
        self._file_path = self._set_file_path
