""" Test file for Python MVC Shell Framework Package """
import unittest
import sys
import io
import os

from unittest.mock import patch

from pmvcs.core.router import Router
from pmvcs.core.views.base_view import BaseView


class TestBaseView(unittest.TestCase):
    """ Class for unittest Test BaseView """

    def setUp(self):
        """
        Instance the unittest
        """
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']
        self.lang = providers['pmvcs_lang']
        self.pmvcs_view = BaseView(**providers)

    def test_get_intro(self):
        """
        Test the return of intro view message
        """
        result = self.pmvcs_view.get_intro()
        original = """------------------------------------------------- 
------------------------------------------------- 
------------------------------------------------- 
                   Example App                    
------------------------------------------------- 
------------------------------------------------- 
------------------------------------------------- 
"""

        self.assertEqual(original, result)

    def test_get_exit(self):
        """
        Test the return of exit view message
        """
        result = self.pmvcs_view.get_exit()
        original = """------------------------------------------------- 
 >>> The program ended 
------------------------------------------------- 
"""

        self.assertEqual(original, result)

    def test_line_brake_print_false(self):
        """
        Test the return of linebrake in view without print output
        """
        result = self.pmvcs_view.line_brake(False)
        original = '\n'

        self.assertEqual(original, result)

    def test_line_brake_print_true(self):
        """
        Test the return of linebrake in view without print output
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.pmvcs_view.line_brake(True)
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__
        
        original = '\n'

        self.assertEqual(original, result)

    @patch('os.system')
    def test_clean_screen(self, mock_system):
        """
        Test the screen clear in view
        """
        self.pmvcs_view.clean_screen()

        if os.name == 'nt':
            mock_system.assert_called_once_with('cls')
        else:
            mock_system.assert_called_once_with('clear')

    def test_input_start(self):
        """
        Test the input for intro press a key in start
        """
        with patch('builtins.input', return_value = 'ENTER'):
            self.assertEqual(self.pmvcs_view.input_start(), 'ENTER')

    def test_input_pause(self):
        """
        Test the input for intro press a key pause
        """
        with patch('builtins.input', return_value = 'ENTER'):
            self.assertEqual(self.pmvcs_view.input_pause(), 'ENTER')

    def test_input_options(self):
        """
        Test the input for select option
        """
        with patch('builtins.input', return_value = 'ENTER'):
            self.assertEqual(self.pmvcs_view.input_options(), 'ENTER')

    def test_input_generic(self):
        """
        Test the input for generic input with passed legend
        """
        with patch('builtins.input', return_value = 'ENTER'):
            self.assertEqual(self.pmvcs_view.input_generic('Option A'), 'ENTER')

    def _test_input_language_options(self) -> str:
        """
        Returns supported languages for selection input
        """
        return_string = ''
        lang_dict = {'en': 'English', 'es': 'Español'}

        for key, value in enumerate(lang_dict, start=1):
            return_string += f'\n({key}) {lang_dict[value]}'

        return f'{return_string}\n'

    def test_input_language(self):
        """
        Test the input for select language
        """
        with patch('builtins.input', return_value = 'ENTER'):
            self.assertEqual(self.pmvcs_view.input_language(self._test_input_language_options()), 'ENTER')

    def test_test(self):
        """
        Test the Testing function
        """
        result = self.pmvcs_view.test()        
        original = 'Hello from PMVCS Base View!'

        self.assertEqual(original, result)


if __name__ == '__main__':
    unittest.main()
