pages
+++++
This is where other things related to your pages are placed, e.g. transitions definition and methods whose scope is limited to pages only.


__init__.py
===========
For this dunder init file, besides its function to recognize the directory, in this case is ``/pages``, as a Python package, it also defines a ``Page`` class, which the parent of all your pages in the future.

.. code-block:: python

    class Page(ABC):
        def __init__(self, base: BaseDriver) -> None:
            self.__bd = base
            self.jpnFormats = ["jpn", "japan", "japanese", "jp"]
            self.engFormats = ["eng", "english", "en"]
            self.emptyFormats = ["", "-", "<blank>", "<empty>", "blank", "empty"]
            self.anyFormats = ["anything", "dc", "Any", "any"]
            self.spaceFormats = ["<space>"]

        @property
        def bd(self):
            return self.__bd

        @abstractmethod
        def changeState(self):
            pass

The ``Page`` class has a number of attributes, but actually the crucial one is only the ``self.__bd`` that defines the ``BaseDriver`` composition object, which can be retrieved through ``bd()`` property. This setup is used so the value of the ``bd`` will remain consistent since it can not be changed from outside the class.

The other attributes are defined just for the purpose of variables centralization, so it avoids the code becoming repetitive. 

Besides ``bd()``, there is another method, which is an ``abstractmethod``, that requires to all the childs of this class to define it. This method is part of the implementation of State Design Pattern, which is used to change current state to a new state.


example_page.py
===============
This holds an example of your specific page class. This type of class is considered as the Context. If you have already read about `State Design Pattern <https://refactoring.guru/design-patterns/state>`_, then you probably already familiar with it. 

.. code-block:: python

    class ExamplePage(Page):
        """Example Page action methods"""

        def __init__(self, base):
            super().__init__(base)
            self.lr = ExampleLocator(base)

Other than the ``super()`` that inherits the methods and attributes of the parent ``Page`` class, it also has a ``self.lr`` that should be assigned with a specific locator of that page class.

.. code-block:: python

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

Besides the ``changeState()`` that has been introduced before, the above code are the example of interface methods. These methods are used about achieving a separation of concerns and enabling dynamic behavior based on the state. The ``Context`` class does not need to know the specific details of how each state handles requests; it relies on the common interface defined by the ``State`` class.