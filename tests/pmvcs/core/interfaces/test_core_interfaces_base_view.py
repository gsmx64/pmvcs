""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.base_view import AbstractBaseView

class TestAbstractBaseView(unittest.TestCase):
    """ Class for unittest Test Abstract Base View """
      
    def test_get_intro(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.get_intro.return_value = 5

    def test_get_exit(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.get_exit.return_value = 5

    def test_line_brake(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.line_brake.return_value = 5

    def test_clean_screen(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.clean_screen.return_value = 5

    def test_input_start(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.input_start.return_value = 5

    def test_input_pause(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.input_pause.return_value = 5

    def test_input_options(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.input_options.return_value = 5

    def test_input_generic(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.input_generic.return_value = 5

    def test_input_language(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.input_language.return_value = 5

    def test_get_menu_options(self):
        """
        Test the abstract class AbstractBaseView
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseView()
            abs.get_menu_options.return_value = 5


if __name__ == '__main__':
    unittest.main()
