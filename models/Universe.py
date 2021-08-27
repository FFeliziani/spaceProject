import uuid

from numpy.random import randint

from models.Cluster import Cluster
from models.Constants import Constants
from models.PlanetaryBody import PlanetaryBody
from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class Universe(TimeSensitiveObject, UniqueObject):
    clusters: list[Cluster]

    def initialize(self):
        super().initialize()
        if self.clusters is None:
            self.clusters = list[Cluster]()
        for i in randint(Constants.CLUSTER_MIN, Constants.CLUSTER_MAX):
            c = Cluster()
            c.initialize()
            self.clusters.append(c)

    def pick_a_planet(self) -> PlanetaryBody:
        selected_cluster = randint(0, len(self.clusters))
        return self.clusters[selected_cluster].pick_a_planet()
