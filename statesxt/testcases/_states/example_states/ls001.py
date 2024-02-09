from ..._interfaces.example_interface import ExampleInterface


class ExampleInitState(ExampleInterface):
    def __init__(self, base, contextPage) -> None:
        super().__init__(base, contextPage)

    def changeLanguage(self, lang):
        # required process
        if lang in self.cp.jpnFormats:
            self.bd.mkd.clicking(self.cp.lr.JPN_FLAG_BUTTON(), sleep=0)
        elif lang in self.cp.engFormats:
            self.bd.mkd.clicking(self.cp.lr.ENG_FLAG_BUTTON(), sleep=0)
        # transition
        self.cp.changeState(ExampleInitState(self.bd, self.cp))