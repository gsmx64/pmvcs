""" Filters Helper file for Python MVC Shell Framework Package """
from pmvcs.core.helpers.base_helper import BaseHelper


class FiltersHelper(BaseHelper):
    """ Class for Filters Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init PMVCS Base Helper requirements
        """
        super().__init__(**kwargs)

    def float_int(self, value: float | int):
        """
        Returns a float or int value
        """
        value_str = str(value)

        if value_str.replace('.', '', 1).isdigit():
            return float(value)

        if value_str.isnumeric():
            return int(value)

        raise TypeError(self.pmvcs_lang.sprintf(
            "ERROR_TYPE_NOT_FLOAT_OR_INTEGER", value))

    @staticmethod
    def data_type(value: str) -> bool | int | float | str:
        """
        Filter a string variable to bool/int/float/str
        """
        if value.lower() == 'true':
            return bool(True)

        if value.lower() == 'false':
            return bool(False)

        if value.isnumeric():
            return int(value)

        if value.replace('.', '', 1).isdigit():
            return float(value)

        return str(value)

    @staticmethod
    def validate(variable, types):
        """
        Validates a variable
        """
        if isinstance(variable, types):
            return True
        return False
