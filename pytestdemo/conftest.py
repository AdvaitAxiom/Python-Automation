import pytest

@pytest.fixture()
def setup():
    print("First start fixtue for all")
    yield
    print("Last end fixtue for all")


@pytest.fixture()
def dataload():
    print("This is my data load")
    return ["Alapan", "Das", "Python"]