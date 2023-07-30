""" Base View file for PMVCS APP """
from app.interfaces.base_view import AbstractBaseView


class BaseView(AbstractBaseView):
    """ Class for Base View """

    def __init__(self, **kwargs) -> None:
        """
        Init Base View requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.about = kwargs['pmvcs_about']
        self.pmvcs_view = kwargs['pmvcs_view']
        self.pmvcs_helper = kwargs['pmvcs_helper']

    def input_option(self) -> str:
        """
        Function to get only city path formated (str)
        """
        return input(f'{self.lang.get("LANG_OPTION")} ')

    def get_select_section(self, message: str) -> str:
        """
        Function to get only city path formated (str)
        """
        return f'[>] {message} '

    def get_submenu_options(self, index: int, value: str) -> str:
        """
        Function to get only city path formated (str)
        """
        return f'[{index}] {value} '

    def get_path(self, sections: list) -> str:
        """
        Function to get path (str)
        """
        path = ''
        i = 0

        for section in sections:
            if i == 0:
                path += f'>>> {str(section)}'

            if i >= 1:                
                path += f' -> {str(section)}'
                
            i +=1

        return path
