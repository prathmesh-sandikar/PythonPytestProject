import Calculator
import pytest




# def test_add():
@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,12,22),(2,5,7),(7,8,15)])
def test_add(a,b,c):
    # x = 10
    # y = 25
    # result=Calculator.add()
    # assert x+y == result
    result = Calculator.add(a,b)
    assert c == result


# def test_subtract():
@pytest.mark.parametrize("a,b,c",[(3,2,1),(12,11,1),(12,5,7),(11,5,6)])
def test_subtract(a,b,c):
    # x=20
    # y=10
    # result= Calculator.substract(x,y)
    # assert x-y == result

    result = Calculator.substract(a,b)
    assert c == result

# def test_multiply():
#     x=5
#     y=5
#     result= Calculator.multiply(x,y)
#     assert x*y == result

@pytest.mark.parametrize("a,b,c", [(3, 2, 6), (1, 12, 12), (2, 5, 10), (7, 8, 56)])
def test_multiply(a,b,c):
    result= Calculator.multiply(a,b)
    assert c == result

# def test_divide():
#     x=20
#     y=10
#     result = Calculator.divide(x,y)
#     assert x/y == result
@pytest.mark.parametrize("a,b,c", [(10, 2, 5), (10, 5, 2), (2, 1, 2), (14, 2, 7)])
def test_divide(a,b,c):

    result = Calculator.divide(a,b)
    assert c == result