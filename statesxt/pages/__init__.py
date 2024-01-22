from base.base_driver import BaseDriver
from abc import ABC, abstractmethod


class Page(ABC):
    """A parent class of all specific page classes."""

    def __init__(self, base: BaseDriver) -> None:
        self.__bd = base
        self.jpnFormats = ["jpn", "japan", "japanese", "jp"]
        self.engFormats = ["eng", "english", "en"]
        self.emptyFormats = ["", "-", "<blank>", "<empty>", "blank", "empty"]
        self.anyFormats = ["anything", "dc", "Any", "any"]
        self.spaceFormats = ["<space>"]

    @property
    def bd(self):
        return self.__bd

    @abstractmethod
    def changeState(self):
        pass
