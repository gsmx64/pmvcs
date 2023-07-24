""" Abstract Sample View file for Python MVC Shell Framework Package """
from abc import ABC, abstractmethod


class AbstractSampleView(ABC):
    """ Class for PMVCS Abstract Sample View """

    @abstractmethod
    def tips_sample(self) -> str:
        """
        Returns tips sample view
        """
        pass

    @abstractmethod
    def configuration_sample(self) -> str:
        """
        Returns configuration sample view
        """
        pass

    @abstractmethod
    def language_sample(self) -> str:
        """
        Returns language sample view
        """
        pass

    @abstractmethod
    def pmvcs_view_sample(self) -> str:
        """
        Returns pmvcs_view sample view
        """
        pass

    @abstractmethod
    def test_view(self, test: str, note='', value='', evals=True) -> str:
        """
        Returns code test view
        """
        pass
