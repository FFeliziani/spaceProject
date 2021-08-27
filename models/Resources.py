from numpy import ulong

from models.Enums import Resources


class Resource:
    label = "NO_LABEL"
    amount: ulong


class Hydrogen(Resource):
    label = Resources.HYDROGEN


class Helium(Resource):
    label = Resources.HELIUM


class Oxygen(Resource):
    label = Resources.OXYGEN


class Carbon(Resource):
    label = Resources.CARBON


class Silicon(Resource):
    label = Resources.SILICON


class Iron(Resource):
    label = Resources.IRON


class Tungsten(Resource):
    label = Resources.TUNGSTEN


class Sulfur(Resources):
    label = Resources.SULFUR


class Lithium(Resources):
    label = Resources.LITHIUM


class Sodium(Resources):
    label = Resources.SODIUM


class Potassium(Resources):
    label = Resources.POTASSIUM
