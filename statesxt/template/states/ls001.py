from ..interface import ExampleInterface


class ExampleInitState(ExampleInterface):
    def __init__(self, base, contextPage) -> None:
        super().__init__(base, contextPage)

    def changeLanguage(self, lang):
        # required process
        if lang in self.p.jpnFormats:
            self.bd.mkd.clicking(self.p.lr.JPN_FLAG_BUTTON(), sleep=0)
        elif lang in self.p.engFormats:
            self.bd.mkd.clicking(self.p.lr.ENG_FLAG_BUTTON(), sleep=0)
        # transition
        self.p.changeState(ExampleInitState(self.bd, self.p))
