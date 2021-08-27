from models.Universe import Universe


class SpaceProject:
    universe: Universe

    def __init__(self):
        if self.universe is None:
            self.universe = Universe()
            self.universe.initialize()
