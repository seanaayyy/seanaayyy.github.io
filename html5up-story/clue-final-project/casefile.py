# casefile struct has:
# suspect (card object)
# weapon (card)
# room (card)
# methods = constructor, getters, setters, make_casefile()

# import Suspect
# import Weapon
# import Room

class CaseFile():
    # initializer
    def __init__(self, suspect, weapon, room):
        self.suspect = suspect
        self.weapon = weapon
        self.room = room

    # getters
    def get_suspect(self):
        return self.suspect

    def get_weapon(self):
        return self.weapon

    def get_room(self):
        return self.room

    # setters
    def set_suspect(self, suspect):
        self.suspect = suspect

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_room(self, room):
        self.room = room
