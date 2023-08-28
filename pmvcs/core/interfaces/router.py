""" Abstract Router file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractRouter(ABC):
    """ Class for PMVCS Abstract Router """
    _task = ''

    @abstractmethod
    def create_app(self, task='default') -> None:
        """
        Routes the app
        """
        pass

    @abstractmethod
    def _get_module_camelcase(self, module_name: str) -> str:
        """
        Returns module class name in CamelCase
        """
        pass

    @abstractmethod
    def import_module(self, module_name, module_subfix='Controller', **kwargs):
        """
        Imports the module
        """
        pass

    @abstractmethod
    def _get_cfg(self) -> object:
        """
        Returns the PMVCS Configuration Model
        """
        pass

    @abstractmethod
    def _get_lang(self) -> object:
        """
        Returns the PMVCS Language Model
        """
        pass

    @abstractmethod
    def _get_about(self) -> object:
        """
        Returns the PMVCS About Model
        """
        pass

    @abstractmethod
    def _get_menus_model(self, **kwargs) -> object:
        """
        Returns the PMVCS Menus Model
        """
        pass

    @abstractmethod
    def _get_model(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Model
        """
        pass

    @abstractmethod
    def _get_view(self, **kwargs) -> object:
        """
        Returns the PMVCS Base View
        """
        pass

    @abstractmethod
    def _get_controller(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Controller
        """
        pass

    @abstractmethod
    def _get_helper(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Helper
        """
        pass
