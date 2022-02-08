class InstrumentStation:
    def __init__(self):
        self.station = []
        self.level_diff = []
        self.tbm = None

    def level_difference(self):
        diff = list(zip(self.station, self.station[1:]))
        v = [self.level_diff.append(round((a-c), 3)) for a, c in diff]
        return self.level_diff
