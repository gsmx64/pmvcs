""" Base View file for PMVCS APP """
from pmvcs.core.decorators.decorators_views import decorate_intro

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

    @decorate_intro(num_lines=1)
    def get_winner(self, number: str) -> str:
        """
        Prints App exit message
        """
        message = f'                 {self.lang.get("LANG_YOU_WIN_TITLE")} \n'
        message += '-'*49+' \n'
        message += self.lang.sprintf("LANG_YOU_WIN_DESC", number) + ' \n'
        return message

    @decorate_intro(num_lines=1)
    def get_game_over(self, number: str) -> str:
        """
        Prints App exit message
        """
        message = f'                 {self.lang.get("LANG_GAME_OVER_TITLE")} \n'
        message += '-'*49+' \n'
        message += self.lang.sprintf("LANG_GAME_OVER_DESC", number) + ' \n'
        return message

    def get_tries_remain(self, value: str) -> str:
        """
        Returns tries remain
        """
        return f'[CodeBreaker] {self.lang.sprintf("LANG_TRIES_REMAIN", value)}'

    def get_text_formated(self, text: str) -> str:
        """
        Returns the player`s name
        """
        return f'[CodeBreaker] {text}'

    def get_insert_number(self, total_tries: str) -> str:
        """
        Returns the inserted number
        """
        return f'[CodeBreaker] {self.lang.sprintf("LANG_ONLY_FOUR_NUMBERS", total_tries)}'

    def input_username(self) -> str:
        """
        Returns the insert player`s name input
        """
        return input(f'[CodeBreaker] {self.lang.get("LANG_INPUT_PLAYER")}: ') or self.lang.get("LANG_ANONIMOUS_PLAYER")

    def input_number(self) -> str:
        """
        Returns the tried number input
        """
        return input(f'[CodeBreaker] {self.lang.get("LANG_INPUT_NUMBER")}: ')
