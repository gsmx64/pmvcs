""" Test file for Recital """
import unittest

from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.about import About


class TestRecital(unittest.TestCase):
    """
    Class for unittest Recital
    """

    def setUp(self):
        """
        Instance the app()
        """
        self.cfg = Configuration()

        self.pmvcs_about = About(self.cfg)
        self.pmvcs_about.tag = 'en'

    def test_credits(self):
        """
        Get from About the App title
        """
        resolve = self.pmvcs_about.get('title')
        title = 'Recital'

        self.assertEqual(title, resolve)


if __name__ == '__main__':
    unittest.main()
