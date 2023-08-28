""" Test file for Python MVC Shell Framework Package """
import unittest

from unittest.mock import Mock, patch

from pmvcs.core.router import Router


class TestRouter(unittest.TestCase):
    """ Class for unittest Test Router """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()

    def test_create_app(self) -> None:
        """
        Test the create_app method
        """
        mock_args = ['1', '', '1','', '', '', '', '', 'q']
        with patch('builtins.input', side_effect=mock_args):
            res = self.router.create_app()

            self.assertEqual(res, None)

    def test_get_providers_check_key(self) -> None:
        """
        Test the return of providers data checking the key
        """
        providers = self.router.get_providers('basic')
        key = 'pmvcs_about'

        self.assertIn(key, providers.keys())

    def test_get_providers_check_value(self) -> None:
        """
        Test the return of providers data checking the value
        """
        providers = self.router.get_providers('basic')
        result = providers['pmvcs_cfg'].get('DEFAULT_LANGUAGE', 'LANGUAGE')
        original = 'en'

        self.assertEqual(original, result)

    def test_error(self) -> None:
        """
        Test the error response on DEBUG False value
        """
        result = self.router._error('ERROR')
        original = ''

        self.assertEqual(original, result)
        
    def test_get_module_camelcase(self) -> None:
        """
        Test the CamelCase string format
        """
        result = self.router._get_module_camelcase('module_name')
        original = 'ModuleName'

        self.assertEqual(original, result)
        
    def test_import_module(self) -> None:
        providers = self.router.get_providers('basic_helper')
        imported_module = self.router.import_module('filters', 'Helper', True, **providers)
        result = imported_module.validate(['jill', 'jack'], list)
        original = True

        self.assertTrue(original, result)

    def test_get_cfg(self) -> None:
        """
        Test the configuration object
        """
        cfg = self.router._get_cfg()
        result = cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')
        original = 'en'

        self.assertEqual(original, result)

    def test_get_lang(self) -> None:
        """
        Test the language object
        """
        cfg = self.router.get_providers('basic')['pmvcs_cfg']
        lang = self.router._get_lang()
        result = lang.get('LANG_QUIT_LEYEND')
        original = 'Quit program'

        self.assertEqual(original, result)

    def test_get_about(self) -> None:
        """
        Test the about object
        """
        cfg = self.router.get_providers('basic')['pmvcs_cfg']
        about = self.router._get_about()
        result = about.get('framework')
        original = 'Python MVC Shell Framework Package'

        self.assertEqual(original, result)

    def test_get_menus_model(self) -> None:
        """
        Test the menus model object
        """
        menus_model = self.router._get_menus_model()
        result = menus_model.get('1')
        original = "{'text': 'Example One', 'call': 'example_one'}"

        self.assertEqual(original, result)

    def test_get_model(self) -> None:
        """
        Test the model object
        """
        providers = self.router.get_providers('basic')
        model = self.router._get_model(**providers)
        result = model.test()
        original = 'Hello from PMVCS Base Model!'

        self.assertEqual(original, result)

    def test_get_view(self) -> None:
        """
        Test the view object
        """
        providers = self.router.get_providers('basic')
        model = self.router._get_view(**providers)
        result = model.test()
        original = 'Hello from PMVCS Base View!'

        self.assertEqual(original, result)

    def test_get_controller(self) -> None:
        """
        Test the controller object
        """
        providers = self.router.get_providers('full')
        model = self.router._get_controller(**providers)
        result = model.test()
        original = 'Hello from PMVCS Base Controller!'

        self.assertEqual(original, result)

    def test_get_helper(self) -> None:
        """
        Test the helper object
        """
        providers = self.router.get_providers('full')
        model = self.router._get_helper(**providers)
        result = model.test()
        original = 'Hello from PMVCS Base Helper!'

        self.assertEqual(original, result)


if __name__ == '__main__':
    unittest.main()
