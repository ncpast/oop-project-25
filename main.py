import Planes
from Places import Base
from Fleet import Fleet
import People

Airline = Fleet()

Airline.NewBase(52.52, 13.405, 'Berlin')
Airline.NewBase(48.8566, 2.3522, 'Paris')
Airline.NewBase(33.3152, 44.3661, 'Baghdad')
Airline.NewBase(52.0420, 6.6114, 'Groenlo')

CargoPlane = Planes.CargoPlane('A-333', Airline.GetBase('Baghdad'), 'Boeing', '747-8F')
Airline.NewPlane(CargoPlane)

CargoCrew = People.Crew()

Passenger = People.Passenger('Richard', 'Roe')
Pilot = People.Pilot('John', 'Doe')
FlightAttendant = People.FlightAttendant('Jane', 'Doe')
CargoCrew.AssignPeople('Pilot', Pilot)
CargoCrew.AssignPeople('FlightAttendant', FlightAttendant)
CargoPlane.AssignCrew(CargoCrew)

Passenger.BoardFlight(CargoPlane) # Passengers can board flights by themselves after the crew has been assigned
FlightAttendant.Serve(Passenger)

print(CargoPlane.GetCrew().GetCrewMembers())

CargoPlane.Refuel(65344)
CargoPlane.LoadCargo(12625)
CargoPlane.Fly(Airline.GetBase('Paris'))
CargoPlane.UnloadCargo(120000)

Ultralight = Planes.Ultralight('A-402', Airline.GetBase('Berlin'), 'Makeshift', 'V1')
Airline.NewPlane(CargoPlane)

UltralightCrew = People.Crew()
UltralightCrew.AssignPeople('Pilot', Pilot)
Ultralight.AssignCrew(UltralightCrew)

Ultralight.Refuel(50)
Ultralight.Fly(Airline.GetBase('Groenlo'))
Ultralight.Refuel(50)

F16 = Planes.FighterJet('B-42', Airline.GetBase('Paris'), 'Lockheed Martin', 'F16')
F16.Intercept(CargoPlane)
F16.Engage(Ultralight)

Mechanic = People.Mechanic('Joe', 'Schmo')

Ultralight.Fly(Airline.GetBase('Berlin'))
Mechanic.Repair(Ultralight)
Ultralight.Fly(Airline.GetBase('Berlin'))