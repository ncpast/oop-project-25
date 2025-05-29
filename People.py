class Person:
    def __init__(self, Name, Surname):
        self.Name = Name
        self.Surname = Surname
        self.__Boarded = None
        pass
    def FullName(self):
        return f'{self.Name} {self.Surname}'
    def Board(self, Plane):
        self.__Boarded = Plane
        print(f'{self.FullName()} has boarded flight {Plane.ID}')
    def GetBoardedPlane(self):
        return self.__Boarded
    
class FlightOccupant(Person):
    def __init__(self, Name, Surname, Type):
        super().__init__(Name, Surname)
        self.__Type = Type
    def Unboard(self, Plane):
        Crew = Plane.GetCrew()
        for Person in Crew.GetCrewMembers()[f'{self.__Type}s']:
            if Person.FullName() == self.FullName():
                Crew.UnboardPassenger(self.__Type, self)
    def BoardFlight(self, Plane):
        Crew = Plane.GetCrew()
        Crew.AssignPeople(self.__Type, self)
        if self.GetBoardedPlane():
            self.Unboard(self.GetBoardedPlane())
        self.Board(Plane)

class Passenger(FlightOccupant):
    def __init__(self, Name, Surname):
        super().__init__(Name, Surname, 'Passenger')

class Pilot(FlightOccupant):
    def __init__(self, Name, Surname):
        super().__init__(Name, Surname, 'Pilot')
        
class FlightAttendant(FlightOccupant):
    def __init__(self, Name, Surname):
        super().__init__(Name, Surname, 'FlightAttendant')
    def Serve(self, Person):
        if Person.GetBoardedPlane() == self.GetBoardedPlane():
            print(f'{self.FullName()} has served {Person.FullName()} snacks')
        else:
            print(f'{self.FullName()} is not on the same flight as {Person.FullName()}')
        
class Crew:
    def __init__(self):
        self.__Crew = {
            'Passengers': [],
            'Pilots': [],
            'FlightAttendants': []
        }
    def AssignPeople(self, type, Passenger):
        if type == "FlightAttendant":
            self.__Crew['FlightAttendants'].append(Passenger)
        elif type == "Pilot":
            self.__Crew['Pilots'].append(Passenger)
        elif type == "Passenger":
            self.__Crew['Passengers'].append(Passenger)
    def BoardPassenger(self, Passenger):
        pass
    def UnboardPassenger(self, type, Passenger):
        if type == "FlightAttendant":
            self.__Crew['FlightAttendants'].remove(Passenger)
        elif type == "Pilot":
            self.__Crew['Pilots'].remove(Passenger)
        elif type == "Passenger":
            self.__Crew['Passengers'].remove(Passenger)
    def TotalCrew(self):
        return len(self.__Crew['Passengers']) + len(self.__Crew['FlightAttendants']) + len(self.__Crew['Pilots'])
    def GetPilots(self):
        return len(self.__Crew['Pilots'])
    def BoardPassenger(self, Passenger):
        self.__Crew['Passengers'].append(Passenger)
    def GetCrewMembers(self):
        return self.__Crew