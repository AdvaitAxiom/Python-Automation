import pytest

@pytest.mark.usefixtures("setup")
class TextExample:
    def fixtureDemo(self):
        print("This is my fixture demo")

    def fixtureDemo(self):
        print("This is my fixture demo")

    def fixtureDemo(self):
        print("This is my fixture demo")
