from numpy.random import randint

from models.Cluster import Cluster
from models.Constants import Constants
from models.PlanetaryBody import PlanetaryBody
from models.Sector import Sector
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class Galaxy(TimeSensitiveObject, UniqueObject):
    cluster: Cluster
    sectors: list[Sector]

    def initialize(self):
        super().initialize()
        if self.sectors is None:
            self.sectors = list[Sector]()
        for i in randint(Constants.SECTOR_MIN, Constants.SECTOR_MAX):
            s = Sector()
            s.initialize()
            self.sectors.append(s)

    def pick_a_planet(self) -> PlanetaryBody:
        selected_sector = randint(0, len(self.sectors))
        return self.sectors[selected_sector].pick_a_planet()
