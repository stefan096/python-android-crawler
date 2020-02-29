# A Sample class with init method
class Pokemon:

    # init method or constructor
    def __init__(self, name="", hp=0, atk=0, defense=0, cp=0, rating=0, image_path=""):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.cp = cp
        self.rating = rating
        self.image_path = image_path

    def __str__(self):
        return str("{name: " + self.name + " hp: " + str(self.hp) + " atk: " + str(self.atk) + " def: " + str(self.defense)
                   + " cp: " + str(self.cp) + " rating: " + str(self.rating) + " image_path: " + self.image_path + "}")