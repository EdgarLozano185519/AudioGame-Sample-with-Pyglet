class Map:
    def init_map(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.map = [[[-1 for i in range(z)] for j in range(y)] for k in range(x)]

    def is_set(self):
        if self.map[0][0][0] == -1:
            return False
        return True

    def get_tile(self, x, y, z):
        return self.map[x][y][z]

    def set_tile(self, x, y, z, type):
        self.map[x][y][z] = type

    def get_x_min(self):
        return 0

    def get_y_min(self):
        return 0

    def get_z_min(self):
        return 0

    def get_x_max(self):
        return self.x

    def get_y_max(self):
        return self.y

    def get_z_max(self):
        return self.z

    def set_map_terrain(self, type):
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    self.map[i][j][k] = type
                    #print(str(i)+str(j)+str(k)+str(self.map[i][j][k])+" ")
