from .. import Locator


class ExampleLocator(Locator):
    """Example page locator class"""

    def __init__(self, base) -> None:
        super().__init__(base)
        self.setup()

    def setup(self):
        # flags
        self.JPN_FLAG_BUTTON = lambda loc="//div[@class='d-flex justify-content-center']//label[1]": self.bd.wd.clickable(self.by.xpath, loc)
        self.ENG_FLAG_BUTTON = lambda loc="//div[@class='d-flex justify-content-center']//label[2]": self.bd.wd.clickable(self.by.xpath, loc)
