class Fleet:
    def __init__(self):
        self.__Bases = []
        self.__Planes = []
        self.__Budget = 100 # In Millions of EUR
        self.__AvailableFuel = 100 # in litres
    def NewBase(self, Base):
        self.__Bases.append(Base)
        print(f'Base {Base.Name} has been assigned to the fleet.')
    def NewPlane(self, Plane):
        self.__Planes.append(Plane)
        print(f'Plane {Plane.ID} has been assigned to the fleet.')
    def GetBases(self):
        return self.__Bases