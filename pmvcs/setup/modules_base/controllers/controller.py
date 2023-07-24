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
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        print('>>> Insert your code here!')

        self.pmvcs_view.input_pause()
        self.pmvcs_view.clean_screen()
        # >>> to here!

        return False
