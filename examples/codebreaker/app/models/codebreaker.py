""" Core Model for CodeBreaker"""
import random
from random import randint

from app.models.base_model import BaseModel
from app.models.validations import CodeBreackerValidation


class CodeBreaker(BaseModel):
    """ Class for CodeBreaker Model """

    def __init__(self, number: str,  username: str, duplicates: bool,
                 **kwargs) -> None:
        """
        Inits the class CodeBreaker (str)
        """
        super().__init__(**kwargs)

        self.validation = CodeBreackerValidation(username, **kwargs)
        self.show_x_not_number = self.cfg.get(
            "USE_X_NOT_NUMBER", "OPTIONS", "boolean")

        self.username = username
        self.number = number
        self.duplicates = duplicates
        self.secret_number = self._secret_number

    def challenge(self) -> str:
        """
        Returns X for guessed digit or _ for a digit inside number.
        """
        if self.validation.is_number(self.number):

            secret_number = self.validation.verify_number(
                self.secret_number, True)
            number = self.validation.verify_number(self.number, False)

            number_list = self.validation.to_list(number, False)

            if self.duplicates:
                return self._check_digit(number_list, secret_number)

            if self.validation.verify_repeated_digit(number) is None:
                return self._check_digit(number_list, secret_number)
        return None

    def update_number(self, number: str):
        """
        Updates the typed number (str)
        """
        self.number = number

    @property
    def is_winner(self) -> bool:
        """
        If you guess the secret number, returns a bolean value (True)
        """
        return self.number == self.secret_number

    @property
    def realnumber(self) -> str:
        """
        Returns the hidden secret number
        """
        return self.secret_number

    @property
    def _secret_number(self):
        """
        Returns the current secret number
        """
        if isinstance(self.cfg.get("USE_RAMDOM_NUMBER", "OPTIONS", "boolean"),
                      bool) and self.cfg.get("USE_RAMDOM_NUMBER", "OPTIONS", "boolean"):
            if self.duplicates:
                random_number = str(randint(0, 99999))
                return random_number[-4:]

            return ''.join(map(str, random.sample(range(0, 9), 4)))

        return self.cfg.get("SECRET_NUMBER", "OPTIONS")

    def _check_digit(self, number: list, secret_number: str) -> str:
        """
        Returns the the guessed numbers, chars by chars giving X or _
        """
        result_value = ''

        try:
            if not isinstance(number, list):
                return number

            for index, value in enumerate(number, start=0):
                if secret_number[index] == value:
                    if self.show_x_not_number:
                        result_value += 'X'
                    else:
                        result_value += number[index]
                if secret_number[index] != value and value in secret_number:
                    result_value += '_'
                if secret_number[index] != value and value not in secret_number:
                    result_value += ' '

            return result_value
        except IndexError as error:
            message = f'ERROR: {error} - Index: {index} - Number: {"".join(number)} - Secret: {secret_number} - Result: {result_value}'
            print(message)
            return message
