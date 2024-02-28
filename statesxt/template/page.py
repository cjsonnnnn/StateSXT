from .states.ls01 import ExampleInitState
from .locator import ExampleLocator
from .. import Page


class ExamplePage(Page):
    """Example Page action methods"""

    def __init__(self, base):
        super().__init__(base)
        self.initState = ExampleInitState(base, self)
        self.state = self.initState
        self.lr = ExampleLocator(base)

    """
    Methods: Abstract
    """

    def changeState(self, newState):
        self.state = newState

    def resetState(self):
        self.state = self.initState

    """
    Methods: Interface
    """

    def changeLanguage(self, lang):
        return self.state.changeLanguage(lang)

    """
    Methods: Specific
    """
