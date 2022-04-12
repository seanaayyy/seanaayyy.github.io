class Card:
    # initializer
    def __init__(self, name, type, image):
        self.name = name
        self.type = type
        self.image = image

    def __eq__(self, other):
        return self.name == other.name

    # getters
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_image(self):
        return self.image

    # setters
    def set_name(self, name):
        self.name = name
    def set_type(self, type):
        self.type = type
    def set_image(self, image):
        self.image = image


