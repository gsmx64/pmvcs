""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.router import Router
from pmvcs.core.models.language import Language


class TestParser(unittest.TestCase):
    """ Class for unittest Test Language """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']

        self.lang = Language(self.cfg)

    def test_lang(self):
        """
        Test the return of ConfigParser data
        """
        # ConfigParser uses section first, then constant key
        resolve = self.lang.lang.get('LANG', 'LANG_EXIT_PROGRAM')

        self.assertEqual('The program ended', resolve)

    def test_tag(self):
        """
        Test the tag getter
        """
        resolve = self.lang.tag

        self.assertEqual('en', resolve)

    def test_tag_setter(self):
        """
        Test the tag setter
        """
        self.lang.tag = 'es'
        resolve = self.lang.tag

        self.assertEqual('es', resolve)

    def test_set_file_path(self):
        """
        Test the set file path
        """
        resolve = self.lang._set_file_path

        self.assertEqual('app/languages/en.ini', resolve)

    def test_update(self):
        """
        Test the update file path
        """
        resolve = None

        self.assertEqual(None, resolve)

    def test_sprintf(self):
        """
        Test the return of data by get method
        """
        resolve = self.lang.sprintf('ERROR_IMPORT_UNKNOWN_FORMAT', 'Format Test')

        self.assertEqual('[>] ERROR: Unknown format "Format Test"', resolve)

    def test_translate(self):
        """
        Test the return of string by get method
        """
        string = 'dictionary'
        resolve = self.lang.translate(string)

        self.assertEqual('Dictionary', resolve)


if __name__ == '__main__':
    unittest.main()
