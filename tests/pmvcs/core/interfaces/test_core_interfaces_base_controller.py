""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.base_controller import AbstractBaseController

class TestAbstractBaseController(unittest.TestCase):
    """ Class for unittest Test Abstract Base Controller """
      
    def test_execute(self):
        """
        Test the abstract class AbstractBaseController
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseController()
            abs.execute.return_value = 5

    def test_current_language(self):
        """
        Test the abstract class AbstractBaseController
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseController()
            abs._current_language.return_value = 5

    def test_get_menus_controller(self):
        """
        Test the abstract class AbstractBaseController
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseController()
            abs._get_menus_controller.return_value = 5


if __name__ == '__main__':
    unittest.main()
