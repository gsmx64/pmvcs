""" Test file for CodeBreaker """
import unittest
import configparser

from pmvcs.core.models.configuration import Configuration
from pmvcs.core.models.language import Language
from app.models.codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """ Class for unittest CodeBreaker """

    def setUp(self):
        """
        Instance CodeBreaker()
        """
        self.cfg = Configuration()
        self.cfg._file_path = 'tests/config_tests.ini'

        self.kwargs = {'pmvcs_cfg': self.cfg}
        self.lang = Language(self.kwargs)
        self.lang.tag = 'en'
        self.lang._file_path = 'app/languages/en.ini'
        self.kwargs['pmvcs_lang'] = self.lang
        self.kwargs['pmvcs_about'] = None
        self.kwargs['pmvcs_view'] = None
        self.kwargs['pmvcs_helper'] = None

    def test_codebreaker_win(self):
        """
        Win Result Test
        """
        codebreaker = CodeBreaker('1058', 'Guest', False, **self.kwargs)
        self.assertTrue(codebreaker)

    def test_codebreaker_test_chars1(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker('1078', 'Guest', False, **self.kwargs)
        self.assertEqual('XX X', codebreaker.challenge())

    def test_codebreaker_test_chars2(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker('1059', 'Guest', False, **self.kwargs)
        self.assertEqual('XXX ', codebreaker.challenge())

    def test_codebreaker_test_chars3(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker('9782', 'Guest', False, **self.kwargs)
        self.assertEqual('  _ ', codebreaker.challenge())

    def test_codebreaker_test_chars4(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker('9504', 'Guest', False, **self.kwargs)
        self.assertEqual(' __ ', codebreaker.challenge())

    def test_codebreaker_fail_chars(self):
        """
        No repeated digits test
        """
        codebreaker = CodeBreaker('9999', 'Guest', False, **self.kwargs)
        test = None
        self.assertEqual(test, codebreaker.challenge())


if __name__ == '__main__':
    unittest.main()
