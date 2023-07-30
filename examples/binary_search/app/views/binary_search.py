""" Binary Search View file for PMVCS APP """
from app.views.base_view import BaseView


class BinarySearchView(BaseView):
    """ Class for Binary Search View  """

    def __init__(self, **kwargs) -> None:
        """
        Init Base View requirements
        """
        super().__init__(**kwargs)
        
    def input_pause_repeat(self) -> str:
        """
        Returns the pause option to repeat binary search
        """
        return input(f'{self.lang.get("LANG_INPUT_PRESS_REPEAT_OR_QUIT")} ')
    
    def get_data_output(self, mode: str, data: list) -> str:
        """
        Returns the list[mode] title and the data
        """
        return self.lang.sprintf("LANG_OUTPUT_LIST", mode, data)

    def get_input_search(self) -> str:
        """
        Returns the binary search input
        """
        return input(f'{self.lang.get("LANG_INPUT_SEARCH_NUMBER")} ')

    def get_result_output(self, result: str) -> str:
        """
        Returns the result title and result from binary search
        """
        return self.lang.sprintf("LANG_OUTPUT_RESULT", result)
