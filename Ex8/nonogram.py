#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
# I choose in the function get_intersection_row will return [-1 ,-1 ,-1] when the parameters are:
# [-1 ,-1- ,-1] ,[0, 1, -1] because it is in coherence with the algorithm
#
#########################################

import copy
import math


def get_row_variations_helper(row, blocks, lst, k):
    """
    the function returns all the possibilities of list in a way that the coloration matches the blocks values
    :param row:list of 1, -1, 0
    :param blocks:list of numbers
    :param lst: list t of list
    :param k: index
    """

    if blocks == [] or blocks == [0] and 1 not in row:
        lst.append([0] * len(row))
        return
    if blocks == [] or blocks == [0] and 1 in row:
        return
    if k == len(row):
        if -1 not in row and row not in lst and blocks == count_ones_in_a_row(row):
            lst.append(row[:])
        return
    if not check_block(row, blocks):
        return

    row_copy = row[:]
    if row[k] == -1:
        if row.count(1) < sum(blocks):
            row_copy[k] = 1
            get_row_variations_helper(row_copy, blocks, lst, k + 1)
        row_copy[k] = 0
        get_row_variations_helper(row_copy, blocks, lst, k + 1)
        return
    get_row_variations_helper(row_copy, blocks, lst, k + 1)
    return


def get_row_variations(row, blocks):
    """
     the function returns all the possibilities of list in a way that the coloration matches the blocks values
    :param row: list that contains 0,1,-1
    :param blocks: list of numbers
    :return: lst
    """
    lst = []
    get_row_variations_helper(row, blocks, lst, 0)
    return lst


def check_block(row, blocks):
    """
    the function checks if constraints can be apply on the row
    :param row: list that contains 1,0,-1
    :param blocks: constraints, list of numbers
    :return: True/False
    """
    if row.count(0) > len(row) - sum(blocks):
        return False

    if -1 in row:
        i = row.index(-1)
        block_row = count_ones_in_a_row(row[:i])
        for k in range(len(block_row) - 1):
            if block_row[k] != blocks[k]:
                return False
        if len(block_row) > len(blocks):
            return False
        if len(block_row) > 0:
            if block_row[len(block_row) - 1] > blocks[len(block_row) - 1]:
                return False
        return True
    else:
        if count_ones_in_a_row(row) == blocks:
            return True
        return False


def count_ones_in_a_row(lst):
    """
    count how much 1 in a row there are
    :param lst: list that contains 1,0,-1
    :return: list of numbers
    """
    result = []
    counter = 0
    for k in lst:
        if k == 1:
            counter += 1
        else:
            if counter != 0:
                result.append(counter)
                counter = 0
    if counter != 0:
        result.append(counter)
    if result == []:
        result = [0]

    return result


def get_intersection_row(rows):
    """
    the functions returns a list that contains -1,1,0 that is the intersection of the list of rows
    :param rows:list of list
    :return: list of 1, 0, -1
    """
    result = []

    for k in range(len(rows[0])):
        add = 0
        for i in range(len(rows)):
            elem = rows[i][k]
            if elem == -1:
                add = -1
                break
            add += elem
        if add == 0:
            result.append(0)
        elif add == len(rows):
            result.append(1)
        else:
            result.append(-1)
    return result


def solve_easy_nonogram_helper(constraints, board):
    """
    the function helper of solve easy nonogram
    :param constraints: list that represents the constraints of columns and the constraints of lines
    :param board: list of list
    :return: the solution of the nonogram
    """

    board_copy = board[:]
    while True:
        result = []
        for y in range(len(board_copy)):
            rows = get_row_variations(board_copy[y], constraints[0][y])
            if not rows:
                return None
            new = get_intersection_row(rows)
            result.append(new)
        transposition = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
        trans_lst = []

        for x in range(len(transposition)):
            rows = get_row_variations(transposition[x], constraints[1][x])
            if not rows:
                return None

            new = get_intersection_row(rows)
            trans_lst.append(new)
        res = [[trans_lst[j][i] for j in range(len(trans_lst))] for i in range(len(trans_lst[0]))]
        if res == board_copy:
            break
        else:
            board_copy = res
    return res


def solve_easy_nonogram(constraints):
    """
    the function returns the solution of the nonogram
    :param constraints: list that represents the constraints of columns and the constraints of lines
    :return: the solution of the nongram
    """
    row = [-1] * len(constraints[1])
    board = []
    for x in range(len(constraints[0])):
        board.append(row)
    return solve_easy_nonogram_helper(constraints, board)


def valid_lst(lst):
    """
    the function check if there is a -1 in items of lst
    :param lst: list of list
    :return: True/False
    """
    for k in lst:
        if -1 in k:
            return False
    return True


def solve_nonogram_helper(board, constraints, lst, i):
    """
    helper of solve nonogram
    :param board:list of list
    :param constraints: list that represents the constraints of columns and the constraints of lines
    :param lst: the solution of the nonogram
    :param i: index
    :return:
    """

    if valid_lst(board) and board not in lst:
        lst.append(board)
        return

    if i < len(board):
        if -1 in board[i]:
            copy_board1 = copy.deepcopy(board)
            copy_board2 = copy.deepcopy(board)
            index = copy_board1[i].index(-1)
            copy_board1[i][index] = 1
            copy_board1 = solve_easy_nonogram_helper(constraints, copy_board1)
            solve_nonogram_helper(copy_board1, constraints, lst, i + 1)
            copy_board2[i][index] = 0
            copy_board2 = solve_easy_nonogram_helper(constraints, copy_board2)
            solve_nonogram_helper(copy_board2, constraints, lst, i + 1)
        if i > 0:
            solve_nonogram_helper(board, constraints, lst, i - 1)


def solve_nonogram(constraints):
    """
    the function solves the nonogram
    :param constraints:
    :return:
    """
    board = solve_easy_nonogram(constraints)
    lst = []
    solve_nonogram_helper(board, constraints, lst, 0)
    return lst


def count_row_variations(length, blocks):
    """
    the function return the number of possibilities of coloration depending on length and blocks
    :param length: length of the list
    :param blocks: list of numbers
    :return: number of possibilities
    """

    n = len(blocks) + 1
    k = length - (sum(blocks) + len(blocks) - 1)
    if k < 0:
        return 0
    number_of_possibilities = int(math.factorial(n + k - 1) / (math.factorial(k) * math.factorial(n - 1)))
    return number_of_possibilities
