import uuid

from models.TimeSensitiveObject import TimeSensitiveObject
from models.UniqueObject import UniqueObject


class UserGeneratedContent(TimeSensitiveObject, UniqueObject):

    def initialize(self):
        super().initialize()
        self.id = uuid.uuid4()
