""" Errors Model for CodeBreaker"""


class CodeBreackerErrors():
    """ CodeBreacker Errors Class """

    @classmethod
    def show(cls, message: str, username: str) -> str:
        """
        Prints formated texts of errors
        """
        print((f'[CodeBreaker] {username}: {message}'))

        return False
