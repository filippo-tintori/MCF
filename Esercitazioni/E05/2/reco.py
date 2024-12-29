class Hit:
    def __init__(self, module_id, sensor_id, timestamp):
        self.module_id = int(module_id)
        self.sensor_id = int(sensor_id)
        self.timestamp = int(timestamp)

    def __lt__(self, other):

        return (self.timestamp, self.module_id, self.sensor_id) < (other.timestamp, other.module_id, other.sensor_id)

    def __sub__(self, other):
        return self.timestamp - other.timestamp # diff

class Event:
    def __init__(self, hits):
        self.hits = hits 
        self.start_time = hits[0].timestamp if hits else None
        self.end_time = hits[-1].timestamp if hits else None
        self.duration = self.end_time - self.start_time if self.start_time and self.end_time else 0
        self.num_hits = len(hits)

    def __repr__(self):
        return (f"Event(num_hits={self.num_hits}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time}, "
                f"duration={self.duration})")