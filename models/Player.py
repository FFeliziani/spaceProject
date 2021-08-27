import numpy as np

from models.Base import Base
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject
from models.User import User


class Player(TimeSensitiveObject, UniqueObject):
    user: User
    home_base: Base
    credits: np.double

    def initialize(self):
        super().initialize()
        self.credits = np.double(0)

    def create_player(self, universe):
        self.initialize()
        planetary_body = universe.pick_a_planet()
        base = Base()
        base.initialize(owner=self, location=planetary_body)
        self.home_base = base
