import pytest


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


@pytest.fixture(scope="session")
def browser(request):
    req = request.config.getoption("--browser") or request.config.getoption("-B")
    return req if req else "chrome"


@pytest.fixture(scope="session")
def use_gsheet(request):
    req = request.config.getoption("--use_gsheet")
    return req if req else "0"


@pytest.fixture(scope="session")
def use_email(request):
    req = request.config.getoption("--use_email")
    return req if req else "0"


@pytest.fixture(scope="session")
def tfo(request):
    req = request.config.getoption("--tfo")
    return req if req else "1"


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
