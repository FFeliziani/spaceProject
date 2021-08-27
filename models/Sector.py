from numpy.random import randint

from models.Constants import Constants
from models.Galaxy import Galaxy
from models.PlanetaryBody import PlanetaryBody
from models.System import System
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class Sector(TimeSensitiveObject, UniqueObject):
    galaxy: Galaxy
    systems: list[System]

    def initialize(self):
        super().initialize()
        if self.systems is None:
            self.systems = list[System]()
        for i in randint(Constants.SYSTEM_MIN, Constants.SYSTEM_MAX):
            s = System()
            s.initialize()
            self.systems.append(s)

    def pick_a_planet(self) -> PlanetaryBody:
        selected_system = randint(0, len(self.systems))
        return self.systems[selected_system].pick_a_planet()
