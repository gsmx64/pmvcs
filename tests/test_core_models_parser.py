""" Test file for Python MVC Shell Framework Package """
import unittest, os

from pmvcs.core.router import Router
from pmvcs.core.models.parser import Parser


class TestParser(unittest.TestCase):
    """ Class for unittest Test Parser """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']
        self.lang = providers['pmvcs_lang']

        self.parser = Parser()

    def test_path_exists(self):
        """
        Test the path exists validation
        """
        path = os.path.join(os.path.dirname( __file__ ), '../..')
        resolve = self.parser.path_exists(path)

        self.assertTrue(resolve)

    def test_file_path(self):
        """
        Test the file path getter
        """
        parser = Parser()
        resolve = self.parser.file_path

        self.assertEqual('', resolve)

    def test_file_path_setter(self):
        """
        Test the file path setter
        """
        parser = Parser()
        parser.file_path = ''
        resolve = self.parser.file_path

        self.assertEqual('', resolve)

    def test_set_file_path(self):
        """
        Test the set file path
        """
        parser = Parser()
        resolve = self.parser._set_file_path

        self.assertEqual(None, resolve)

    def test_update(self):
        """
        Test the update file path
        """
        parser = Parser()
        resolve = self.parser.update

        self.assertEqual(None, resolve)

    def test_data(self):
        """
        Test the return of ConfigParser data
        """
        parser = Parser()
        parser.file_path = './config.ini'
        
        # ConfigParser uses section first, then constant key
        resolve = parser.data.get('LANGUAGE', 'DEFAULT_LANGUAGE')

        self.assertEqual('en', resolve)

    def test_get_string(self):
        """
        Test the return of data by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('DEFAULT_LANGUAGE', 'LANGUAGE')

        self.assertEqual('en', resolve)

    def test_get(self):
        """
        Test the return of string by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_CONSTANT', 'OPTIONS')

        self.assertEqual('This is an example value from config file', resolve)

    def test_get_int(self):
        """
        Test the return of integer by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_INT', 'OPTIONS', 'int')

        self.assertEqual(8, resolve)

    def test_get_float(self):
        """
        Test the return of float by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_FLOAT', 'OPTIONS', 'float')

        self.assertEqual(1.57, resolve)

    def test_get_boolean(self):
        """
        Test the return of boolean by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_BOOLEAN', 'OPTIONS', 'boolean')

        self.assertEqual(True, resolve)

    def test_get_list(self):
        """
        Test the return of list by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_LIST', 'OPTIONS', 'list')
        temp_list = ['1', '2']

        self.assertEqual(temp_list, resolve)

    def test_get_dict(self):
        """
        Test the return of dict by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.get('EXAMPLE_DICT', 'OPTIONS', 'dict')
        temp_dict = {'value_one': '1', 'value_two': '2'}

        self.assertEqual(temp_dict, resolve)

    def test_to_dict(self):
        """
        Test the return of dict by get method
        """
        parser = Parser()
        parser.file_path = './config.ini'
        resolve = parser.to_dict()

        self.assertTrue(isinstance(resolve, dict))


if __name__ == '__main__':
    unittest.main()
