# traffic_light.py
class TrafficLightRecord:
    def __init__(self, id, start_time, end_time, passed, waiting):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.passed = passed
        self.waiting = waiting

    def __repr__(self):
        return f"[{self.start_time} ➜ {self.end_time}] — Cars Passed: {self.passed}, Waiting: {self.waiting}"

    # Добавим сортировку в метод класса
    @staticmethod
    def sort_records(records):
        return sorted(records, key=lambda x: x.start_time)
    
    @staticmethod
    def generate(records):
        for r in records:
            yield r


