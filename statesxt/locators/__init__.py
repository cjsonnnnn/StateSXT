from base.base_driver import BaseDriver
from base.wait import MyBy


class Locator:
    """A parent class of all page locator classes."""

    def __init__(self, base: BaseDriver) -> None:
        self.__bd = base
        self.by = MyBy()

    @property
    def bd(self):
        return self.__bd
