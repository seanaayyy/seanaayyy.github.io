class Player:

    def __init__(self, name, is_computer, x, y, color):
        self.name = name
        # Boolean
        self.is_computer = is_computer
        self.cards = []
        self.seen_cards = []
        self.coordinates = {'x': x, 'y': y}
        self.color = color

    # getters
    def get_name(self):
        return self.name

    def get_is_computer(self):
        return self.is_computer

    def get_cards(self):
        return self.cards

    def get_seen_cards(self):
        return self.seen_cards

    def get_coordinates(self):
        return self.coordinates

    def get_x(self):
        return self.coordinates["x"]

    def get_y(self):
        return self.coordinates["y"]

    def get_color(self):
        return self.color

    # setters
    def set_name(self, name):
        self.name = name

    def set_is_computer(self, is_computer):
        self.is_computer = is_computer

    def add_card(self, card):
        self.cards.append(card)

    def add_seen_card(self, card):
        if card not in self.seen_cards:
            self.seen_cards.append(card)

    def set_x(self, x):
        self.coordinates["x"] = x

    def set_y(self, y):
        self.coordinates["y"] = y

    def set_color(self, color):
        self.color = color
