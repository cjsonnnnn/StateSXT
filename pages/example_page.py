from statesxt.locators.example_locator import ExampleLocator
from . import Page


class ExamplePage(Page):
    """Analysis Profile Page action methods"""

    def __init__(self, base):
        super().__init__(base)
        self.lr = ExampleLocator(base)

    # Interface Methods
    def changeState(self, newState):
        self.state = newState

    def clickLogin(self, *args, **kwargs):
        return self.state.clickLogin(*args, **kwargs)

    def changeLanguage(self, *args, **kwargs):
        return self.state.changeLanguage(*args, **kwargs)

    def success(self, *args, **kwargs):
        return self.state.success(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.state.error(*args, **kwargs)