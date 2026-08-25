import pytest

@pytest.mark.usefixtures("dataload")
class TestExample:
    def test_fixtureDemo(self,dataload):
        print("This is my fixture demo")
        print(dataload)

    def test_fixtureDemo1(self):
        print("This is my fixture demo")

    def test_fixtureDemo2(self):
        print("This is my fixture demo")
