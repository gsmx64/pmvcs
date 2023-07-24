""" Base Helper file for Python MVC Shell Framework Package """
from pmvcs.core.interfaces.base_helper import AbstractBaseHelper


class BaseHelper(AbstractBaseHelper):
    """ Class for PMVCS Base Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init PMVCS Base Helper requirements
        """
        self.pmvcs_cfg = kwargs['pmvcs_cfg']
        self.pmvcs_lang = kwargs['pmvcs_lang']

        if self.__class__.__name__ == 'BaseHelper':
            self.pmvcs_router = kwargs['pmvcs_router']
        else:
            kwargs['pmvcs_router'] = None

    def load_helper(self, helper_name: str, is_pmvcs=False) -> object:
        """
        Loads a helper
        """
        kwargs = {'pmvcs_cfg': self.pmvcs_cfg,
                  'pmvcs_lang': self.pmvcs_lang,
                  'pmvcs_helper': self}
        return self.pmvcs_router.import_module(
            helper_name, 'Helper', is_pmvcs, **kwargs)

    @staticmethod
    def test() -> str:
        """
        Testing function
        """
        return 'Hello from PMVCS Base Helper!'
