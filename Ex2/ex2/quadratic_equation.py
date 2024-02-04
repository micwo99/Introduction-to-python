#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

import math


def quadratic_equation(a, b, c):  # Function that return the results of a quadratic equation
    delta = (b ** 2) - 4 * (a * c)

    if a == 0:
        return None, None

    if delta > 0:

        x = (-b+math.sqrt(delta))/(2*a)
        y = (-b-(math.sqrt(delta)))/(2*a)
        return x, y

    elif delta == 0:

        x = (-b)/(2*a)
        return x, None
    elif delta < 0:
        return None, None


def quadratic_equation_user_input():

    # Function that print the result of a quadratic equation or if the coefficient 'a' is equal to 0
    a, b, c = input('Insert coefficients a, b, and c: ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    X, Y = quadratic_equation(a, b, c)

    if a == 0:
        print("The parameter 'a' may not equal 0")

    elif X != None and Y != None:
        print('The equation has 2 solutions:', X, "and", Y)
        return None

    elif X == None and Y != None:
        print("The equation has 1 solution:", X)
        return None

    elif X != None and Y == None:
        print("The equation has 1 solution:", X)
        return None

    elif X == None and Y == None:
        print("The equation has no solutions")
        return None












