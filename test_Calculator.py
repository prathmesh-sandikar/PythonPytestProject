import Calculator

def test_add():
    x = 10
    y = 25
    result=Calculator.add(x,y)
    assert x+y == result

def test_subtract():
    x=20
    y=10
    result= Calculator.substract(x,y)
    assert x-y == result

def test_multiply():
    x=5
    y=5
    result= Calculator.multiply(x,y)
    assert x*y == result

def test_divide():
    x=20
    y=10
    result = Calculator.divide(x,y)
    assert x/y == result