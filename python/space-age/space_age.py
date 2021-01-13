earth_years = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.seconds_on_earth = seconds / 31557600

    def __calc(self, divisor):
        return round(self.seconds_on_earth / divisor, 2)

    def on_earth(self):
        return round(self.seconds_on_earth, 2)

    def on_mercury(self):
        return self.__calc(earth_years["mercury"])

    def on_venus(self):
        return self.__calc(earth_years["venus"])

    def on_mars(self):
        return self.__calc(earth_years["mars"])

    def on_jupiter(self):
        return self.__calc(earth_years["jupiter"])

    def on_saturn(self):
        return self.__calc(earth_years["saturn"])

    def on_uranus(self):
        return self.__calc(earth_years["uranus"])

    def on_neptune(self):
        return self.__calc(earth_years["neptune"])
