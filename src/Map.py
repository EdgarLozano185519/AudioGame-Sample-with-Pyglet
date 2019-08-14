class Map:
    def __init__(self, minx = 0, miny = 0, minz = 0, maxx = 0, maxy = 0, maxz = 0):
     """Constructs a basic map:
     params:
     minx (int): Minimum x of the map
     miny (int): Minimum y of the map
     minz (int): Minimum Z of the map
     maxx (int): Maximum x of the map
     maxy (int): Maximum y of the map
     maxz (int): Maximum z of the map"""
     self.minx, self.miny, self.minz = minx, miny, minz
     self.maxx = maxx
     self.maxy = maxy
     self.maxz = maxz
     # Store our tiles
     self.tile_list = []
     # Store our zones
     self.zone_list = []
     # Possible sound_source list
     self.srlist = []

    def get_tile_at(self, x, y, z):
     """Returns a tile at a specified coordinates
     params:
     x (int): The x coordinate from which a tile will be retrieved
     y (int): The y coordinate from which a tile will be retrieved
     z (int): The z coordinate from which a tile will be retrieved
     Return Value:
     A blank string if a tile wasn't found or a tiletype which is within the x, y, and z coordinate"""
     found_responses = ""
     for i in self.tile_list:
      if i.in_bound(x, y, z): found_responses = i.type
     return found_responses

    def get_zone_at(self, x, y, z):
     """Same as get_tile_at, except deals with zones. Will return Uncharted Area if nothing was found"""
     found_responses = "Uncharted Area"
     for i in self.zone_list:
      if i.in_bound(x, y, z): found_responses = i.type
     return found_responses

    def spawn_tile(self, minx, maxx, miny, maxy, minz, maxz, type):
     """Spawns a tile
     Params:
     minx (int): The minimum x of the tile
     maxx (int): The maximum x of the tile
     miny (int): The minimum y of the tile
     maxy (int): The maximum y of the tile
     minz (int): The minimum z of the tile
     maxz (int): The maximum z of the tile"""
     self.tile_list.append(tile(minx, maxx, miny, maxy, minz, maxz, type))

    def spawn_zone(self, minx, maxx, miny, maxy, minz, maxz, type):
     """Same as spawn_tile, except it deals with zones"""
     self.zone_list.append(zone(minx, maxx, miny, maxy, minz, maxz, type))

    def get_min_x(self):
     """Returns the minimum x"""
     return self.minx

    def get_min_y(self):
     """Returns the minimum y"""
     return self.miny

    def get_min_z(self):
     """Returns the minimum z"""
     return self.minz

    def get_max_x(self):
     """Returns the maximum x"""
     return self.maxx

    def get_max_y(self):
     """Returns the maximum y"""
     return self.maxy

    def get_max_z(self):
     """Returns the maximum z"""
     return self.maxz

class tile:
    def __init__(self, minx, maxx, miny, maxy, minz, maxz, type):
     """An internal tile class. You do not need to create any objects with this type externally"""
     self.minx = minx
     self.maxx = maxx
     self.miny = miny
     self.maxy = maxy
     self.minz = minz
     self.maxz = maxz
     self.type = type

    def in_bound(self, x, y, z):
     """Tests whether the tile is within the specified coordinates"""
     if x >= self.minx and x <= self.maxx and y >= self.miny and y <= self.maxy and z >= self.minz and z <= self.maxz: return True
     return False

class zone:
    def __init__(self, minx, maxx, miny, maxy, minz, maxz, type):
     """An internal zone class. You do not need to create objects with this type externally"""
     # Possibly use inheritence from the tile class do to identical code
     self.minx = minx
     self.maxx = maxx
     self.miny = miny
     self.maxy = maxy
     self.minz = minz
     self.maxz = maxz
     self.type = type

    def in_bound(self, x, y, z):
     """Tests whether the given coordinates are in the zone's bounds."""
     if x >= self.minx and x <= self.maxx and y >= self.miny and y <= self.maxy and z >= self.minz and z <= self.maxz: return True
     return False
