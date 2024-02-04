#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

import math


def shape_area():  # the function give us the value of the area of a circle or a rectangle or a triangle
    shape = input('Choose shape (1=circle, 2=rectangle, 3=triangle): ')

    if shape == '1':
        radius = float(input())
        return math.pi*(radius**2)

    elif shape == '2':
        side1 = float(input())
        side2 = float(input())
        return side1*side2

    elif shape == '3':
        side = float(input())
        return ((3**0.5)/4)*(side**2)

    return None  # if we choose something than 1,2 or 3 the function will return None


