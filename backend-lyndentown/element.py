
class Element:
    def __init__(self):
        self.weight = None # weight of the item
        self.name = None # name of the item
        self.quantity = None # acumulated quantity of item in one place
        self.posX = 0 # posX for the item in the map
        self.posY = 0 # posY for the item in the map
        self.order = None # if the item is in the inventory
        self.hardness = 0 # hardness of material
        self.color = None # color of material
        self.quality = None # quality of item
        self.lvl = 0 # level of the item