import timer, sound_pool as sp, random
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.movetimer = timer.timer()
        self.movetime = 200

    def can_move(self):
        if self.movetimer.elapsed <= self.movetime: return False
        return True

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def set_z(self, z):
        self.z = z

    def get_z(self):
        return self.z

    def get_string_coordinates(self):
        return str(self.x)+", "+str(self.y)+", "+str(self.z)

    def move(self, direction):
        self.movetimer.restart()
        if direction == 1: self.y += 1
        elif direction == 2: self.x += 1
        elif direction == 3: self.y -= 1
        elif direction == 4: self.x -= 1
        elif direction == 5: self.z += 1
        else: self.z -= 1
        sp.p.play_stationary("footsteps/wood/fs_wood_" + str(random.randint(1, 5)), False)