import pytest

"""
Set Role
"""
# region


@pytest.fixture(scope="class")
def admin(request):
    request.cls.role = "admin"


@pytest.fixture(scope="class")
def managaer(request):
    request.cls.role = "manager"


@pytest.fixture(scope="class")
def operator(request):
    request.cls.role = "operator"


@pytest.fixture(scope="class")
def supervisor(request):
    request.cls.role = "supervisor"


# endregion


"""
Set State
"""


# region
@pytest.fixture(scope="class")
def state1(request):
    request.cls.state = 1


@pytest.fixture(scope="class")
def state2(request):
    request.cls.state = 2


@pytest.fixture(scope="class")
def state3(request):
    request.cls.state = 3


@pytest.fixture(scope="class")
def state5(request):
    request.cls.state = 4


@pytest.fixture(scope="class")
def state5(request):
    request.cls.state = 5


@pytest.fixture(scope="class")
def state6(request):
    request.cls.state = 6


@pytest.fixture(scope="class")
def state7(request):
    request.cls.state = 7


# endregion
