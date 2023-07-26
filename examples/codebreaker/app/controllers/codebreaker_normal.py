""" Codebreaker Normal Controller file for PMVCS APP """
from app.controllers.base_controller import BaseController
from app.models.codebreaker_normal import CodebreakerNormalModel
from app.views.codebreaker_normal import CodebreakerNormalView
from app.models.codebreaker import CodeBreaker


class CodebreakerNormalController(BaseController):
    """ Class for Codebreaker Normal Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init CodebrakerNormal Controller requirements
        """
        super().__init__(**kwargs)

        self.model = CodebreakerNormalModel(**kwargs)
        self.view = CodebreakerNormalView(**kwargs)

        self.kwargs = kwargs
        self.tries = 1
        self.total_tries = 10

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        print(self.view.get_text_formated(self.lang.get("LANG_INSERT_NAME")))
        username = self.view.input_username()
        print(f'[CodeBreaker] {self.lang.sprintf("LANG_PLAYER_IS", username)}')

        self.total_tries = self.cfg.get("TOTAL_TRIES_NORMAL", "OPTIONS", "int")
        print(self.view.get_text_formated(self.lang.get("LANG_NORMAL_MODE")))
        random_with_duplicates = False

        print(self.view.get_insert_number(self.total_tries))
        number = self.view.input_number()

        codebreaker = CodeBreaker(number,
                                  username,
                                  random_with_duplicates,
                                  **self.kwargs)

        while self.tries != self.total_tries:

            challenge = codebreaker.challenge()

            if challenge:
                self.pmvcs_view.clean_screen()
                print(self.pmvcs_view.get_intro())

                print(self.view.get_text_formated(
                    self.lang.sprintf("LANG_NUMBER_INSERTED", number)))
                print(self.view.get_text_formated(
                    self.lang.sprintf("LANG_OUTPUT_RESULT", challenge)))
                self.tries += 1
                tries_remain = self.total_tries-self.tries+1

                # print(f'TESTING!!! - REAL NUMBER: {codebreaker.realnumber}')
                print(self.view.get_tries_remain(tries_remain))

            number = self.view.input_number()
            print(self.view.get_text_formated(
                self.lang.sprintf("LANG_NUMBER_INSERTED", number)))
            codebreaker.update_number(number)

            if isinstance(codebreaker.is_winner,
                          bool) and codebreaker.is_winner:
                self.pmvcs_view.clean_screen()
                print(self.pmvcs_view.get_intro())
                print(self.view.get_winner(codebreaker.realnumber))
                self.pmvcs_view.input_pause()
                break
        else:
            self.pmvcs_view.clean_screen()
            print(self.pmvcs_view.get_intro())
            print(self.view.get_game_over(codebreaker.realnumber))
            self.pmvcs_view.input_pause()
            self.tries = 1

        return False
