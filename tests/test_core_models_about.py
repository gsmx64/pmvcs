""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.router import Router
from pmvcs.core.models.about import About


class TestAbout(unittest.TestCase):
    """ Class for unittest Test About """

    def setUp(self):
        """
        Instance the unittest
        """
        self.router = Router()
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']

        self.about = About(self.cfg)

    def test_about(self):
        """
        Test the return of ConfigParser data
        """
        # ConfigParser uses section first, then constant key
        resolve = self.about.data.get('ABOUT', 'framework')

        self.assertEqual('Python MVC Shell Framework Package', resolve)

    def test_tag(self):
        """
        Test the tag getter
        """
        resolve = self.about.tag

        self.assertEqual('en', resolve)

    def test_tag_setter(self):
        """
        Test the tag setter
        """
        self.about.tag = 'es'
        resolve = self.about.tag

        self.assertEqual('es', resolve)

    def test_set_file_path(self):
        """
        Test the set file path
        """
        resolve = self.about._set_file_path

        self.assertEqual('app/languages/en.about.ini', resolve)

    def test_update(self):
        """
        Test the update file path
        """
        resolve = None

        self.assertEqual(None, resolve)


if __name__ == '__main__':
    unittest.main()
