from testcases._states.example_states.ls001 import ExampleInitState
from locators.example_locator import ExampleLocator
from . import Page


class ExamplePage(Page):
    """Example Page action methods"""

    def __init__(self, base):
        super().__init__(base)
        self.initState = ExampleInitState(base, self)
        self.state = self.initState
        self.lr = ExampleLocator(base)

    # Interface Methods
    def changeState(self, newState):
        self.state = newState

    def changeLanguage(self, *args, **kwargs):
        return self.state.changeLanguage(*args, **kwargs)

    # Other methods specific to this page
