class Map:
    def __init__(self, minx=0, miny=0, minz=0, maxx=0, maxy=0, maxz=0):
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
            if i.in_bound(x, y, z):
                found_responses = i.tiletype
        return found_responses

    def get_zone_at(self, x, y, z):
        """Same as get_tile_at, except deals with zones. Will return Uncharted Area if nothing was found"""
        found_responses = "Uncharted Area"
        for i in self.zone_list:
            if i.in_bound(x, y, z):
                found_responses = i.zonename
        return found_responses

    def spawn_tile(self, minx=0, maxx=0, miny=0, maxy=0, minz=0, maxz=0, type=""):
        """Spawns a tile
        Params:
        minx (int): The minimum x of the tile
        maxx (int): The maximum x of the tile
        miny (int): The minimum y of the tile
        maxy (int): The maximum y of the tile
        minz (int): The minimum z of the tile
        maxz (int): The maximum z of the tile"""
        self.tile_list.append(Tile(minx, maxx, miny, maxy, minz, maxz, type))

    def spawn_zone(self, minx=0, maxx=0, miny=0, maxy=0, minz=0, maxz=0, type=""):
        """Same as spawn_tile, except it deals with zones"""
        self.zone_list.append(Zone(minx, maxx, miny, maxy, minz, maxz, type))

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


class BaseMapObj:
    """base map object
    this object is the base class from where tiles, zones and custom map objects inherit
    """

    def __init__(self, minx, maxx, miny, maxy, minz, maxz, type):
        """the BaseMapObj constructor
        params:
        minx (int) the minimum x, from where  the object starts
        maxx (int) the maximum x of the map
        miny (int) the minimum y of the map
        maxy (int) the maximum y of the map
        minz (int) the minimum z of the map
        maxz (int) the maximum z of the map
        type (str) the type of the map object, tile, zone, or whatever
        """
        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy
        self.minz = minz
        self.maxz = maxz
        self.type = type

    def in_bound(self, x, y, z):
        """verifies whether the current object covers a certain coordinate
        params:
        x (int) the x of the coordinate
        y (int) the y of the coordinate
        z (int) the z of the coordinate
        returns:
        (bool) true if the objects covers this coordinate, or false if otherwise
        """
        return (
            x >= self.minx
            and x <= self.maxx
            and y >= self.miny
            and y <= self.maxy
            and z >= self.minz
            and z <= self.maxz
        )


class Tile(BaseMapObj):
    """An internal tile class. You do not need to create any objects with this type externally"""

    def __init__(self, minx, maxx, miny, maxy, minz, maxz, type):
        super(Tile, self).__init__(minx, maxx, miny, maxy, minz, maxz, "tile")
        self.tiletype = type


class Zone(BaseMapObj):
    """an internal zone class"""

    def __init__(self, minx, maxx, miny, maxy, minz, maxz, name):
        super(Zone, self).__init__(minx, maxx, miny, maxy, minz, maxz, "zone")
        self.zonename = name
