#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
# I choose the values (1,2,1) to show if for 2 same values in a different position it will give also true
# I also chose (1,1,1) to see if the function work with 3 same values
#########################################





def largest_and_smallest(a, b, c):  # function that return 2 values: the maximal and the minimal
    if a >= b >= c:
        return a, c
    elif a >= c >= b:
        return a, b
    elif b >= a >= c:
        return b, c
    elif b >= c >= a:
        return b, a
    elif c >= a >= b:
        return c, b
    elif c >= b >= a:
        return c, a


def check_largest_and_smallest():  # function that check if the precedent function work or not
    x1 = largest_and_smallest(17, 1, 6)

    x2 = largest_and_smallest(1, 17, 6)

    x3 = largest_and_smallest(1, 1, 2)

    x4 = largest_and_smallest(1, 2, 1)

    x5 = largest_and_smallest(1, 1, 1)

    if x1 == (max(x1), min(x1)):
        return True
    elif x2 == (max(x2), min(x3)):
        return True
    elif x3 == (max(x3), min(x3)):
        return True
    elif x4 == (max(x4), min(x4)):
        return True
    elif x5 == (max(x5), min(x5)):
        return True

    return False





