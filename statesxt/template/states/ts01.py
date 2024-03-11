from ..interface import ExampleInterface


class ExampleInitState(ExampleInterface):
    def __init__(self, base, contextPage) -> None:
        super().__init__(base, contextPage)

    def exampleTransition(self, exampleParam):
        # required process
        self.bd.fd.insert_to_textbox(self.p.lr.exampleLocator1(), exampleParam)
        # transition
        self.p.changeState(ExampleInitState(self.bd, self.p))
