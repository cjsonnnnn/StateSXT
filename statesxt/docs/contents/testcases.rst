##########
/testcases
##########

This folder will mostly contain test scenarios categorized by page. While the rest are fixtures, interfaces, and states.

.. note::
    There are few files/folders that the naming begins with ``_``. The reason is simply so that they will be placed at the beginning of the folder they are in, which in this case is ``/testcases``.


/_fixtures
==========
This folder, ``/_fixtures``, will contains fixtures.

A fixture is a Pytest feature that provides a way to set up and tear down resources or perform setup and cleanup operations before and after tests. It can help to modularize and reuse code related to test setup and teardown, making test code cleaner and more maintainable.

A fixture function in Pytest is marked with the ``@pytest.fixture`` decorator. When a test function includes the fixture function as an argument, Pytest automatically invokes the fixture function and passes its return value to the test function. This allows you to perform setup operations, provide data, or create resources that are required for the test.


__init__.py
-----------
This dunder init file does not contain anything, so its presence only to recognize the directory, which in this case is ``/_fixtures``.


composition_fixture.py
----------------------
This file contains all composition fixtures. They are called as a composition because the way they are most likely to be used is as a composition, i.e. defining an instance into a class attribute.

These are several composition fixtures you can use,

* ``logger``

  .. code-block:: python

    @pytest.fixture(scope="session")
    def logger():
        lg = Logger()
        yield
        lg.shutdown()

  This fixture's scope is session, meaning that it will be destroyed at the end of the test session.

  Inside the function, first it defines a Logger from ``/utils/logger.py`` as in the setup. Meanwhile, in the teardown, it shutdowns the Logger instance.
    
* ``gsheet``

  .. code-block:: python

    @pytest.fixture(scope="session")
    @pytest.mark.usefixtures("use_gsheet")
    @pytest.mark.usefixtures("tfo")
    def gsheet(request, use_gsheet, tfo):
        usedMarkers = request.config.getoption("-m").split(" and ")
        if "scheduler" in usedMarkers:
            yield None
            return
        gsheet_bbui = GSheetYOURPROJECT(
            spreadsheetName=os.getenv("SPREADSHEET_NAME"),
            folderId=os.getenv("FOLDER_ID"),
            testedFilesOnly=False if (tfo == "0") else True,
        )
        yield gsheet_bbui
        if use_gsheet == "1":
            print("updating gsheet...")
            gsheet_bbui.update_all_values()
            gsheet_bbui.update_worksheet_colors()

  This fixture has several decorators. The ``@pytest.fixture(scope="session")`` is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session. As for the rest, are implementing other fixtures into this function that each to give the capability to insert a configuration into CLI, e.g. for the ``@pytest.mark.usefixtures("use_gsheet")`` enables you to insert ``use_gsheet``, which the value either 0 or 1, into CLI.

  Inside the function, it enables an option ``-m`` into CLI and defines a GSheet as in the setup. Meanwhile, in the teardown, it invokes some methods from GSheet if tha value of ``use_gsheet`` is 1.
    

* ``email``

  .. code-block:: python

    @pytest.fixture(scope="session")
    @pytest.mark.usefixtures("use_email")
    def email(use_email):
        # create an email instance
        email = EmailScheduler(
            sender_email=os.getenv("SENDER_EMAIL"),
            sender_password=os.getenv("SENDER_PASSWORD"),
            receiver_email=os.getenv("RECEIVER_EMAIL").split(","),
            receiver_name=os.getenv("RECEIVER_NAME").split(","),
        )
        yield email
        print(f"\n\nResults:\n{email.testResult}\n")
        if use_email == "1":
            # send email
            try:
                print("Sending email...")
                email.send()
                print("Email has been sent successfully.")
            except Exception as e:
                print(f"Email failed to send: {str(e)}")

  This fixture has 2 decorators. The ``@pytest.fixture(scope="session")`` is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session. Meanwhile, ``@pytest.mark.usefixtures("use_email")`` is implementing another fixture into this function that gives the capability to insert a configuration into CLI.

  Inside the function, it defines an EmailScheduler from ``/utils/email.py`` as in the setup. Meanwhile, in the teardown, it invokes some methods from EmailScheduler if tha value of ``use_email`` is 1.


option_fixture.py
-----------------
This file contains all option fixtures. They are called as an option because they can give the capability to insert an option into CLI.

These are several option fixtures you can use,

* ``pytest_addoption``

  .. code-block:: python

    def pytest_addoption(parser):
        parser.addoption("--browser", "-B")
        parser.addoption("--use_gsheet")
        parser.addoption("--use_email")
        parser.addoption("--tfo")
        parser.addoption(
            "--number-help",
            action="store_true",
            default=False,
            help="Print custom number help information and exit.",
        )

  This function is a hook in the pytest framework. When pytest runs, it calls this function, passing an argument called ``parser``. The ``parser`` is an instance of the ``ArgumentParser`` class from the ``argparse`` module, and it is used to define command-line options for your pytest scripts. It allows to specify various options when running the pytest scripts, such as the browser to use, whether to use Google Sheets or email functionalities, and potentially some custom behavior related to numbers.

* ``browser``

  .. code-block:: python

    @pytest.fixture(scope="session")
    def browser(request):
        req = request.config.getoption("--browser") or request.config.getoption("-B")
        return req if req else "chrome"

  This fixture has a decorator, ``@pytest.fixture(scope="session")``, that is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session.

  This fixture allows you to specify the browser to be used in your tests through command-line options while providing a default value of "chrome" if no option is specified.


* ``use_gsheet``

  .. code-block:: python

    @pytest.fixture(scope="session")
    def use_gsheet(request):
        req = request.config.getoption("--use_gsheet")
        return req if req else "1"

  This fixture has a decorator, ``@pytest.fixture(scope="session")``, that is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session.

  This fixture allows you to specify whether to use Google Sheets in your tests through the ``--use_gsheet`` command-line option. If the option is not specified, the default value "1" is used. 

* ``use_email``

  .. code-block:: python

    @pytest.fixture(scope="session")
    def use_email(request):
        req = request.config.getoption("--use_email")
        return req if req else "1"

  This fixture has a decorator, ``@pytest.fixture(scope="session")``, that is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session.

  This fixture allows you to specify whether to use email functionality in your tests through the ``--use_email`` command-line option. If the option is not specified, the default value "1" is used.

* ``tfo``

  .. code-block:: python

    @pytest.fixture(scope="session")
    def tfo(request):
        req = request.config.getoption("--tfo")
        return req if req else "1"
  
  This fixture has a decorator, ``@pytest.fixture(scope="session")``, that is used to declare this function as a fixture with ``session`` as the scope, meaning that it will be destroyed at the end of the test session.

  The name 'tfo' stands for 'tested files only'. This fixture allows you to control whether to generate a worksheet report only for tested files in your tests using the ``--tfo`` command-line option. If the option is not specified, the default value "1" is used, indicating that the worksheet report should include only tested files.

* ``pytest_collection_modifyitems``

  .. code-block:: python

    def pytest_collection_modifyitems(config, items):
        if config.option.number_help:
            print(
                """
            Browser:
            - 1 = brave
            - 2 = chrome
            - 3 = edge
            - 4 = firefox

            """
            )
            items.clear()

  It is a hook in the pytest framework that allows you to modify the test items collected during the test collection phase. In this specific case, it checks if the ``--number-help`` option is provided, and if so, it prints information about browser options and clears the test items. This can be helpful for providing user guidance on browser options without running the tests.


/_interfaces
============


__init__.py
-----------


example_interface.py
--------------------


/_states
========


example_states.py
-----------------


__init__.py
~~~~~~~~~~~


ls001.py
~~~~~~~~


__init__.py
-----------


/example
========


__init__.py
-----------


test_0_1.py
-----------


__init__.py
===========


conftest.py
===========

