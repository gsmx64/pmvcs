""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.router import Router
from pmvcs.core.models.menus import Menus


class TestMenus(unittest.TestCase):
    """ Class for unittest Test Menus """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']

        self.menus = Menus(self.cfg)

    def test_tag(self):
        """
        Test the tag getter
        """
        resolve = self.menus.tag

        self.assertEqual('en', resolve)

    def test_tag_setter(self):
        """
        Test the tag setter
        """
        self.menus.tag = 'es'
        resolve = self.menus.tag

        self.assertEqual('es', resolve)

    def test_set_file_path(self):
        """
        Test the set file path
        """
        resolve = self.menus._set_file_path

        self.assertEqual('app/languages/en.menus.ini', resolve)

    def test_update(self):
        """
        Test the update file path
        """
        resolve = None

        self.assertEqual(None, resolve)


if __name__ == '__main__':
    unittest.main()
