import numpy as np

from models.Enums import PlanetaryBodyType, Resources
from models.System import System
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class PlanetaryBody(TimeSensitiveObject, UniqueObject):
    system: System
    planetary_body_type: PlanetaryBodyType
    population: np.ulong
    resources: Resources

    def initialize(self):
        super().initialize()
        self.planetary_body_type = np.random.choice(list(PlanetaryBodyType))


class Moon(PlanetaryBody):
    def __init__(self):
        super().__init__()
        self.planetary_body_type = PlanetaryBodyType.MOON


class Planet(PlanetaryBody):
    def __init__(self):
        super().__init__()
        self.planetary_body = PlanetaryBodyType.PLANET
