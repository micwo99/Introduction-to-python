#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################


BOARD_LENGTH = 7
TARGET_COORDINATE = (3, 7)
CAR_LENGTH_MAX = 4
CAR_LENGTH_MIN = 2
VERTICAL = 0
HORIZONTAL = 1
RIGHT = 'r'
LEFT = 'l'
UP = 'u'
DOWN = 'd'


class Board:
    """
    the Board class creates a board,a target coordinate,and cars in the boards.
    the function in class Board allow to move a car in the board,give us all the coordinate of the board,
    if a car is located in a coordinate of the board or if this coordinate is empty,
    inform us which move can do the cr in the board, add a car in the board and alsoo get the list of cars in the board.
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.

        self.__length = BOARD_LENGTH
        self.__target_coordinate = TARGET_COORDINATE
        self.cars_in_board = []
        self.__board = []
        for k in range(self.__length):
            self.__board.append(["_ "] * self.__length + ["*"])

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # self.display_update()
        self.__board = []
        for k in range(self.__length):
            self.__board.append(["_ "] * self.__length + ["*"])

        self.__board[self.__target_coordinate[0]][self.__target_coordinate[1]] = 'E'
        for my_cars in self.cars_in_board:
            for m, k in my_cars.car_coordinates():
                self.__board[m][k] = my_cars.get_name() + ' '

        board_string = ''
        for i in self.__board:
            board_string += ''.join(i) + '\n'

        return board_string

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        coordinates_list = []
        for i in range(len(self.__board)):
            for k in range(len(self.__board[0]) - 1):
                coordinates_list.append((i, k))
        coordinates_list.append(TARGET_COORDINATE)
        return coordinates_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        possible_moves = []
        for my_car in self.cars_in_board:
            if my_car.get_orientation() == VERTICAL:
                if my_car.car_coordinates()[0][0] > 0:
                    next_coord = my_car.car_coordinates()[0]
                    next_coord = (next_coord[0] - 1, next_coord[1])
                    if self.cell_content(next_coord) is None:
                        possible_moves.append((my_car.get_name(), UP, "the car can move up"))
                if my_car.car_coordinates()[-1][0] < BOARD_LENGTH:
                    next_coord = my_car.car_coordinates()[-1]
                    next_coord = (next_coord[0] + 1, next_coord[1])
                    if self.cell_content(next_coord) is None:
                        possible_moves.append((my_car.get_name(), DOWN, "the car can move down"))

            if my_car.get_orientation() == HORIZONTAL:
                if my_car.car_coordinates()[0][1] > 0:
                    next_coord = my_car.car_coordinates()[0]
                    next_coord = (next_coord[0], next_coord[1] - 1)
                    if self.cell_content(next_coord) is None:
                        possible_moves.append((my_car.get_name(), LEFT, "the car can move left"))
                if my_car.car_coordinates()[-1][1] < BOARD_LENGTH:
                    next_coord = my_car.car_coordinates()[-1]
                    next_coord = (next_coord[0], next_coord[1] + 1)
                    if self.cell_content(next_coord) is None:
                        possible_moves.append((my_car.get_name(), RIGHT, "the car can move right"))

        return possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return TARGET_COORDINATE

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for my_car in self.cars_in_board:
            if coordinate in my_car.car_coordinates():
                return my_car.get_name()

        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        for car_coordinate in car.car_coordinates():
            if car_coordinate not in self.cell_list():
                return False
            if self.cell_content(car_coordinate) is not None:
                return False

        for my_car in self.cars_in_board:
            if my_car.get_name() == car.get_name():
                return False

        self.cars_in_board.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for my_cars in self.cars_in_board:
            if my_cars.get_name() == name:
                coord = my_cars.movement_requirements(movekey)[0]
                if self.cell_content(coord) is None and coord in self.cell_list():
                    return my_cars.move(movekey)
        return False

    def get_my_cars(self):
        return self.cars_in_board

