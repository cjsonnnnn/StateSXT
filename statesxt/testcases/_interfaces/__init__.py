from base.base_driver import BaseDriver
from abc import ABC


class StateInterface(ABC):
    """
    An abstract class for all the state interface classes
    """

    def __init__(self, base: BaseDriver) -> None:
        self.__bd = base

    @property
    def bd(self):
        return self.__bd
