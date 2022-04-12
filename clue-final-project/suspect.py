class Suspect:
    def __init__(self):
        self.name = ""
        self.image = ""

    def __int__(self, name, image):
        self.name = name
        self.image = image

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def set_name(self, name):
        self.name = name

    def set_image(self, image):
        self.image = image
        