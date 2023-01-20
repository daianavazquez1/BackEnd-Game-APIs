
class Personaje:
    def __init__(self,):
        self.name = None #NAME OF THE CHARACTER
        self.__energy = 100 # energy for play
        self.__hungry = 0 # hungry for the player it's grow when the player do actions out of his house
        self.__corporal_heat = 100 # it's down when it's cold in winter or places with cold like mountains
        self.__corporal_clean = 100 # it's down every moment and when you do some dirty actions
        self.happy = ((self.__coporal_heat+self.__corporal_clean)//2)-self.__hungry//2 #it's make all easy
        self.__health = 100 # it's down when you get hungry or get cold
        self.__strenght = 0 # this attribute help you to carry more items or big items
        self.__inteligence = 0 # this attribute help you when you need to resolve hard puzzles
        self.__charisma = 0 # this attribute help you when you try to talk with people or something like this
        self.__luck = 0 # this attribute help you to get more money or get rare items
        self.__green_leaves = 0 # quantity of green leaves (money of the game) that can be converter in ETH
        self.__habilities = {} # a set of habilities that help you to play the game
        self.profession = None # profession of pj

        self.__wearing = {'head': None, 'neck': None, 'body': None,
                          'jacket': None, 'legs': None, 'feets': None,
                          'hands': None, 'ear': None, 'fingers': None
                          } # wearing
        self.__inventory = {'supported_weight':50*(self.__strenght+1),"elements":{}} # inventory like a bagpack

        self.__eth_wallet = None #hash of EHT wallet to send your eth when you change the GL
        self.__green_leaves_wallet = None # GL wallet you need to generate one when you play the game
        self.posX = 0
        self.posY = 0



    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self,value):
        self.__energy = value

    @property
    def hungry(self):
        return self.__hungry

    @hungry.setter
    def hungry(self, value):
        self.__hungry = value

    @property
    def corporal_heat(self):
        return self.__corporal_heat

    @corporal_heat.setter
    def corporal_heat(self, value):
        self.__corporal_heat = value

    @property
    def happy(self):
        return self.__happy

    @happy.setter
    def happy(self,value):
        self.__happy = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def strenght(self):
        return self.__strenght

    @strenght.setter
    def strenght(self, value):
        self.__strenght = value

    @property
    def inteligence(self):
        return self.__inteligence

    @inteligence.setter
    def inteligence(self, value):
        self.__inteligence = value

    @property
    def charisma(self):
        return self.__charisma

    @charisma.setter
    def charisma(self, value):
        self.__charisma = value

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, value):
        self.__luck = value

    @property
    def green_leaves(self):
        return self.__green_leaves

    @green_leaves.setter
    def green_leaves(self, value):
        self.__green_leaves = value

    @property
    def habilities(self):
        return self.__habitilies

    @habilities.setter
    def habilities(self, key, value):
        self.__habilities[key] = value

    @property
    def wearing(self):
        return self.__wearing

    @wearing.setter
    def wearing(self, key, value):
        self.__wearing[key] = value

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, key, value):
        self.__inventory[key] = value

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, value):
        self.__posX = value

    @property
    def posY(self):
        return self.__posY

    @posY.setter
    def posY(self, value):
        self.__posY = value
