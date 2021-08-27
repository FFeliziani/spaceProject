import uuid

import numpy as np

from models.Enums import AccessLevel
from models.TimeSensitiveObject import TimeSensitiveObject


class User(TimeSensitiveObject):
    id: uuid
    access_level: AccessLevel = None
    user_name: str
    email: str
    auth0_id: str

    def initialize(self):
        super().initialize()
