from base.base_driver import BaseDriver
from base.wait import MyBy


class Locator:
    """Provides all element locators as well as their actions, and returns the elements."""

    def __init__(self, base: BaseDriver) -> None:
        self.__bd = base
        self.by = MyBy()

    @property
    def bd(self):
        return self.__bd
