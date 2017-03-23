def is_digit(num):
    typ = type(num)
    return typ == int or typ == float


def divide(a, b):
    if b == 0:
        return "Infinity"
    if not (is_digit(a) and is_digit(b)):
        return "numbers only"
    return (a / b)
