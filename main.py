import Planes
from Places import Base
from Fleet import Fleet
import People

Airline = Fleet()

Berlin = Base(52.52, 13.405, 'Berlin')  
Paris = Base(48.8566, 2.3522, 'Paris')  
Baghdad = Base(33.3152, 44.3661, 'Baghdad')
Groenlo = Base(52.0420, 6.6114, 'Groenlo')
Airline.NewBase(Berlin)
Airline.NewBase(Paris)
Airline.NewBase(Baghdad)
Airline.NewBase(Groenlo)

CargoPlane = Planes.CargoPlane('A-333', Baghdad, 'Boeing', '747-8F')
Airline.NewPlane(CargoPlane)

CargoCrew = People.Crew()
CargoCrew.AssignPeople('FlightAttendant', 10)
CargoCrew.AssignPeople('Pilot', 2)
CargoPlane.AssignCrew(CargoCrew)

CargoPlane.Refuel(65344)
CargoPlane.Fly(Paris)

Ultralight = Planes.Ultralight('A-402', Berlin, 'Makeshift', 'V1')
Airline.NewPlane(CargoPlane)

UltralightCrew = People.Crew()
UltralightCrew.AssignPeople('Pilot', 1)
Ultralight.AssignCrew(UltralightCrew)

Ultralight.Refuel(50)
Ultralight.Fly(Groenlo)