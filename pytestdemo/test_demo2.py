import pytest as pt

@pt.mark.xfail
def test_program3():
    msg = "Alapan"
    assert msg == "alapan", "Assertion failure"
@pt.mark.smoke
def test_program4Marked():
    a=10
    b=20
    assert a+b == 30, "Sum is not equal to 30"