""" Example One Controller file for PMVCS APP """
from app.controllers.base_controller import BaseController
from app.models.example_one import ExampleOneModel
from app.views.example_one import ExampleOneView


class ExampleOneController(BaseController):
    """ Class for Example One Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init ExampleOne Controller requirements
        """
        super().__init__(**kwargs)

        self.model = ExampleOneModel(**kwargs)
        self.view = ExampleOneView(**kwargs)

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        # >>> Inserts your code from here...
        super().execute()

        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        filters = self.pmvcs_helper.load_helper('filters', True)
        value = str('5')
        print("filters = self.pmvcs_helper.load_helper('filters', True)")
        print(f"filters.data_type(str('5')): {filters.data_type(value)}")
        print(f"filters type(): {type(filters.data_type(value))}")

        self.pmvcs_view.input_pause()
        # >>> to here!

        return False
