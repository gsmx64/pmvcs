""" Language Model file for Python MVC Shell Framework Package """
from pmvcs.core.models.parser import Parser


class Language(Parser):
    """ Class for PMVCS Language Model """
    _tag = 'en'

    def __init__(self, cfg: object) -> None:
        """
        Init PMVCS Language Model requirements
        """
        self.cfg = cfg
        self._only_section = 'LANG'
        self._file_path = self._set_file_path

    @property
    def lang(self) -> object:
        """
        Returns the language configparser.ConfigParser
        """
        return self.data

    @property
    def tag(self) -> str:
        """
        Returns default language name tag
        """
        return self._tag

    @tag.setter
    def tag(self, tag='en') -> None:
        """
        Set default language name tag, (en) for default
        """
        self._tag = tag.lower()

    @property
    def _set_file_path(self) -> str:
        """
        Sets the file path
        """
        if self.cfg.get("APP_FOLDER", "DEFAULT"):
            path = self.cfg.get("APP_FOLDER", "DEFAULT")
            path += f'/languages/{self.tag}.ini'
        else:
            path = f'/languages/{self.tag}.ini'

        if self.path_exists(path) is False:
            from importlib.resources import files
            path = files('pmvcs').joinpath(
                f'core/setup/languages/{self._tag}.setup.ini')

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

    def sprintf(self, text, *args, **kwargs) -> str:
        """
        Return a formatted string
        """
        return self.get(text).format(*args, **kwargs)

    def translate(self, text) -> str:
        """
        Return a translated string
        """
        import configparser
        default = {text: text}

        try:
            return self.data.get(self._only_section, text)
        except configparser.NoOptionError:
            return self.data.get(self._only_section, text, vars=default)
