from screen import Screen
import sys
from ship import Ship
import random
from asteroid import Asteroid
from math import cos, sin, radians, sqrt
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
INIT_ASTEROID_SIZE = 3
ASTEROID_SIZE = [1, 2, 3]
LIFE_SHIP = 3
LOCATION_X = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
LOCATION_Y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
TITLE_LOOSE_LIFE = 'Lost life'
MESSAGE_LOOSE_LIFE = 'You lost 1 life'
ASTEROID_SPEED = [x for x in range(-4, 5) if x != 0]
X = 0
Y = 1
DEGREE_ORIENTATION = 7
INIT_SPEED = 0
INIT_ORIENTATION = 0
MAX_TORPEDOES = 10
MAX_COUNT_GAME = 200
WIN_POINT = [20, 50, 100]
GAME_OVER = 'Game over '
WIN_MESSAGE = 'You won!!!'


class GameRunner:

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        self.__screen = Screen()
        self.__ship = Ship(LOCATION_X, LOCATION_Y, INIT_SPEED, INIT_SPEED, INIT_ORIENTATION, LIFE_SHIP)
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__num_asteroid = asteroids_amount
        self.__my_asteroids = []
        self.add_asteroid()
        self.__my_torpedoes = []
        self.__my_score = 0
        self.__count_game = 0

    def load_asteroid(self):
        """
        load asteroid and add it in list of all asteroid

        :return:
        """
        for i in range(self.__num_asteroid):
            asteroid = Asteroid(random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X),
                                random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y),
                                random.choice(ASTEROID_SPEED),
                                random.choice(ASTEROID_SPEED), INIT_ASTEROID_SIZE)
            self.__my_asteroids.append(asteroid)
            self.__screen.register_asteroid(asteroid, INIT_ASTEROID_SIZE)

    def add_asteroid(self):
        """
        use the function load asteroid and check if the position is valid
        :return:
        """
        self.load_asteroid()
        self.change_location_asteroid()

    def change_location_asteroid(self):
        """
        change location of asteroid if the ship qnd the asteroids appears in the same place in the screen
        """
        for asteroid in self.__my_asteroids:
            while asteroid.get_location() == self.__ship.get_location():
                asteroid.set_location()

    def load_torpedo(self):
        """
        if the user press the space key, it will appear a torpedo in the screen
        The maximum of torpedoes that appear in the screen are 10
        """

        if self.__screen.is_space_pressed() and len(self.__my_torpedoes) < MAX_TORPEDOES:
            torpedo_speed_x = self.__ship.get_speed()[X] + 2 * cos(radians(self.__ship.get_orientation()))
            torpedo_speed_y = self.__ship.get_speed()[Y] + 2 * sin(radians(self.__ship.get_orientation()))
            torpedo_location = self.__ship.get_location()
            torpedo = Torpedo(torpedo_location[X], torpedo_location[Y], torpedo_speed_x, torpedo_speed_y,
                              self.__ship.get_orientation(), self.__count_game)
            self.__my_torpedoes.append(torpedo)
            self.__screen.register_torpedo(torpedo)

    def torpedo_loop(self):
        """
        execute all the function that we need for game, according to the part of torpedo

        """
        self.load_torpedo()
        self.move_torpedo()
        self.intersection_asteroid_torpedo()
        self.life_time_torpedo()

    def life_time_torpedo(self):
        """
        calculate the life time of the torpedo and remove it if the time is up
        """
        for torpedo in self.__my_torpedoes:
            if self.__count_game - torpedo.get_life_torpedo() >= MAX_COUNT_GAME:
                self.remove_torpedo(torpedo)

    def intersection_asteroid_torpedo(self):
        """
        execute all function related to intersections between asteroid and torpedo
        """
        torpedo_to_remove = []

        for asteroid in self.__my_asteroids:
            for torpedo in self.__my_torpedoes:
                if asteroid.has_intersection(torpedo):
                    self.remove_torpedo(torpedo)
                    torpedo_to_remove.append(id(torpedo))
                    self.add_point(asteroid)
                    self.split_asteroid(asteroid, torpedo)
                    break

        # for torpedo in set(torpedo_to_remove):
        #     for torpedo_1 in self.__my_torpedoes:
        #         if id(torpedo_1) == torpedo:
        #             self.remove_torpedo(torpedo_1)

    def remove_torpedo(self, torpedo):
        """
        re,ove torpedo of the list of torpedo and the screen
        :param torpedo:
        :return:
        """
        self.__screen.unregister_torpedo(torpedo)
        self.__my_torpedoes.remove(torpedo)

    def add_point(self, asteroid):
        """
        add point to user according to the size of torpedo
        :param asteroid:
        :return:
        """
        if asteroid.get_size() == INIT_ASTEROID_SIZE:
            self.__my_score += WIN_POINT[0]
            self.__screen.set_score(self.__my_score)
        if asteroid.get_size() == ASTEROID_SIZE[0]:
            self.__my_score += WIN_POINT[1]
            self.__screen.set_score(self.__my_score)
        if asteroid.get_size() == ASTEROID_SIZE[1]:
            self.__my_score += WIN_POINT[2]
            self.__screen.set_score(self.__my_score)

    def speed_asteroid_splited(self, asteroid, torpedo):
        """
        calculate the speed of the asteroids splited
        :param asteroid:
        :param torpedo:
        :return:
        """
        speed_x = (torpedo.get_speed()[X] + asteroid.get_speed()[X]) / (
            sqrt(asteroid.get_speed()[X] ** 2 + asteroid.get_speed()[Y] ** 2))
        speed_y = (torpedo.get_speed()[Y] + asteroid.get_speed()[Y]) / (
            sqrt(asteroid.get_speed()[X] ** 2 + asteroid.get_speed()[Y] ** 2))
        return speed_x, speed_y

    def split_asteroid(self, asteroid, torpedo):
        """
        remove asteroid and split it to two asteroid
        :param asteroid:
        :param torpedo:
        :return:
        """

        self.remove_asteroid(asteroid)
        if asteroid.get_size() > 1:
            asteroid1 = Asteroid(asteroid.get_location()[X], asteroid.get_location()[Y],
                                 self.speed_asteroid_splited(asteroid, torpedo)[X],
                                 self.speed_asteroid_splited(asteroid, torpedo)[Y], asteroid.get_size() - 1)
            asteroid2 = Asteroid(asteroid.get_location()[X], asteroid.get_location()[Y],
                                 -self.speed_asteroid_splited(asteroid, torpedo)[X],
                                 -self.speed_asteroid_splited(asteroid, torpedo)[Y], asteroid.get_size() - 1)
            self.__my_asteroids.append(asteroid1)
            self.__screen.register_asteroid(asteroid1, asteroid1.get_size())
            self.__my_asteroids.append(asteroid2)
            self.__screen.register_asteroid(asteroid2, asteroid2.get_size())

    def move_torpedo(self):
        """
        move torpedo on the screen
        :return:
        """
        for torpedo in self.__my_torpedoes:
            torpedo_location = torpedo.get_location()
            torpedo_direction = torpedo.get_direction()
            self.__screen.draw_torpedo(torpedo, torpedo_location[X], torpedo_location[Y], torpedo_direction)
            torpedo.new_spot(self.__screen.SCREEN_MIN_X, self.__screen.SCREEN_MAX_X,
                             self.__screen.SCREEN_MIN_Y, self.__screen.SCREEN_MAX_Y)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        the function contains all the function to allow the game to run
        :return:
        """
        self.__count_game += 1
        self.ship_loop()
        self.asteroid_loop()
        self.torpedo_loop()
        if self.__ship.get_life() == 0 or \
                self.__screen.should_end():
            self.end_of_game()
        if len(self.__my_asteroids) == 0:
            self.win_game()

    def win_game(self):
        self.__screen.show_message(WIN_MESSAGE,WIN_MESSAGE)
        self.__screen.end_game()
        sys.exit()



    def end_of_game(self):
        """
        the function exit the user of the game
        """
        self.__screen.show_message(GAME_OVER, GAME_OVER)
        self.__screen.end_game()
        sys.exit()

    def asteroid_loop(self):
        """
        the function draws the asteroids in the screen and check if there is intersection with the ship
        if yes the game remove one life to the ship and makes disappear the asteroid
        """
        for asteroid in self.__my_asteroids:
            location_x, location_y = asteroid.get_location()
            self.__screen.draw_asteroid(asteroid, location_x, location_y)
            asteroid.new_spot(self.__screen.SCREEN_MIN_X, self.__screen.SCREEN_MAX_X,
                              self.__screen.SCREEN_MIN_Y, self.__screen.SCREEN_MAX_Y)

            if asteroid.has_intersection(self.__ship):
                self.__screen.show_message(TITLE_LOOSE_LIFE, MESSAGE_LOOSE_LIFE)
                self.__screen.remove_life()
                self.__ship = Ship(location_x, location_y, self.__ship.get_speed()[X], self.__ship.get_speed()[Y],
                                   self.__ship.get_orientation(), self.__ship.get_life() - 1)
                self.remove_asteroid(asteroid)

    def remove_asteroid(self, asteroid):
        """
        the function remove the asteroid of the screen
        """
        self.__my_asteroids.remove(asteroid)
        self.__screen.unregister_asteroid(asteroid)

    def ship_orientation(self):
        """
        the function change the direction and the place of the ship if the user press the up/left/right key
        """
        if self.__screen.is_left_pressed():
            self.__ship.change_orientation(DEGREE_ORIENTATION)
        if self.__screen.is_right_pressed():
            self.__ship.change_orientation(-DEGREE_ORIENTATION)
        if self.__screen.is_up_pressed():
            self.__ship.new_speed()
        self.__ship.new_spot(self.__screen.SCREEN_MIN_X, self.__screen.SCREEN_MAX_X,
                             self.__screen.SCREEN_MIN_Y, self.__screen.SCREEN_MAX_Y)

    def ship_loop(self):
        """
        the function draws the ship into the screen and allow to move it
        """
        location_x, location_y = self.__ship.get_location()
        orientation = self.__ship.get_orientation()
        self.__screen.draw_ship(location_x, location_y, orientation)
        self.ship_orientation()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
