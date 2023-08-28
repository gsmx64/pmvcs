""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.models.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    """ Class for unittest Test Configuration """

    def setUp(self):
        """
        Instance the unittest
        """
        self.cfg = Configuration()

    def test_cfg(self):
        """
        Test the return of ConfigParser data
        """
        # ConfigParser uses section first, then constant key
        resolve = self.cfg.cfg.get('DEFAULT', 'DEFAULT_TITLE')

        self.assertEqual('Example App', resolve)

    def test_set_file_path(self):
        """
        Test the set file path
        """
        resolve = self.cfg._set_file_path

        self.assertEqual('config.ini', resolve)


if __name__ == '__main__':
    unittest.main()
