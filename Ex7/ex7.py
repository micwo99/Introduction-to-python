#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

def print_to_n(n):
    """
    the function print the numbers from 1 to n
    """
    if n <= 0:
        return None
    if n == 1:
        print(1)
    else:
        print_to_n(n-1)
        print(n)


def digit_sum(n):
    """
    the function receive a number n and return the sum of the digits of n 
    :param n: 
    :return:sum of digits of n 
    """""
    if n == 0:
        return 0
    else:
        x = n % 10
        n = (n-x)/10
    return int(x+digit_sum(n))


def has_divisor_smaller_than(n,i):
    """
    the function check if the numbers between 1 and i divide
    or not n if yes the function return true
    """

    if i >= 2:
        if n % i == 0:
            return True
        else:
            return has_divisor_smaller_than(n,i-1)


def is_prime(n):
    """
    the function return True if n is prime and False if n is'nt prime
    """
    if n<=1:
        return False
    if has_divisor_smaller_than(n, int(n ** 0.5)):
        return False
    else:
        return True


def play_hanoi(hanoi,n,src,dst,temp):
    """
    the function resolve the the hanoi tower
    :param hanoi:
    :param n: number of disk
    :param src: the rod where all the disks are at hte beginning
    :param dst: the rod where we want that all the disk are at the end of the game
    :param temp: auxiliary rod
    """
    if n < 0:
        n = 0
    if n == 1:
        hanoi.move(src,dst)
    else:
        play_hanoi(hanoi,n-1,src,temp,dst)
        hanoi.move(src,dst)
        play_hanoi(hanoi,n-1,temp,dst,src)


def print_sequence_helper(char_list, n, curr=[]):
    """
    the function prints all possible combinations of n lengths of characters from the list
    :param char_list: characters list
    :param n: length of the combinations
    :param curr: empty list
    """
    if n == 0:
        for char in curr:
            print(char, end='')
        print('')

    else:
        for char in char_list:
            print_sequence_helper(char_list, n - 1, [char] + curr)


def print_sequences(char_list,n):
    """
    the function prints all possible combinations of n lengths
    of characters from the list
    :param char_list: characters list
    :param n: length of the combinations
    """
    print_sequence_helper(char_list,n,[])



def print_no_repetition_sequences_helper(char_list,n,curr=[]):
    """
    the function prints all possible combinations of n length
    of characters from the list  without repetition
    :param char_list:characters list
    :param n:length of the combination
    :param curr: empty list
    """

    if n == 0:
        for i in curr:
            print(i, end='')
        print('')

    else:
        for char in char_list:
            char_list2 = []
            for char2 in char_list:
                if char2 != char:
                    char_list2.append(char2)
            print_no_repetition_sequences_helper(char_list2, n - 1, [char] + curr)


def print_no_repetition_sequences(char_list,n):
    """
    the function prints all possible combinations of n length
    of characters from the list  without repetition
    :param char_list:characters list
    :param n:length of the combination
    """
    print_no_repetition_sequences_helper(char_list,n,[])


def parentheses_help(countToOpen, countToClose, ans=[], string =''):
    """
    the function return a list of all strings with n valid pairs of parentheses
    :param countToOpen: count the number of '('
    :param countToClose:  count the number of ')'
    :param ans: list of all the combinations with n valid pairs of parentheses
    :param string: strings that the code add to ans
    :return: ans
    """
    if countToOpen == countToClose == 0:
        return ans.append(string)
    if countToOpen < countToClose:
        parentheses_help(countToOpen, countToClose - 1, ans, string + ')')
    if countToOpen > 0:
        parentheses_help(countToOpen - 1, countToClose, ans, string+ '(')
    return ans


def parentheses(n):
    """
    the function return a list of all strings with n valid pairs of parentheses
    :param n: number of pairs of parentheses
    :return: a list that contains all the combination of n valid pairs of parentheses
    """
    if n==0:
        return [""]
    return parentheses_help(n, n, [])

def flood_fill_help(image,a,b):
    """
    The function replaces the characters "." by characters "*" start from the start point
    according to the instructions of the exercise.
     The function changes the original image and fills it with the "*" character in the correct places.
     It should be noted that only the cells that can be accessed from the starting point will only be filled
     with cells with the character "." .

    :param image: list of list that contains or '*'or '.'
    :param a:the first coordinate of the starting point
    :param b:the second coordinate of the starting point

    """
    if image[a][b] == '.':
        image[a][b]= '*'
        flood_fill_help(image, a - 1, b)
        flood_fill_help(image, a , b-1)
        flood_fill_help(image, a+1, b)
        flood_fill_help(image, a, b + 1)


def flood_fill(image,start):
    """
        The function replaces the characters "." by characters "*" start from the start point
        according to the instructions of the exercise.
         The function changes the original image and fills it with the "*" character in the correct places.
         It should be noted that only the cells that can be accessed from the starting point will only be filled
         with cells with the character "." .

        :param start:  starting point with two coordinates
        :param image: list of list that contains or '*'or '.'
        """
    flood_fill_help(image, start[0], start[1])
    print(image)

