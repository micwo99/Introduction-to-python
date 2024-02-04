#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################

import sys
import helper
from board import Board
from car import Car

EXIT_GAME = '!'
CARS_NAME = ['Y', 'B', 'O', 'G', 'W', 'R']
VALID_DIRECTION = ['u', 'd', 'l', 'r']
CAR_LENGTH_MAX = 4
CAR_LENGTH_MIN = 2
VERTICAL = 0
HORIZONTAL = 1
MSG_ERROR = 'the input is invalid'
TARGET_COORDINATE = (3, 7)
SUCCESS_MESSAGE = "YOU WON!!!"
FINISH_MSG = 'you finish to play'
MSG = "you didn't arrive to the target"


class Game:
    """
    the class Game create the platform where we can play the game Rush Hour
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')

        self.__board = board
        self.cars = []

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        user_input = input("choose a name's car and a direction:")
        if user_input == EXIT_GAME:
            return False
        if len(user_input) == 3:
            if user_input[0] in CARS_NAME:
                if user_input[2] in VALID_DIRECTION:
                    if self.__board.move_car(user_input[0], user_input[2]) is not False:
                        if self.__board.cell_content(TARGET_COORDINATE) is not None:
                            return True
                        else:
                            return None
        return None

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        value = None
        while value is None:
            print(self.__board)
            value = self.__single_turn()
        if value:
            print(SUCCESS_MESSAGE)
        if not value:
            print(FINISH_MSG)


def create_car_objects(dictionary, board):
    """
    the function check if the an element in the dictionary can be a car object and if it can be insert to the board
    :return: the list of cars in the board
    """
    for car in dictionary:
        if car in CARS_NAME:
            if CAR_LENGTH_MAX >= dictionary[car][0]:
                if dictionary[car][0] >= CAR_LENGTH_MIN:
                    if (dictionary[car][1][0], dictionary[car][1][1]) in board.cell_list():
                        if dictionary[car][2] == VERTICAL or dictionary[car][2] == HORIZONTAL:
                            car_location = (dictionary[car][1][0], dictionary[car][1][1])
                            new_car = Car(car, dictionary[car][0], car_location, dictionary[car][2])
                            board.add_car(new_car)
    return board.get_my_cars()


def main():
    """
    the main function allow the user to play the game: Rush hour , until he wins
    """
    cars = helper.load_json(sys.argv[1])
    board = Board()
    create_car_objects(cars, board)
    print(board.possible_moves())
    game = Game(board)
    game.play()


if __name__ == "__main__":
    main()
