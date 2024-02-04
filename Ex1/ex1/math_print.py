import math


def golden_ratio():  # function that prints the golden ratio
    print((1 + 5 ** (1 / 2)) / 2)


def six_squared():  # function that prints six squared
    print(6 ** 2)


def hypotenuse():  # function that print the hypotenuse of the triangle with (12,5) as sides
    print(((12 ** 2) + (5 ** 2)) ** (1 / 2))


def pi():  # function that print the value of pi
    print(math.pi)


def e():  # function that print the value of e
    print(math.e)


def squares_area():  # function that print the area of a square, the length of the side goes from 1 to 10
    print(1 ** 2, 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2, 6 ** 2, 7 ** 2, 8 ** 2, 9 ** 2, 10 ** 2)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
