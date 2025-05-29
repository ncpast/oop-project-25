import Planes
import People
import Places

class Fleet:
    def __init__(self):
        self.__Bases = {}
        self.__Planes = []
        self.__Budget = 100 # In Millions of EUR
        self.__AvailableFuel = 100 # in litres
    def NewBase(self, lat, lon, name):
        Base = Places.Base(lat, lon, name)
        self.__Bases[name] = Base
        print(f'Base {Base.Name} has been assigned to the fleet.')
        return self.__Bases[name]
    def NewPlane(self, Plane):
        self.__Planes.append(Plane)
        print(f'Plane {Plane.ID} has been assigned to the fleet.')
    def GetBase(self, name):
        return self.__Bases[name]