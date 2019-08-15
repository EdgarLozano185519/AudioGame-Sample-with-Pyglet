import math


class Enemy:
    def __init__():
        self.x = 0
        self.y = 0
        self.z = 0
        self.max_distance = 0
        self.step_volume = 0

    def spawn(self):
        self.spawn = 1

    # Defines the minimum distance for an enemy to spawn
    def define_distance(self, distance):
        self.max_distance = distance

    def calculate_step_volume(self):
        self.step_volume = 1.0 / self.max_distance

    def calculate_distance(self, x, y, z):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2)
