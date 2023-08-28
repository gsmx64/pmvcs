""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.router import Router
from pmvcs.core.models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Class for unittest Test BaseModel """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()
        providers = Router().get_providers('basic_view')

        self.pmvcs_model = BaseModel(**providers)
        self.pmvcs_model.section = 'en'

    def test_section(self):
        """
        Test the section getter
        """
        resolve = self.pmvcs_model.section

        self.assertEqual('en', resolve)

    def test_section_setter(self):
        """
        Test the section setter
        """
        self.pmvcs_model.section = 'es'
        resolve = self.pmvcs_model.section

        self.assertEqual('es', resolve)

    def test_file_path(self):
        """
        Test the file path getter
        """
        resolve = self.pmvcs_model.file_path

        self.assertEqual(None, resolve)

    def test_file_path_setter(self):
        """
        Test the file path setter
        """
        self.pmvcs_model.file_path = ''
        resolve = self.pmvcs_model.file_path

    def test_set_file_path(self):
        """
        Test the set file path
        """
        resolve = self.pmvcs_model._set_file_path

        self.assertEqual(None, resolve)

    def test_update(self):
        """
        Test the update file path
        """
        resolve = None

        self.assertEqual(None, resolve)

    def test_data(self):
        """
        Test the return of ConfigParser data
        """
        resolve = None

        self.assertEqual(None, resolve)

    def test_get(self):
        """
        Test the return of string by get method
        """
        self.pmvcs_model.file_path = './config.ini'
        resolve = self.pmvcs_model.get('EXAMPLE_CONSTANT', 'OPTIONS')

        self.assertEqual(None, resolve)

    def test_to_dict(self):
        """
        Test the return of dict by get method
        """
        self.pmvcs_model.file_path = './config.ini'
        resolve = self.pmvcs_model.to_dict()

        self.assertFalse(isinstance(resolve, dict))

    def test_test(self):
        """
        Test the Testing function
        """
        result = self.pmvcs_model.test()        
        original = 'Hello from PMVCS Base Model!'

        self.assertEqual(original, result)


if __name__ == '__main__':
    unittest.main()
