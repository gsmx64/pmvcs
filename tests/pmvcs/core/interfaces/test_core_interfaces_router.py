""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.router import AbstractRouter

class TestAbstractRouter(unittest.TestCase):
    """ Class for unittest Test Abstract Router """
      
    def test_create_app(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs.create_app.return_value = 5

    def test_get_module_camelcase(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_module_camelcase.return_value = 5

    def test_import_module(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs.import_module.return_value = 5

    def test_get_cfg(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_cfg.return_value = 5

    def test_get_lang(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_lang.return_value = 5

    def test_get_about(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_about.return_value = 5

    def test_get_menus_model(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_menus_model.return_value = 5

    def test_get_model(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_model.return_value = 5

    def test_get_view(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_view.return_value = 5

    def test_get_controller(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_menus_controller.return_value = 5

    def test_get_helper(self):
        """
        Test the abstract class AbstractRouter
        """
        with self.assertRaises(TypeError):
            abs = AbstractRouter()
            abs._get_helper.return_value = 5


if __name__ == '__main__':
    unittest.main()
