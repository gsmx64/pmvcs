""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.about import About


class TestPmvcs(unittest.TestCase):
    """ Class for unittest Test Pmvcs """

    def setUp(self):
        """
        Instance the app()
        """
        self.cfg = Configuration()

        self.pmvcs_about = About(self.cfg)
        self.pmvcs_about.tag = 'en'

    def test_credits(self):
        """
        Get from Info the Test App title
        """
        resolve = self.pmvcs_about.get('title')
        title = 'Example App'

        self.assertEqual(title, resolve)


if __name__ == '__main__':
    unittest.main()
