from datetime import datetime

from numpy.random import randint

from models.Constants import Constants
from models.Galaxy import Galaxy
from models.PlanetaryBody import PlanetaryBody
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject
from models.Universe import Universe


class Cluster(TimeSensitiveObject, UniqueObject):
    universe: Universe
    galaxies: list[Galaxy]
    created_ad: datetime

    def initialize(self):
        super().initialize()
        if self.galaxies is None:
            self.galaxies = list[Galaxy]()
        for i in randint(Constants.GALAXY_MIN, Constants.GALAXY_MAX):
            g = Galaxy()
            g.initialize()
            self.galaxies.append(g)

    def pick_a_planet(self) -> PlanetaryBody:
        selected_galaxy: int = randint(0, len(self.galaxies))
        return self.galaxies[selected_galaxy].pick_a_planet()
