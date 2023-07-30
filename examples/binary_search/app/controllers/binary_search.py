""" Binary Search Controller file for PMVCS APP """
from app.controllers.base_controller import BaseController
from app.models.binary_search import BinarySearchModel
from app.models.random_data import RamdomDataModel
from app.views.binary_search import BinarySearchView


class BinarySearchController(BaseController):
    """ Class for Binary Search Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init Binary Search Controller requirements
        """
        super().__init__(**kwargs)

        self.model = BinarySearchModel(**kwargs)
        self.view = BinarySearchView(**kwargs)

        self.random_data = RamdomDataModel()
        self.random_data.mode = self.cfg.get("RANDOMDATA_MODE", "OPTIONS")
        self.random_data.amounth = self.cfg.get("RANDOMDATA_AMOUNTH", "OPTIONS", "int")
        self.random_data.max = self.cfg.get("RANDOMDATA_MAX", "OPTIONS", "int")
        self.data = self.random_data.get_data

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        check = ''
        while check not in ['q', 'Q']:
            self.pmvcs_view.clean_screen()
            print(self.pmvcs_view.get_intro())

            print(self.view.get_data_output(
                    self.cfg.get("RANDOMDATA_MODE", "OPTIONS"),
                    self.data))
            self.pmvcs_view.line_brake(True)

            search_value = self.view.get_input_search()
            if not search_value.isnumeric():
                continue

            print(self.view.get_result_output(
                self.model.get(self.data, search_value)))
            self.pmvcs_view.line_brake(True)

            check = self.view.input_pause_repeat()

        self.pmvcs_view.clean_screen()

        return False
