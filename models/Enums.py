from enum import Enum


class AccessLevel(Enum):
    FREE = "FREE"
    LEVEL_1 = "LEVEL_1"


class Resources(Enum):
    CREDITS = "CREDITS"
    HYDROGEN = "HYDROGEN"
    HELIUM = "HELIUM"
    OXYGEN = "OXYGEN"
    CARBON = "CARBON"
    SILICON = "SILICON"
    IRON = "IRON"
    TUNGSTEN = "TUNGSTEN"
    SULFUR = "SULFUR"
    LITHIUM = "LITHIUM"
    SODIUM = "SODIUM"
    POTASSIUM = "POTASSIUM"


class BaseType(Enum):
    PLANET = "PLANET"
    STATION = "STATION"
    OTHER = "OTHER"


class PlanetaryBodyType(Enum):
    PLANET = "PLANET"
    GAS_GIANT = "GAS_GIANT"
    MOON = "MOON"
