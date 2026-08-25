import pytest

@pytest.mark.smoke 
def test_program5():
    msg = "Alapan"
    assert msg == "Alapan", "Assertion failure"

@pytest.mark.skip
def test_program6():
    a = 10
    b = 20
    assert b - a  == 10, "Sum is not equal to 30"

#written in conftest.py file
# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#     yield
#     print("I will execute last")

def test_program7(setup):   
    print("I will execute second")