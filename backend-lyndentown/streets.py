
class Street:
    def __init__(self):
        self.posX = 0
        self.posY = 0

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, value):
        self.__posX = value

    @property
    def posY(self):
        return self.__posY

    @posX.setter
    def posY(self, value):
        self.__posY = value