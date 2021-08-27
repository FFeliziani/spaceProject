import uuid


class UniqueObject:
    id: uuid

    def initialize(self):
        self.id = uuid.uuid4()
