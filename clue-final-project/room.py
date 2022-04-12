class Room:
    def __init__(self, entrances, name, x, y):
        self.name = name
        self.entrances = entrances  # tuple of coordinate tuples
        self.players = []
        self.passage = None  # holds room object or None
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.name == other.name

    # Call this on every room with a passage AFTER they have all been initialized
    def add_passage(self, room):
        self.passage = room

    def use_passage(self, player):
        if self.passage is not None and player in self.players:
            self.players.remove(player)
            self.passage.add_player(player)
            return True
        return False

    def get_passage(self):
        return self.passage

    def has_passage(self):
        if self.passage is not None:
            return True
        return False

    def get_name(self):
        return self.name

    def add_player(self, player):
        if not self.has_player(player):
            self.players.append(player)
            return True
        return False

    def has_player(self, player):
        try:
            self.players.index(player)
            return True
        except ValueError:
            return False

    def remove_player(self, player):
        try:
            self.players.remove(player)
            return True
        except ValueError:
            return False

    def get_entrances(self):
        return self.entrances

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def add_entrance(self, entrance):
        self.entrances = self.entrances + (entrance,)
