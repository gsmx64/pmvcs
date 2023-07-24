""" Base Controller file for PMVCS APP """
from abc import ABC, abstractmethod


class AbstractBaseController(ABC):
    """ Class for Base Controller """

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        pass
