""" Ramdom Data Model for Binary Search Algorithms"""
import random
import numpy as np

from app.decorators.decorators_random import remove_duplicates_decorator
from app.decorators.decorators_random import sorted_decorator


class RamdomDataModel():
    """ Returns a orderer ramdom list from 3 optional modes. """
    _mode = 'sample'
    _amounth = 50
    _max = 200

    def __init__(self) -> object:
        """
        Init Ramdom Data Model requirements
        """
        self.random_list = []
        random.shuffle(self.random_list)

    @property
    def mode(self) -> str:
        """
        Returns getter of mode for data builder (str)
        """
        return self._mode

    @mode.setter
    def mode(self, value: str) -> str:
        """
        Returns setter for mode to select data builder
        """
        self._mode = value

    @property
    def amounth(self) -> int:
        """
        Returns getter of amounth for data builder
        """
        return self._amounth

    @amounth.setter
    def amounth(self, value: int) -> int:
        """
        Returns setter for amounth to set data builder
        """
        self._amounth = value

    @property
    def max(self) -> int:
        """
        Returns getter of max for data builder
        """
        return self._max

    @max.setter
    def max(self, value: int) -> int:
        """
        Returns setter for mode to set data builder
        """
        self._max = value

    @property
    def get_data(self) -> list:
        """
        Return data by setted mode, returns a list()
        """
        if self._mode == 'sample':
            return self._get_random_sample()
        if self._mode == 'randint':
            return self._get_random_randint()
        if self._mode == 'numpy':
            return self._get_random_numpy()

    @sorted_decorator
    def _get_random_sample(self) -> list:
        """
        Build data numbers with random sample mode, returns a list()
        """
        return random.sample(range(0, self._max), self._amounth)

    @sorted_decorator
    @remove_duplicates_decorator
    def _get_random_randint(self) -> list:
        """
        Build data numbers with random randint mode, returns a list() (list)
        """
        randint_list = list(random.randint(1, self._max) for _ in range(0, self._amounth+30))
        truncated_list = slice(self._amounth)
        return randint_list[truncated_list]

    @sorted_decorator
    @remove_duplicates_decorator
    def _get_random_numpy(self) -> list:
        """
        Build data numbers with numpy`s random randint mode,
        returns a list()
        """
        return np.random.randint(0, high=self._max, size=self._amounth,
                                 dtype=int).tolist()
