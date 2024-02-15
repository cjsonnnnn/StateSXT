from .states.ls001 import ExampleInitState
from .locator import ExampleLocator
from .. import Page


class ExamplePage(Page):
    """Example Page action methods"""

    def __init__(self, base):
        super().__init__(base)
        self.initState = ExampleInitState(base, self)
        self.state = self.initState
        self.lr = ExampleLocator(base)

    # Interface Methods
    def changeState(self, newState):        # abstract method
        self.state = newState

    def resetState(self):                   # abstract method
        self.state = self.initState

    def changeLanguage(self, lang):
        return self.state.changeLanguage(lang)

    # Other methods specific to this page
