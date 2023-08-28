""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.sample import AbstractSampleView

class TestAbstractSampleView(unittest.TestCase):
    """ Class for unittest Test Abstract Sample View """
      
    def test_tips_sample(self):
        """
        Test the abstract class AbstractSampleView
        """
        with self.assertRaises(TypeError):
            abs = AbstractSampleView()
            abs.tips_sample.return_value = 5

    def test_configuration_sample(self):
        """
        Test the abstract class AbstractSampleView
        """
        with self.assertRaises(TypeError):
            abs = AbstractSampleView()
            abs.configuration_sample.return_value = 5

    def test_language_sample(self):
        """
        Test the abstract class AbstractSampleView
        """
        with self.assertRaises(TypeError):
            abs = AbstractSampleView()
            abs.language_sample.return_value = 5

    def test_pmvcs_view_sample(self):
        """
        Test the abstract class AbstractSampleView
        """
        with self.assertRaises(TypeError):
            abs = AbstractSampleView()
            abs.pmvcs_view_sample.return_value = 5

    def test_test_view(self):
        """
        Test the abstract class AbstractSampleView
        """
        with self.assertRaises(TypeError):
            abs = AbstractSampleView()
            abs.test_view.return_value = 5


if __name__ == '__main__':
    unittest.main()
