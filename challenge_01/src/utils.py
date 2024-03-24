def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "undefined"


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
