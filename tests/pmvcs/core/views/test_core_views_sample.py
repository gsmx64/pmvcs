""" Test file for Python MVC Shell Framework Package """
import unittest
import sys
import io

from pmvcs.core.router import Router
from pmvcs.core.views.sample import SampleView
from pmvcs.core.models.language import Language


class TestSampleView(unittest.TestCase):
    """ Class for unittest Test SampleView """

    def setUp(self):
        """
        Instance the unittest
        """
        providers = Router().get_providers('basic_view')
        self.cfg = providers['pmvcs_cfg']
        self.lang = providers['pmvcs_lang']
        self.pmvcs_view = providers['pmvcs_view']
        self.sample_view = SampleView(**providers)

    def test_tips_sample(self) -> str:
        """
        Test the return of tips sample view
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sample_view.tips_sample()
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """[>] Tips:
  For run a module without menu, just edit app.py and change the
  line app.create_app('test'), where test is the name of module
  inside app/controllers folder (see app/controllers/test.py file
  for class structure).

[>] You can load PMVCS Helpers or custom helpers, check the documentation. 
  Code: >>> filters = self.pmvcs_helper.load_helper('filters', True)
  Code: >>> filters.data_type(str('5'))   -> (returns int value)
"""

        self.assertEqual(original, result)

    def test_configuration_sample(self) -> str:
        """
        Test the return of configuration sample view
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sample_view.configuration_sample()
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """[>] Get configuration constants from config.ini:
  Code: >>> self.cfg.get("EXAMPLE_CONSTANT", "OPTIONS")
  Returns: This is an example value from config file
  Value Type: <class 'str'>

  Code: >>> self.cfg.get("DEFAULT_TITLE", "DEFAULT")
  Returns: Example App
  Value Type: <class 'str'>

  Code: >>> self.cfg.get("EXAMPLE_INT", "OPTIONS", "int")
  Returns: 8
  Value Type: <class 'int'>

  Code: >>> self.cfg.get("EXAMPLE_FLOAT", "OPTIONS", "float")
  Returns: 1.57
  Value Type: <class 'float'>

  Code: >>> self.cfg.get("EXAMPLE_BOOLEAN", "OPTIONS", "boolean")
  Returns: True
  Value Type: <class 'bool'>

  Code: >>> self.cfg.get("EXAMPLE_LIST", "OPTIONS", "list")
  Returns: ['1', '2']
  Value Type: <class 'list'>

  Code: >>> self.cfg.get("EXAMPLE_DICT", "OPTIONS", "dict")
  Returns: {'value_one': '1', 'value_two': '2'}
  Value Type: <class 'dict'>

"""

        self.assertEqual(original, result)

    def test_language_sample(self) -> str:
        """
        Test the return of language sample view
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sample_view.language_sample()
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """[>] Get language constants from languages/en.ini:
  Code: >>> self.lang.tag   -> (current language tag)
  Returns: en
  Value Type: <class 'str'>

  Code: >>> self.lang.get("LANG_EXAMPLE_STRING")
  Returns: This is an example string
  Value Type: <class 'str'>

  In the language file you will see: "String-Print-Format value here: "{}""
  Code: >>> self.lang.sprintf("LANG_EXAMPLE_SPRINTF", "3")
  Returns: String-Print-Format value here: "3"
  Value Type: <class 'str'>

  In the language file you will see: "One: "{}". Two: "{}". Three: "{}"."
  Code: >>> self.lang.sprintf("LANG_EXAMPLE_SPRINTF2", "1", "2", "3")
  Returns: One: "1". Two: "2". Three: "3".
  Value Type: <class 'str'>

  Code: >>> self.lang.translate(value)   -> value = 'dictionary'
  Returns: Dictionary
  Value Type: <class 'str'>

"""

        self.assertEqual(original, result)

    def test_pmvcs_view_sample(self) -> str:
        """
        Test the return of pmvcs_view sample view
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sample_view.pmvcs_view_sample()
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """[>] Using PMVCS View functions
  Code: >>> self.pmvcs_view.get_intro()   -> (shows the banner)

  Code: >>> self.pmvcs_view.get_exit()   -> (shows the exit)

  Code: >>> self.pmvcs_view.line_brake()   -> (inserts a line break without print())

  Code: >>> self.pmvcs_view.line_brake(True)   -> (insert a line break with print())

  Code: >>> self.pmvcs_view.input_start()   -> (inserts a pause to press ENTER to start)

  Code: >>> self.pmvcs_view.input_pause()   -> (inserts a pause to press ENTER to continue)

  Code: >>> self.pmvcs_view.input_options()   -> (inserts a select an option input())

  Code: >>> self.pmvcs_view.input_generic(text)   -> (inserts a select an input())

"""

        self.assertEqual(original, result)

    def test_test_view_eval_false(self) -> str:
        """
        Test the return of pmvcs_view sample view with evals false
        """
        self.sample = Language(self.cfg)
        self.sample.tag = f'{self.lang.tag}.sample'
        self.sample.update

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.sample_view.test_view('self.pmvcs_view.get_intro()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_BANNER")})',
                       evals=False)
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """  Code: >>> self.pmvcs_view.get_intro()   -> (shows the banner)

"""

        self.assertEqual(original, result)

    def test_test_view_eval_true(self) -> str:
        """
        Test the return of pmvcs_view sample view with evals true
        """
        self.sample = Language(self.cfg)
        self.sample.tag = f'{self.lang.tag}.sample'
        self.sample.update
        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        value = 'dictionary'
        self.sample_view.test_view('self.lang.translate(value)', '   -> value = \'dictionary\'', value, evals=True)
        result = capturedOutput.getvalue()
        sys.stdout = sys.__stdout__

        original = """  Code: >>> self.lang.translate(value)   -> value = 'dictionary'
  Returns: Dictionary
  Value Type: <class 'str'>

"""

        self.assertEqual(original, result)
        

if __name__ == '__main__':
    unittest.main()
