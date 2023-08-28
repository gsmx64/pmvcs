""" Test file for Python MVC Shell Framework Package """
import unittest

from pmvcs.core.interfaces.base_model import AbstractBaseModel

class TestAbstractBaseModel(unittest.TestCase):
    """ Class for unittest Test Abstract Base Model """
      
    def test_section(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.section.return_value

    def test_section_setter(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.section.return_value = 5

    def test_path_exists(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.path_exists.return_value = 5
            
    def test_file_path(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.file_path.return_value
            
    def test_file_path_setter(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.file_path.return_value = 5
            
    def test_set_file_path(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs._set_file_path.return_value = 5
            
    def test_update(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.update.return_value = 5
            
    def test_data(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.data.return_value = 5
            
    def test_get(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.get.return_value = 5
            
    def test_to_dict(self):
        """
        Test the abstract class AbstractBaseModel
        """
        with self.assertRaises(TypeError):
            abs = AbstractBaseModel()
            abs.to_dict.return_value = {'a': 5}


if __name__ == '__main__':
    unittest.main()
