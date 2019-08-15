from gamewindow import *
from speechsystem import *
from pyglet.window import key
from menu import *
from gametimer import *
import pyglet.app
import pyglet.resource
from sound import *
import time
import pyglet.event
from map import *
import random
from player import *


class GameLoop:
    def __init__(self):
        self.speech = SpeechSystem()
        self.window = GameWindow()

        # Dictionary of keys
        self.keys = dict(
            up=False,
            left=False,
            right=False,
            down=False,
            enter=False,
            escape=False,
            f1=False,
            f2=False,
        )

        # Timer for entire game is here
        self.game_timer = GameTimer()
        self.game_timer.start_timer()

        # Here is where menus will be initialized
        self.main_menu = Menu()

        # Game state here
        self.game_state = 0

        # Specify paths to search for resources
        pyglet.resource.path = [
            "sounds/music",
            "sounds/clicks",
            "sounds/footsteps/wood",
            "sounds/sample",
        ]
        pyglet.resource.reindex()

        # Initialize maps
        self.first_map = Map(0, 0, 0, 100, 100, 3)
        self.first_map.spawn_tile(
            0, 100, 0, 100, 0, 3, "wood"
        )  # Can be used later to play surface but as of now I'm still sticking with pyglet

        # Seed random number generator
        random.seed()

        # Init player here
        self.p = Player()

    # Function for loading all sounds
    def load_sounds(self):
        self.menu_click = Sound()
        self.menu_click.load("click.ogg", False)
        self.menu_click.loop(False)
        self.main_menu_music = Sound()
        self.main_menu_music.load("mainMenuMusic.ogg", True)
        self.main_menu_music.loop(True)
        self.fs_wood = [Sound() for x in range(10)]
        r = 0
        while r < 10:
            self.fs_wood[r].load("fs_wood_" + str(r + 1) + ".ogg", False)
            self.fs_wood[r].loop(False)
            r += 1

    def set_up_main_menu(self):
        self.main_menu.add_item("Play Game")
        self.main_menu.add_item("Exit")

    def place_window(self):
        return self.window.place_window("Test app.")

    def set_up_menus(self):
        self.set_up_main_menu()

    def main_menu_next(self):
        if self.game_state == 0:
            self.main_menu.get_next()
            self.speech.speak(self.main_menu.current_as_string())
            self.menu_click.play()

    def main_menu_previous(self):
        if self.game_state == 0:
            self.main_menu.get_previous()
            self.speech.speak(self.main_menu.current_as_string())
            self.menu_click.play()

    def main_menu_loop_music(self):
        if self.game_state == 1:
            self.main_menu_music.set_time(0)
            self.main_menu_music.set_volume(1.0)
            self.game_state = 0
        if self.game_state == 0:
            self.main_menu_music.play()
        else:
            self.main_menu_music.pause()

    def main_menu_escape(self):
        if self.game_state == 0:
            x = 0
            while x < 100 and self.main_menu_music.get_volume() >= 0:
                self.main_menu_music.set_volume(
                    self.main_menu_music.get_volume() - 0.01
                )
                time.sleep(0.01)
                x += 1
            pyglet.app.exit()

    def main_menu_enter(self):
        if self.game_state == 0:
            x = 0
            while x < 100 and self.main_menu_music.get_volume() >= 0:
                self.main_menu_music.set_volume(
                    self.main_menu_music.get_volume() - 0.01
                )
                time.sleep(0.01)
                x += 1

        # Handle the main menu choices here
        if self.main_menu.get_current() == 1:
            pyglet.app.exit()
        elif self.main_menu.get_current() == 0:
            self.game_state = 2

    def main_menu_volume_up(self):
        if self.game_state == 0 and self.main_menu_music.get_volume() <= 1.0:
            self.main_menu_music.set_volume(self.main_menu_music.get_volume() + 0.001)

    def main_menu_volume_down(self):
        if self.game_state == 0 and self.main_menu_music.get_volume() >= 0:
            self.main_menu_music.set_volume(self.main_menu_music.get_volume() - 0.001)

    def game_escape(self):
        if self.game_state == 2:
            self.game_state = 1

    def game_play_fs(self):
        t = self.first_map.get_tile_at(self.p.get_x(), self.p.get_y(), self.p.get_z())
        if t != "":
            self.fs_wood[random.randint(0, 9)].play()

    def game_player_left(self):
        if self.game_state >= 2:
            self.p.set_x(self.p.get_x() - 1)
            if self.p.get_x() < 0:
                self.p.set_x(self.p.get_x() + 1)
            else:
                self.game_play_fs()

    def game_player_right(self):
        if self.game_state >= 2:
            self.p.set_x(self.p.get_x() + 1)
            if self.p.get_x() >= self.current.get_max_x():
                self.p.set_x(self.p.get_x() - 1)
            else:
                self.game_play_fs()

    def game_player_down(self):
        if self.game_state >= 2:
            self.p.set_y(self.p.get_y() - 1)
            if self.p.get_y() < 0:
                self.p.set_y(self.p.get_y() + 1)
            else:
                self.game_play_fs()

    def game_player_up(self):
        if self.game_state >= 2:
            self.p.set_y(self.p.get_y() + 1)
            if self.p.get_y() >= self.current.get_max_y():
                self.p.set_y(self.p.get_y() - 1)
            else:
                self.game_play_fs()

    def game_current_map(self):
        if self.game_state == 2:
            self.current = self.first_map

    def speak_random(self):
        self.speech.speak("Game is loading, please wait...")

    def close(self):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys["up"] = True
        elif symbol == key.DOWN:
            self.keys["down"] = True
        if symbol == key.LEFT:
            self.keys["left"] = True
        elif symbol == key.RIGHT:
            self.keys["right"] = True
        elif symbol == key.ESCAPE:
            self.keys["escape"] = True
            return pyglet.event.EVENT_HANDLED
        elif symbol == key.ENTER:
            self.keys["enter"] = True
        elif symbol == key.F1:
            self.keys["f1"] = True
        elif symbol == key.F2:
            self.keys["f2"] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys["up"] = False
        elif symbol == key.DOWN:
            self.keys["down"] = False
        if symbol == key.LEFT:
            self.keys["left"] = False
        elif symbol == key.RIGHT:
            self.keys["right"] = False
        elif symbol == key.ESCAPE:
            self.keys["escape"] = False
            return pyglet.event.EVENT_HANDLED
        elif symbol == key.ENTER:
            self.keys["enter"] = False
        elif symbol == key.F1:
            self.keys["f1"] = False
        elif symbol == key.F2:
            self.keys["f2"] = False

    def update(self, dt):
        # First, functions to check looping
        self.main_menu_loop_music()

        # Detect current map based on state
        self.game_current_map()

        # Control all functions related to keyboard events here
        if self.keys["up"] and self.game_timer.get_time() > 200:
            self.main_menu_previous()
            self.game_player_up()
            self.game_timer.start_timer()
        elif self.keys["down"] and self.game_timer.get_time() > 200:
            self.main_menu_next()
            self.game_player_down()
            self.game_timer.start_timer()
        elif self.keys["left"] and self.game_timer.get_time() > 200:
            self.game_player_left()
            self.game_timer.start_timer()
        elif self.keys["right"] and self.game_timer.get_time() > 200:
            self.game_player_right()
            self.game_timer.start_timer()
        elif self.keys["escape"] and self.game_timer.get_time() > 200:
            self.main_menu_escape()
            self.game_escape()
            self.game_timer.start_timer()
        elif self.keys["enter"] and self.game_timer.get_time() > 100:
            self.main_menu_enter()
            self.game_timer.start_timer()
        elif self.keys["f1"] and self.game_timer.get_time() > 100:
            self.main_menu_volume_up()
            self.game_timer.start_timer()
        elif self.keys["f2"] and self.game_timer.get_time() > 100:
            self.main_menu_volume_down()
            self.game_timer.start_timer()
