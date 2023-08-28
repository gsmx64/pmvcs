""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.menus import AbstractMenusController

class TestAbstractMenusController(unittest.TestCase):
    """ Class for unittest Test Abstract Menus Controller """
      
    def test_go_to_menu(self):
        """
        Test the abstract class AbstractMenusController
        """
        abs = AbstractMenusController()
        print(abs.go_to_menu())

    def test_go_to_exit(self):
        """
        Test the abstract class AbstractMenusController
        """
        abs = AbstractMenusController()
        print(abs.go_to_exit())

    def test_go_to_option(self):
        """
        Test the abstract class AbstractMenusController
        """
        with self.assertRaises(TypeError):
            abs = AbstractMenusController()
            print(abs.go_to_option().return_value())

    def test_get_controller_name(self):
        """
        Test the abstract class AbstractMenusController
        """
        abs = AbstractMenusController()
        print(abs._get_controller_name('test'))

    def test_get_values(self):
        """
        Test the abstract class AbstractMenusController
        """
        abs = AbstractMenusController()
        print(abs._get_values())        


if __name__ == '__main__':
    unittest.main()
