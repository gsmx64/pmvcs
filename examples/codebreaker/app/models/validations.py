""" Validations Model for CodeBreaker"""
from app.models.base_model import BaseModel
from app.models.errors import CodeBreackerErrors


class CodeBreackerValidation(BaseModel):
    """ CodeBreacker Validation Class """

    def __init__(self, username: str, **kwargs) -> None:
        """
        Inits the class CodeBreacker Validation
        """
        super().__init__(**kwargs)

        self.username = username
        self.errors = CodeBreackerErrors()

    def is_number(self, number: str) -> bool:
        """
        Validates the 4 digits inserted are numbers
        """
        if number.isnumeric():
            return True

        self.errors.show(
            self.lang.get("LANG_VALIDATION_FOUR_NUMBERS"),
            self.username)
        return False

    def verify_number(self, number: str, secret=True) -> str:
        """
        Validates the secret and typed number in config file
        """
        if not number and secret:
            return self.errors.show(
                self.lang.get("LANG_VALIDATION_SECRET_EMPTY"),
                self.username)

        if not number and not secret:
            return self.errors.show(
                self.lang.get("LANG_VALIDATION_NUMBER_EMPTY"),
                self.username)

        return number

    def verify_repeated_digit(self, number: str) -> str:
        """
        Checks if is a digit of given number are repeated (str)
        """
        repeated_numbers = {}

        for digit in number:
            if digit in repeated_numbers:
                repeated_numbers[digit] += 1
            else:
                repeated_numbers[digit] = 0

        repeated_numbers = {k: v for k, v in repeated_numbers.items() if v > 0}

        if len(repeated_numbers) >= 1:
            return self.errors.show(
                self.lang.get("LANG_VALIDATION_DUPLICATED_DIGITS"),
                self.username)

        return None

    def to_list(self, number: str, secret=True) -> list:
        """
        Validates lenght in secret and typed lists()
        """
        number_list = list(number)
        if len(number_list) != 4 and secret:
            return self.errors.show(
                self.lang.get("LANG_VALIDATION_SECRET_LENGHT"),
                self.username)

        if len(number_list) != 4 and not secret:
            return self.errors.show(
                self.lang.sprintf("LANG_VALIDATION_NUMBER_LENGHT", number),
                self.username)

        return number_list
