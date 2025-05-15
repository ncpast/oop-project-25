import Planes
from Places import Base
from Fleet import Fleet

Airline = Fleet()

base1 = Base(52.52, 13.405, 'Berlin')  # Berlin
base2 = Base(48.8566, 2.3522, 'Paris')  # Paris
Baghdad = Base(33.3152, 44.3661, 'Baghdad')
Airline.NewBase(base1)
Airline.NewBase(base2)

print(f"Distance: {base1.DistanceTo(Baghdad)} km")
# print(Airline.GetBases())