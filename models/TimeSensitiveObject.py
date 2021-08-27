from datetime import datetime


class TimeSensitiveObject:
    created_at: datetime

    def initialize(self):
        self.created_at = datetime.now()
