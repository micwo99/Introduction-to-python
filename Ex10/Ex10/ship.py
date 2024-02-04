from math import cos, sin, radians
RADIUS_SHIP = 1


class Ship:

    def __init__(self, location_x, location_y, speed_x, speed_y, orientation, life):
        self.__location_x = location_x
        self.__location_y = location_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__orientation = orientation
        self.__life = life


    def get_orientation(self):
        """
        return orientation of the ship
        :return:
        """
        return self.__orientation

    def get_speed(self):
        """
        return speed of the ship
        :return:
        """
        return self.__speed_x, self.__speed_y

    def change_orientation(self, number):
        """
        change orientation of the ship
        :param number:
        :return:
        """
        self.__orientation += number

    def new_speed(self):
        """
        set the speed of the ship
        :return:
        """
        self.__speed_x = self.__speed_x + cos(radians(self.__orientation))
        self.__speed_y = self.__speed_y + sin(radians(self.__orientation))

    def new_spot(self, min_x, max_x, min_y, max_y):
        """
        the function change the location of the torpedo depending on its speed
        """
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        self.__location_x = min_x + (self.__location_x + self.__speed_x - min_x) % delta_x
        self.__location_y = min_y + (self.__location_y + self.__speed_y - min_y) % delta_y

    def get_location(self):
        """
        return location of the ship
        :type: tuple
        :return:
        """
        return self.__location_x, self.__location_y

    def get_radius(self):
        """
        return radius of the ship
        :return:
        """
        return RADIUS_SHIP

    def get_life(self):
        """
        return the number of life of the ship
        :return:
        """
        return self.__life






