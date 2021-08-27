import numpy as np

from models.Enums import BaseType
from models.PlanetaryBody import PlanetaryBody
from models.Player import Player
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class Base(TimeSensitiveObject, UniqueObject):
    base_type: BaseType = BaseType.OTHER
    base_name: str
    population: np.double
    planetary_body: PlanetaryBody
    owner: Player

    def initialize(self, owner: Player, location: PlanetaryBody):
        super().initialize()
        self.owner = owner
        self.planetary_body = location


class PlanetaryBase(Base):
    base_type: BaseType = BaseType.PLANET


class OrbitalStation(Base):
    base_type: BaseType = BaseType.STATION
