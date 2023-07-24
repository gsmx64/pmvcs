""" Sample View file for Python MVC Shell Framework Package """
from pmvcs.core.interfaces.sample import AbstractSampleView
from pmvcs.core.models.language import Language


class SampleView(AbstractSampleView):
    """ Class for PMVCS Sample View """

    def __init__(self, **kwargs: dict) -> None:
        """
        Init PMVCS Sample View requirements
        """
        self.cfg = kwargs['pmvcs_cfg']
        self.lang = kwargs['pmvcs_lang']
        self.pmvcs_view = kwargs['pmvcs_view']

        self.sample = Language(self.cfg)
        self.sample.tag = f'{self.lang.tag}.sample'
        self.sample.update

    def tips_sample(self) -> str:
        """
        Returns tips sample view
        """
        print(f'[>] {self.sample.get("SAMPLE_TIPS")}')
        print(f'  {self.sample.get("SAMPLE_RUN_NO_MENU_1")}\n', end='')
        print(f'  {self.sample.get("SAMPLE_RUN_NO_MENU_2")}\n', end='')
        print(f'  {self.sample.get("SAMPLE_RUN_NO_MENU_3")}\n', end='')
        print(f'  {self.sample.get("SAMPLE_RUN_NO_MENU_4")}\n')

        print(f'[>] {self.sample.get("SAMPLE_HELPERS_TITLE")} ')
        print(f'  {self.sample.get("SAMPLE_CODE")} >>> filters = self.pmvcs_helper.load_helper(\'filters\', True)')
        print(f'  {self.sample.get("SAMPLE_CODE")} >>> filters.data_type(str(\'5\'))   -> ({self.sample.get("SAMPLE_INT_VALUE")})')

    def configuration_sample(self) -> str:
        """
        Returns configuration sample view
        """
        print(f'[>] {self.sample.get("SAMPLE_CONFIG_TITLE")}')
        self.test_view('self.cfg.get("EXAMPLE_CONSTANT", "OPTIONS")')
        self.test_view('self.cfg.get("DEFAULT_TITLE", "DEFAULT")')
        self.test_view('self.cfg.get("EXAMPLE_INT", "OPTIONS", "int")')
        self.test_view('self.cfg.get("EXAMPLE_FLOAT", "OPTIONS", "float")')
        self.test_view('self.cfg.get("EXAMPLE_BOOLEAN", "OPTIONS", "boolean")')
        self.test_view('self.cfg.get("EXAMPLE_LIST", "OPTIONS", "list")')
        self.test_view('self.cfg.get("EXAMPLE_DICT", "OPTIONS", "dict")')

    def language_sample(self) -> str:
        """
        Returns language sample view
        """
        print(f'[>] {self.sample.sprintf("SAMPLE_TITLE", self.lang.tag)}')
        self.test_view('self.lang.tag', f'   -> ({self.sample.get("SAMPLE_LTAG")})')
        self.test_view('self.lang.get("LANG_EXAMPLE_STRING")')

        print(f'  {self.sample.get("SAMPLE_SEEN")} "{self.lang.get("LANG_EXAMPLE_SPRINTF")}"')
        self.test_view('self.lang.sprintf("LANG_EXAMPLE_SPRINTF", "3")')

        print(f'  {self.sample.get("SAMPLE_SEEN")} "{self.lang.get("LANG_EXAMPLE_SPRINTF2")}"')
        self.test_view('self.lang.sprintf("LANG_EXAMPLE_SPRINTF2", "1", "2", "3")')

        value = 'dictionary'
        self.test_view('self.lang.translate(value)', '   -> value = \'dictionary\'', value)

    def pmvcs_view_sample(self) -> str:
        """
        Returns pmvcs_view sample view
        """
        print(f'[>] {self.sample.get("SAMPLE_PMVCS_VIEW_TITLE")}')
        self.test_view('self.pmvcs_view.get_intro()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_BANNER")})',
                       evals=False)
        self.test_view('self.pmvcs_view.get_exit()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_EXIT")})',
                       evals=False)
        self.test_view('self.pmvcs_view.line_brake()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_LB1")})',
                       evals=False)
        self.test_view('self.pmvcs_view.line_brake(True)',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_LB2")})',
                       evals=False)
        self.test_view('self.pmvcs_view.input_start()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_START")})',
                       evals=False)
        self.test_view('self.pmvcs_view.input_pause()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_CONT")})',
                       evals=False)
        self.test_view('self.pmvcs_view.input_options()',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_OPTION")})',
                       evals=False)
        self.test_view('self.pmvcs_view.input_generic(text)',
                       f'   -> ({self.sample.get("SAMPLE_PMVCS_VIEW_GENERIC")})',
                       evals=False)

    def test_view(self, test: str, note='', value='', evals=True) -> str:
        """
        Returns code test view
        """
        if evals:
            if evals and note and value:
                eval_code = eval(test, {}, {'self': self, 'value': value})
            eval_code = eval(test)
            returns = f'  {self.sample.get("SAMPLE_CODE")} >>> {str(test)}{note}\n'
            returns += f'  {self.sample.get("SAMPLE_RETURNS")} {eval_code}\n'
            returns += f'  {self.sample.get("SAMPLE_VALUE_TYPE")} {type(eval_code)}\n'
            print(returns)
        else:
            returns = f'  {self.sample.get("SAMPLE_CODE")} '
            returns += f'>>> {str(test)}{note}\n'
            print(returns)
