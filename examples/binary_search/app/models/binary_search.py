""" Binary Search Model file for PMVCS APP """
from app.models.base_model import BaseModel


class BinarySearchModel(BaseModel):
    """ Class for Binary Search Model """
    
    def __init__(self, **kwargs) -> None:
        """
        Init Base View requirements
        """
        super().__init__(**kwargs)

    def get(self, data: list, search: int) -> str:
        """
        Returns a seach from list() using binary search algorithm
        """
        start = 0
        end = len(data) - 1
        half = (start+end)//2
        element = data[half]
        search = int(search)

        while start <= end:

            if data[half] == search:
                return self.lang.sprintf("LANG_MODELS_ALG_BIN_INDEX", search, half)

            if data[half] < search:
                start = half + 1
                end = len(data) - 1
                half = (start + end) // 2
                element = data[half]
                if element == search:
                    return self.lang.sprintf("LANG_MODELS_ALG_BIN_INDEX", element, half)

            if data[half] > search:
                end = half - 1
                half = (start + end) // 2
                element = data[half]
                if element == search:
                    return self.lang.sprintf("LANG_MODELS_ALG_BIN_INDEX", element, half)

        return self.lang.sprintf("LANG_MODELS_ALG_BIN_NOT_IN_LIST", search)
