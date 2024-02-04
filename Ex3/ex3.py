#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################


def input_list():
    """ the function receive several numbers from the user and will return a list of all those number and at
    the end of the list their sum"""

    lst = []  # lst will be the list that the function return
    num_from_user = input()  # num_from_user represents what the user will enter in the code
    summ = 0  # summ will represent the sum of all the value of num_from_user

    if num_from_user == "":
        num_from_user = 0
        lst.append(num_from_user)  # if the first input is a empty string the first value in the lst will be 0
        num_from_user = input()

    # the input will be add to the list if it"s a number and the user will choose again a input
    # until that the user insert a input which is a empty string
    while num_from_user != "":
        num_from_user = float(num_from_user)
        lst.append(num_from_user)  # if the input is not a empty string so we will add the input to the list
        summ += num_from_user  # we will add to summ the value of the input until that we get out of the loop
        num_from_user = input()
    lst.append(summ)
    return lst


def inner_product(vec_1, vec_2):
    """ The function return the inner product of two vectors"""
    summ = 0  # it will be the inner product of the two vectors
    if len(vec_1) != len(vec_2):
        return None
    elif vec_1 == [] and vec_2 == []:
        return 0

    for i in range(len(vec_1)):
        # the loop give the inner product of vec_1 and vec_2 if the length of vec_1 and vec_2 are equal
        # and if vec_1 and vec_2 aren't empty lists
        summ += vec_1[i] * vec_2[i]
    return summ


def sequence_monotonicity(sequence):
    """the function recive a list of numbers and return the list of 4 element boolean that will say if the list
    of numbers are monotonically increasing, strictly increasing, monotonically decreasing, strictly decreasing"""
    result = []  # it will be the list that the function return that will say if the sequence meets the 4 definitions
    i = 0
    j = 0
    k = 0
    m = 0
    if len(sequence) == 0:
        result.extend([True, True, True, True])

    while i < len(sequence) - 1:  # monotonically increasing
        if sequence[i] > sequence[i + 1]:
            result.append(False)
            break
        i = i + 1
    if i == len(sequence) - 1:
        result.append(True)

    while j < len(sequence) - 1:     # strictly increasing
        if sequence[j] >= sequence[j + 1]:
            result.append(False)
            break
        j = j + 1
    if j == len(sequence) - 1:
        result.append(True)

    while k < len(sequence) - 1:  # monotonically decreasing
        if sequence[k] < sequence[k + 1]:
            result.append(False)
            break
        k = k + 1
    if k == len(sequence) - 1:
        result.append(True)

    while m < len(sequence) - 1:  # strictly decreasing
        if sequence[m] <= sequence[m + 1]:
            result.append(False)
            break
        m = m + 1
    if m == len(sequence) - 1:
        result.append(True)

    return result


def monotonicity_inverse(def_bool):
    """ the function return sequence examples
     which holds the 4 definitions  which are in the precedent function"""

    if def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    elif def_bool == [True, False, False, False]:
        return [1, 2, 2, 3]
    elif def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    elif def_bool == [False, False, False, False]:
        return [1, 2, 1, 2]
    elif def_bool == [False, False, True, True]:
        return [4, 3, 2, 1]
    elif def_bool == [False, False, True, False]:
        return [4, 2, 2, 1]
    else:
        return None


def is_prime_fast(n):
    """ Function that check if a number is prime"""
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_for_asafi(n):
    """ the function will return a list of n prime number """
    res = []  # res will be the list of n prime number
    i = 2  # i will be the number that we will check if is prime or not

    while len(res) < n:  # Check all the numbers if they are prime until there are n numbers prime
        if is_prime_fast(i):
            res.append(i)
        i = i + 1
    return res


def sum_of_vectors(vec_lst):
    """ the function will receive a list of vectors and will will return the inner product of the vectors"""
    lst = []  # it will be the list of the inner products of the vectors that the function received
    summ = 0  # it will be the sum of the numbers in the same range of the vectors
    j = 0
    if vec_lst == []:
        return None
    if vec_lst[0] == []:
        return []
    # this loop give the list of the result from an addition of vectors
    while j < len(vec_lst[0]):
        summ = 0
        for i in range(len(vec_lst)):
            summ = summ + (vec_lst[i][j])
        lst.append(summ)
        j = j + 1

    return lst


def num_of_orthogonal(vectors):
    """the function will receive a lis of vectors and will return the number of pairs of orthogonal vectors"""
    num_of_pairs = 0  # it will be the number of pairs of orthogonal vectors in the function
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            # we don't multiply a vector by itself
            if i != j:
                if inner_product(vectors[i], vectors[j]) == 0:
                    num_of_pairs += 1
    num_of_pairs = int(num_of_pairs / 2)
    # number of pairs of orthogonal vectors
    return num_of_pairs
