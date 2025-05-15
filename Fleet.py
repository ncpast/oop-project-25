class Fleet:
    def __init__(self):
        self.__Bases = []
        self.__Planes = []
        self.__Budget = 100 # In Millions of EUR
    def NewBase(self, Base):
        self.__Bases.append(Base)
    def NewPlane(self, Plane):
        self.__Planes.append(Plane)
    def GetBases(self):
        return self.__Bases