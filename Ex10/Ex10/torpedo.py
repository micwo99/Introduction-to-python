TORPEDO_RADIUS = 3


class Torpedo:

    def __init__(self, location_x, location_y, speed_x, speed_y, direction, life_torpedo):
        self.__location_x = location_x
        self.__location_y = location_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__direction = direction
        self.__life_torpedo = life_torpedo

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
        return location of the torpedo
        :type: tuple
        :return:
        """
        return self.__location_x, self.__location_y

    def get_speed(self):
        """
        return the speed of the torpedo
        :return:
        """

        return self.__speed_x, self.__speed_y

    def get_direction(self):
        """
        return direction of the torpedo
        :return:
        """
        return self.__direction

    def get_radius(self):
        """
        return radius of the torpedo
        :return:
        """
        return TORPEDO_RADIUS

    def get_life_torpedo(self):
        """
        return life time of the torpedo
        :return:
        """
        return self.__life_torpedo
