import Places
import Fleet

class Plane:
    def __init__(self, ID, Base, Make, Model):
        self.ID = ID
        self.__StationedIn = Base
        self.__Make = Make
        self.__Model = Model
    def Fly(self, destination: float):
        print('Hi')

class CargoPlane(Plane):
    def __init__(self):
        self.__CargoCapacity = 0
        self.__CargoVolume = 0