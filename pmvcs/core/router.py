""" Router file for Python MVC Shell Framework Package """
import importlib
import configparser

from pmvcs.core.interfaces.router import AbstractRouter
from pmvcs.core.helpers.base_helper import BaseHelper
from pmvcs.core.models.base_model import BaseModel
from pmvcs.core.models.about import About
from pmvcs.core.models.menus import Menus
from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.language import Language
from pmvcs.core.views.base_view import BaseView
from pmvcs.core.controllers.base_controller import BaseController


class Router(AbstractRouter):
    """ Class for PMVCS Router """
    _task = ''

    def __init__(self) -> None:
        """
        Init PMVCS Router requirements
        """
        self.cfg = self._get_cfg()
        self.lang = self._get_lang()
        self.lang.tag = self.cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')
        self.about = self._get_about()
        self.about.tag = self.cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')
        self.menus_model = self._get_menus_model()
        self.menus_model.tag = self.cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')

        kwargs = {'pmvcs_lang': self.lang,
                  'pmvcs_cfg': self.cfg,
                  'pmvcs_about': self.about}

        kwargs_helpers = {'pmvcs_router': self}
        kwargs_helpers.update(kwargs)
        self.helper = self._get_helper(**kwargs_helpers)
        kwargs['pmvcs_helper'] = self.helper

        self.model = self._get_model(**kwargs)
        self.view = self._get_view(**kwargs)
        kwargs['pmvcs_model'] = self.model
        kwargs['pmvcs_view'] = self.view
        kwargs['pmvcs_router'] = self
        kwargs['pmvcs_menus_model'] = self.menus_model

        self.controller = self._get_controller(**kwargs)

    def create_app(self, task: str = 'default') -> None:
        """
        Routes the app
        """
        try:
            return self.controller.execute(task)
        except (FileNotFoundError,
                TypeError,
                ValueError,
                ImportError,
                AttributeError,
                configparser.Error) as error:
            print(self._error(error))
        return ''

    def _error(self, error: str) -> str:
        error_message = f'[>>>] {error}'

        if self.cfg.get("DEBUG", "DEFAULT", "boolean"):
            import traceback
            error_message += f'[>>>] {traceback.print_tb(error.__traceback__)}'
            return error_message
        return ''

    def _get_module_name(self, module_name: str) -> str:
        """
        Returns module name in string
        """
        return str(module_name)

    def _get_module_camelcase(self, module_name: str) -> str:
        """
        Returns module class name in CamelCase
        """
        splited = module_name.replace("_", " ").split()
        if len(module_name) == 0:
            return module_name
        return ''.join(i.capitalize() for i in splited[0:])

    def import_module(self, module_name: str,
                       module_subfix:str = 'Controller', is_pmvcs: bool = False, **kwargs):
        """
        Imports the module
        """
        try:
            module_class_name = self._get_module_camelcase(module_name)

            if is_pmvcs and module_subfix == 'Helper':
                app_folder = 'pmvcs.core'
            else:
                app_folder = self.cfg.get("APP_FOLDER", "DEFAULT")

            module_import = importlib.import_module(f"{app_folder}.{module_subfix.lower()}s.{module_name}")
            module = getattr(module_import, f"{module_class_name}{module_subfix}")
        except (ImportError, AttributeError) as error:
            raise ValueError(self.pmvcs_lang.sprintf(
                "ERROR_IMPORT_UNKNOWN_FORMAT", error)) from None

        return module(**kwargs)

    def _get_cfg(self) -> object:
        """
        Returns the PMVCS Configuration Model
        """
        return Configuration()

    def _get_lang(self) -> object:
        """
        Returns the PMVCS Language Model
        """
        return Language(self.cfg)

    def _get_about(self) -> object:
        """
        Returns the PMVCS About Model
        """
        return About(self.cfg)

    def _get_menus_model(self, **kwargs) -> object:
        """
        Returns the PMVCS Menus Model
        """
        return Menus(self.cfg, **kwargs)

    def _get_model(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Model
        """
        return BaseModel(**kwargs)

    def _get_view(self, **kwargs) -> object:
        """
        Returns the PMVCS Base View
        """
        return BaseView(**kwargs)

    def _get_controller(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Controller
        """
        return BaseController(**kwargs)

    def _get_helper(self, **kwargs) -> object:
        """
        Returns the PMVCS Base Helper
        """
        return BaseHelper(**kwargs)
