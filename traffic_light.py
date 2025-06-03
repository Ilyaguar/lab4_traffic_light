# traffic_light.py
class TrafficLightRecord:
    def __init__(self, id, start_time, end_time, passed, waiting):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.passed = passed
        self.waiting = waiting

    def __repr__(self):
        return f"<Record #{self.id}: {self.start_time} - {self.end_time}, Cars: {self.passed}, Waiting: {self.waiting}>"
