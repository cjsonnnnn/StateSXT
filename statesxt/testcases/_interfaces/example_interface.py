from . import StateInterface

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.example_page import ExamplePage


class ExampleInterface(StateInterface, ABC):
    def __init__(self, base, contextPage: "ExamplePage") -> None:
        super().__init__(base)
        self.cp = contextPage

    def changeLanguage(self, *args, **kwargs):
        pass
