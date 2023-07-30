""" Recital Controller file for PMVCS APP """
from app.controllers.base_controller import BaseController
from app.models.recital import RecitalModel
from app.models.queues import QueueData
from app.views.recital import RecitalView
from app.views.stage import StageView


class RecitalController(BaseController):
    """ Class for Recital Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init Recital Controller requirements
        """
        super().__init__(**kwargs)

        self.model = RecitalModel(**kwargs)
        self.view = RecitalView(**kwargs)

        self.pit_list = []
        self.queue_list = []
        self.queues = QueueData(self.pit_list, self.queue_list, **kwargs)
        self.view_stage = StageView(self.queues, **kwargs)

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        # >>> Inserts your code from here...
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        check = '*'
        while check.lower() != 'q':
            self.pmvcs_view.clean_screen()
            print(self.view_stage.get_stage)

            if check.lower() != 'q':
                check = self.pmvcs_view.input_generic(self.lang.get("LANG_INPUT_SELECT_STAGE_OPTIONS"))

            if check == '1':
                if self.queues.list_full(self.queue_list, self.lang.get("LANG_INPUT_FREE_QUEUE")):  # noqa: E501  # pylint: disable=C0301

                    self.pmvcs_view.input_generic(
                        self.lang.get("LANG_INPUT_STAGE_COMPLETE"))
                else:
                    queue_user = self.pmvcs_view.input_generic(
                        self.lang.get("LANG_INPUT_STAGE_QUEUE_INSERT"))

                    self.queues.list_add(self.queue_list,
                                         self.lang.get("LANG_INPUT_FREE_QUEUE"),  # noqa: E501  # pylint: disable=C0301
                                         queue_user)

            if check == '2':
                if self.queues.list_empty(self.queue_list,
                                          self.lang.get("LANG_INPUT_FREE_QUEUE")):  # noqa: E501  # pylint: disable=C0301

                    self.pmvcs_view.input_generic(
                        self.lang.get("LANG_INPUT_STAGE_QUEUE_EMPTY"))
                else:
                    pit_top = self.queues.list_top(
                        self.queue_list,
                        self.lang.get("LANG_INPUT_FREE_QUEUE"))

                    pit_check = self.pmvcs_view.input_generic(
                        self.lang.sprintf("LANG_INPUT_STAGE_QUEUE_TO_PIL", pit_top))

                    if pit_check.lower() == 'y':
                        self.queues.queue_to_pil(
                            self.queue_list,
                            self.lang.get("LANG_INPUT_FREE_QUEUE"),
                            self.pit_list,
                            self.lang.get("LANG_INPUT_FREE_SEAT"))
                        print(
                            self.lang.sprintf("LANG_INPUT_STAGE_PIL_IN", pit_top))

            if check == '3':
                while True:
                    try:
                        next(self.queues.pit_remove_generator(self.pit_list))
                    except StopIteration:
                        self.pmvcs_view.input_generic(
                            self.lang.get("LANG_INPUT_STAGE_PIL_EXIT"))
                        break
                self.pmvcs_view.clean_screen()
                break
                #self._go_to_menu(self)  # pylint: disable=E1121

            if check.lower() == 'q':
                self.pmvcs_view.clean_screen()
                break

        #self.pmvcs_view.clean_screen()

        return False
