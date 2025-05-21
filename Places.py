import math

class Base:
    def __init__(self, latitude : float, longitude : float, Name):
        self.Lat = ((latitude + 90) % 180 ) - 90
        self.Lon = ((longitude + 180) % 360 ) - 180 
        self.Name = Name
    def DistanceTo(self, other):
        R = 6371 # Radius of Earth in KM

        lat1 = math.radians(self.Lat)
        lon1 = math.radians(self.Lon)
        lat2 = math.radians(other.Lat)
        lon2 = math.radians(other.Lon)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = math.ceil(R * c * 100) / 100
        return distance