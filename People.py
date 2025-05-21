class Person:
    def __init__(self):
        pass
        
class Crew:
    def __init__(self):
        self.__CrewMembers = {
            "Pilots": 0,
            "FlightAttendants": 0
        }
        self.__Passengers = 0
    def AssignPeople(self, type, amount):
        if type == "FlightAttendant":
            self.__CrewMembers['FlightAttendants'] += amount
        elif type == "Pilot":
            self.__CrewMembers['Pilots'] += amount
        elif type == "Passenger":
            self.__Passengers += amount
    def TotalCrew(self):
        return self.__CrewMembers['Pilots'] + self.__CrewMembers['FlightAttendants'] + self.__Passengers
    def GetPilots(self):
        return self.__CrewMembers['Pilots']