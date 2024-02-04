#########################################
# Writer: Michael Wolhandler,micwo99, 777848979
#########################################


VERTICAL = 0
HORIZONTAL = 1
RIGHT = 'r'
LEFT = 'l'
UP = 'u'
DOWN = 'd'


class Car:
    """
    the class Car creates cars, those cars have differents attributes: a name, a length, a location, an orientation
    the functions in class Car allow us to give the coordinate of the car,to move it,
    to get the name and the orientation of the car to inform us which directions can take the car.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = [self.__location]
        if self.__orientation == VERTICAL:
            for k in range(1, self.__length):
                lst.append((self.__location[0] + k, self.__location[1]))
            return lst
        if self.__orientation == HORIZONTAL:
            for i in range(1, self.__length):
                lst.append((self.__location[0], self.__location[1] + i))
            return lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.

        if self.__orientation == VERTICAL:
            dictionary = {UP: 'the car can move up', DOWN: 'the car can move down'}
        if self.__orientation == HORIZONTAL:
            dictionary = {RIGHT: 'the car can move to the right', LEFT: 'the car can move to the left'}
        return dictionary

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        coordinate = []
        if self.__orientation == VERTICAL:
            if movekey == UP:
                coordinate.append((self.__location[0] - 1, self.__location[1]))
            if movekey == DOWN:
                last_coordinate = self.car_coordinates()[-1]
                coordinate.append((last_coordinate[0] + 1, last_coordinate[1]))
        if self.__orientation == HORIZONTAL:
            if movekey == LEFT:
                coordinate.append((self.__location[0], self.__location[1] - 1))
            if movekey == RIGHT:
                last_coordinate = self.car_coordinates()[-1]
                coordinate.append((last_coordinate[0], last_coordinate[1] + 1))
        return coordinate

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves():
            if movekey == UP:
                self.__location = (self.__location[0] - 1, self.__location[1])
            if movekey == DOWN:
                self.__location = (self.__location[0] + 1, self.__location[1])
            if movekey == RIGHT:
                self.__location = (self.__location[0], self.__location[1] + 1)
            if movekey == LEFT:
                self.__location = (self.__location[0], self.__location[1] - 1)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

    def get_orientation(self):
        """
        :return: the orientation of this car
        """
        return self.__orientation


car1 = Car("O", 2, (1, 0), 1)
print(car1.car_coordinates())
# print(car1.possible_moves())
# print(car1.movement_requirements(movekey=LEFT))
# print((car1.get_name()))
# print(car1.get_orientation())
