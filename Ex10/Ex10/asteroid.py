import random
from screen import Screen
from math import sqrt


class Asteroid:

    def __init__(self, location_x, location_y, speed_x, speed_y, size):
        self.__location_x = location_x
        self.__location_y = location_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__size = size

    def get_location(self):
        """
        return location of  asteroid
        :type : tuple
        :return:
        """
        return self.__location_x, self.__location_y

    def get_speed(self):
        """
        return speed of asteroid
        :type: tuple
        :return:
        """
        return self.__speed_x, self.__speed_y

    def get_size(self):
        """
        return size of asteroid
        :return:
        """
        return self.__size

    def set_location(self):
        """
        set location of asteroid
        :return:
        """
        self.__location_x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        self.__location_y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)

    def new_spot(self, min_x, max_x, min_y, max_y):

        delta_x = max_x - min_x
        delta_y = max_y - min_y
        self.__location_x = min_x + (self.__location_x + self.__speed_x - min_x) % delta_x
        self.__location_y = min_y + (self.__location_y + self.__speed_y - min_y) % delta_y

    def get_radius(self):
        """
        return radius of asteroid
        :return:
        """
        asteroid_radius = self.__size * 10 - 5
        return asteroid_radius

    def has_intersection(self, obj):
        """
        return True if asteroid meet some object in the screen
        :param obj:
        :return:
        """
        distance = sqrt(
            ((obj.get_location()[0] - self.__location_x) ** 2) + ((obj.get_location()[1] - self.__location_y) ** 2))
        if distance <= self.get_radius() + obj.get_radius():
            return True
        return False
