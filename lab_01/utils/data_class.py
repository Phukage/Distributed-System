class AIR: 
    def __init__(self, time, station, temperature, moisture, light, total_rainfall, rainfall, wind_direction, pm25, pm10, co, nox, so2):
        self.time = time
        self.station = station
        self.temperature = temperature
        self.moisture = moisture
        self.light = light
        self.total_rainfall = total_rainfall
        self.rainfall = rainfall
        self.wind_direction = wind_direction
        self.pm25 = pm25
        self.pm10 = pm10
        self.co = co
        self.nox = nox
        self.so2 = so2 
    def value(self):
        return f"Time: {self.time}, Station: {self.station}, Temperature: {self.temperature}, Moisture: {self.moisture}, Light: {self.light}, Total Rainfall: {self.total_rainfall}, Rainfall: {self.rainfall}, Wind Direction: {self.wind_direction}, PM2.5: {self.pm25}, PM10: {self.pm10}, CO: {self.co}, NOx: {self.nox}, SO2: {self.so2}"
    
class EARTH: 
    def __init__(self, time, station, moisture, temperature, salinity, ph, water_root, water_leaf, water_level, voltage):
        self.time = time
        self.station = station
        self.moisture = moisture
        self.temperature = temperature
        self.salinity = salinity
        self.ph = ph
        self.water_root = water_root
        self.water_leaf = water_leaf
        self.water_level = water_level
        self.voltage = voltage 
    def value(self):
        return f"Time: {self.time}, Station: {self.station}, Moisture: {self.moisture}, Temperature: {self.temperature}, Salinity: {self.salinity}, pH: {self.ph}, Water Root: {self.water_root}, Water Leaf: {self.water_leaf}, Water Level: {self.water_level}, Voltage: {self.voltage}"
    
class WATER: 
    def __init__(self, time, station, ph, do, temperature, salinity):
        self.time = time
        self.station = station
        self.ph = ph
        self.do = do
        self.temperature = temperature
        self.salinity = salinity    
    def value(self):
        return f"Time: {self.time}, Station: {self.station}, pH: {self.ph}, DO: {self.do}, Temperature: {self.temperature}, Salinity: {self.salinity}"