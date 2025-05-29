import Places
import Fleet
import math
import People
import numpy

class Plane:
    def __init__(self, ID, Base, Make, Model):
        self.ID = ID
        self.__StationedIn = Base
        self.__LastBase = None
        self.Make = Make
        self.Model = Model
        self.__Crew = People.Crew()

        self.__Fuel = 0 # in litres
        self.__Broken = False

        self.MaxFuelCapacity = 0 # in K liters
        self.MaxCrewSize = 0
        self.AverageSpeed = 0
        self.FuelConsumption = 0
    def GetFullName(self):
        return f'{self.Make} {self.Model} {self.ID}'
    def Fly(self, Destination: float):
        if self.__Broken: 
            print(f'\n{self.GetFullName()} is broken. Flight cancelled.\n')
            return
        
        if self.__Crew.GetPilots() < 1:
            print('No pilots have been assigned!')
            return

        OldStation = self.__StationedIn.Name
        Traveled = self.__StationedIn.DistanceTo(Destination)
        TimeEstimate = math.ceil(Traveled / self.AverageSpeed * 100) / 100
        FuelNeeded = TimeEstimate * self.FuelConsumption

        if (self.__Fuel - FuelNeeded) <= 0:
            print(f'Not enough fuel! Needed (more than): {FuelNeeded}; Present: {self.__Fuel}.')
            return

        self.__Fuel -= FuelNeeded 
        self.__Fuel = math.ceil(self.__Fuel * 10) / 10

        if type(Destination) == type(self.__StationedIn):
            self.__LastBase = self.__StationedIn
            self.__StationedIn = Destination
            print(f'{self.GetFullName()} has flown {Traveled} KM from {OldStation} to {self.__StationedIn.Name} in {TimeEstimate} hours.')
            print(f'{self.GetFullName()} is now stationed in {self.__StationedIn.Name}.')
            print(f'{self.GetFullName()} fuel capacity has been decreased to {self.__Fuel} ({math.ceil(self.__Fuel / self.MaxFuelCapacity * 1000) / 10}%) litres.\n')
    def Refuel(self, amount):
        if not amount > self.MaxFuelCapacity:
            self.__Fuel = amount
            print(f'{self.GetFullName()} has been refueled to {self.__Fuel} / {self.MaxFuelCapacity} ({math.ceil(self.__Fuel / self.MaxFuelCapacity * 1000) / 1000 * 100}%) litres.\n')
        else:
            print('Given amount exceeds fuel capacity.\n')
    def GetMaxFuelCap(self):
        return self.MaxFuelCapacity
    def AssignCrew(self, Crew : People.Crew):
        if type(Crew) == type(self.__Crew):
            TotalCrew = Crew.TotalCrew()
            CrewMembers = Crew.GetCrewMembers()
            
            for Type in CrewMembers:
                for CrewMember in CrewMembers[Type]:
                    CrewMember.Board(self)

            if TotalCrew <= self.MaxCrewSize:
                self.__Crew = Crew
                print(f'A crew of {TotalCrew} has been assigned to {self.ID}.')
            else:
                print('Crew size exceeds limits.')
        else:
            print('Incorrect type.')
    def GetCrew(self):
        return self.__Crew
    def GetLastBase(self):
        if self.__LastBase:
            return self.__LastBase
        else:
            return self.__StationedIn
    def Break(self):
        self.__Broken = True
        print(f'{self.GetFullName()} is now broken.')
    def Repair(self):
        self.__Broken = False
        print(f'{self.GetFullName()} has been repaired.')
        
class CargoPlane(Plane):
    def __init__(self, ID, Base, Make, Model):
        super().__init__(ID, Base, Make, Model)
        self.MaxCargoWeight = 120000  # in kg
        self.MaxFuelCapacity = 200000 # in liters
        self.MaxCrewSize = 20
        self.AverageSpeed = 850 # in km/h
        self.FuelConsumption = 10000 # in liters per hour
        self.__LoadedCargo = 0 # in kg
    def LoadCargo(self, cargo):
        CargoToLoad = cargo + self.__LoadedCargo
        if CargoToLoad <= self.MaxCargoWeight:
            self.__LoadedCargo = CargoToLoad
            print(f'{self.GetFullName()} has been loaded with {CargoToLoad} KG.')
        else:
            print('Given cargo weight exceeds limits.')
    def UnloadCargo(self, cargo):
        cargo = numpy.clip(cargo, 0, self.__LoadedCargo)
        CargoToUnload = self.__LoadedCargo - cargo
        self.__LoadedCargo = CargoToUnload
        print(f"{self.GetFullName()} has unloaded {cargo} KG. It's current load is {CargoToUnload} KG.")

        
class Ultralight(Plane):
    def __init__(self, ID, Base, Make, Model):
        super().__init__(ID, Base, Make, Model)
        self.MaxCargoWeight = 200 
        self.MaxFuelCapacity = 50 
        self.MaxCrewSize = 2       
        self.AverageSpeed = 150    
        self.FuelConsumption = 15  

class FighterJet(Plane):
    def __init__(self, ID, Base, Make, Model):
        super().__init__(ID, Base, Make, Model)
        self.MaxFuelCapacity = 3300
        self.MaxCrewSize = 2       
        self.AverageSpeed = 1100    
        self.FuelConsumption = 3000
    def Intercept(self, target : Plane):
        print(f'{self.GetFullName()} has intercepted {target.GetFullName()}.')
        target.Fly(target.GetLastBase())
    def Engage(self, target : Plane):
        print(f'{self.GetFullName()} has engaged {target.GetFullName()}.')
        target.Break()