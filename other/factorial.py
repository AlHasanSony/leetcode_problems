# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


def factorial(n):
    if n < 0:
        return "Error"
    if n in [0,1]:
        return 1
    return n * factorial(n - 1)


def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 1
    assert factorial(-1) == None
    assert factorial(5) == 120
    