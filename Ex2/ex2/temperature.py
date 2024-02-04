#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################


def is_it_summer_yet(temp1, temp2, temp3, temp4):
    # function that say to us if it has at least two parameters which are equal or greater than the first parameter
    if temp1 <= temp2 and temp1 <= temp3:
        return True
    elif temp1 <= temp2 and temp1 <= temp4:
        return True
    elif temp1 <= temp3 and temp1 <= temp4:
        return True
    return False
