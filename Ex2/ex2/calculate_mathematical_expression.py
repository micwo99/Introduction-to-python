#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

def calculate_mathematical_expression(a, b, op):
    # function that return the calculated value of the accounting expression
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return None
        return a / b
    else:
        return None


def calculate_from_string(s):
    a, op, b = s.split()
    a = float(a)
    b = float(b)
    return calculate_mathematical_expression(a, b, op)

