from numpy.random import randint

from models.Constants import Constants
from models.PlanetaryBody import PlanetaryBody
from models.Sector import Sector
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class System(TimeSensitiveObject, UniqueObject):
    sector: Sector
    planetary_bodies: list[PlanetaryBody]

    def initialize(self):
        super().initialize()
        if self.planetary_bodies is None:
            self.planetary_bodies = list[PlanetaryBody]()
        for _ in randint(Constants.PLANETARY_BODY_MIN, Constants.PLANETARY_BODY_MAX):
            p = PlanetaryBody()
            p.initialize()
            self.planetary_bodies.append(p)

    def pick_a_planet(self) -> PlanetaryBody:
        selected_planetary_body = randint(0, len(self.planetary_bodies))
        return self.planetary_bodies[selected_planetary_body]
