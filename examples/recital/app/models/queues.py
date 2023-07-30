""" Queue Data Model for Recital """
from app.models.base_model import BaseModel


class QueueData(BaseModel):
    """
    Class for Ramdom Data Model
    Returns a orderer ramdom list from 3 optional modes.
    """
    _pit_list = []
    _queue_list = []
    _capacity = 10

    def __init__(self, pit_list: list, queue_list: list,
                 **kwargs) -> None:
        """
        Init Queue Data Model requirements
        """
        super().__init__(**kwargs)

        self._capacity = self.cfg.get("STAGE_CAPACITY", "OPTIONS", "int")

        self._pit_list = self.list_complete(
            pit_list, self.lang.get("LANG_INPUT_FREE_SEAT"),
            self._capacity)

        self._queue_list = self.list_complete(
            queue_list, self.lang.get("LANG_INPUT_FREE_QUEUE"),
            self._capacity)

    @property
    def pit_list(self) -> list:
        """
        Returns getter of pit_list for data builder
        """
        return self._pit_list

    @pit_list.setter
    def pit_list(self, value: str) -> list:
        """
        Returns setter for pit_list to select data builder
        """
        self._pit_list = value

    @property
    def queue_list(self) -> list:
        """
        Returns getter of pit_list for data builder
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, value: str) -> list:
        """
        Returns setter for queue_list to select data builder
        """
        self._queue_list = value

    def list_empty(self, current_list: list, default_empty: str) -> bool:
        """
        Returns True is the list is empty (removes the default
        free queues or seats)
        """
        temp_list = current_list.copy()
        self.list_iterate(temp_list, default_empty, mode='drop')
        return len(temp_list) == 0

    def list_full(self, current_list: list, default_empty: str) -> bool:
        """
        Returns True is the list is full (removes the default free
        queues or seats)
        """
        temp_list = current_list.copy()
        self.list_iterate(temp_list, default_empty, mode='drop')
        return len(temp_list) == self._capacity

    def list_top(self, current_list: list, default_empty: str) -> str:
        """
        Returns the top value of the list
        """
        if self.list_empty(current_list, default_empty):
            return None

        return current_list[0]

    def list_add(self, current_list: list, default_empty: str, element: str) -> list:
        """
        Add a value back to the list (reorders the default free queues or seats)
        """
        if self.list_full(current_list, default_empty):
            return None

        current_list.pop(-1)
        current_list.append(element)
        return self.list_iterate(current_list, default_empty, 'reorder')

    def list_complete(self, current_list: list, default_empty: str, capacity: int) -> list:
        """
        Returns a complete list with default free
        queues or seats, limited by capacity
        """
        while len(current_list) < capacity:
            current_list.append(default_empty)
        return current_list

    def list_iterate(self, current_list: list, default_empty: str, mode='reorder'):
        """
        Returns a list with orderer default free queues or seats,
        or a clean list without default free queues or seats
        """
        counter = 0
        end = len(current_list) - 1

        while counter <= end:
            if current_list[counter] == default_empty:
                if mode == 'reorder':
                    current_list.append(current_list.pop(counter))

                if mode == 'drop':
                    current_list.pop(counter)
                end -= 1
            else:
                counter += 1
        return current_list

    def queue_to_pil(self, queue_list: list, default_empty_queue: str,
                     pil_list: list, default_empty_pil: str) -> list:
        """
        Moves the first index of the list, to another list in first
        index, and (reorders the default free queues or seats)
        """
        if self.list_empty(queue_list, default_empty_queue):
            return None

        element_out = queue_list.pop(0)
        self.list_complete(queue_list, default_empty_queue, self._capacity)
        pil_list.pop(-1)
        pil_list.append(element_out)
        return self.list_iterate(pil_list, default_empty_pil, 'reorder')

    def pit_remove_generator(self, pit_list: list) -> list:
        """
        Returns a generator where the elements of a list gets out,
        so finally we get an empty list (reorders the default free
        seats)
        """
        for pit in pit_list:
            if pit != self.lang.get("LANG_INPUT_FREE_SEAT"):
                pit_list.remove(pit)
                pit_list.insert(0, self.lang.get("LANG_INPUT_FREE_SEAT"))
                yield input(
                    self.lang.sprintf("LANG_INPUT_STAGE_PIL_OUT", pit))
