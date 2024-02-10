import pytest

from database.service import DBService
from base.base_driver import BaseDriver
from ._fixtures.option_fixture import *
from ._fixtures.composition_fixture import *


@pytest.fixture(scope="class")
@pytest.mark.usefixtures("logger")
@pytest.mark.usefixtures("browser")
@pytest.mark.usefixtures("gsheet")
@pytest.mark.usefixtures("email")
def setup(request, logger, browser, gsheet, email):
    logger

    # setup driver
    base = BaseDriver(browser, fullscreen=True)

    # setup service
    service = DBService()
    service.start()

    # set requests
    request.cls.base = base
    request.cls.service = service
    request.cls.gsheet = gsheet
    request.cls.email = email

    yield

    service.end()
    base.exit()
