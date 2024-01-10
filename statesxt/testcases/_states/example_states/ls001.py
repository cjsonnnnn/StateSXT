from ..._interfaces.example_interface import ExampleInterface


class ExamplePageState(ExampleInterface):
    def __init__(self, base, contextPage) -> None:
        super().__init__(base, contextPage)

    def changeLanguage(self, lang):
        # required process
        if lang in self.ep.jpnFormats:
            self.bd.mkd.clicking(self.ep.lr.JPN_FLAG_BUTTON(), sleep=0)
        elif lang in self.ep.engFormats:
            self.bd.mkd.clicking(self.ep.lr.ENG_FLAG_BUTTON(), sleep=0)
        # transition
        self.ep.changeState(ExamplePageState(self.bd, self.ep))