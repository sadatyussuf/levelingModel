from utilis import readFile
from utilis.record import Record


class InstrumentStation:
    def __init__(self):
        self.station = []
        self.level_diff = []
        # self._level_difference()

    def level_difference(self):
        diff = list(zip(self.station, self.station[1:]))
        v = [self.level_diff.append(round((a-c), 3)) for a, c in diff]
        # self.level_diff.append(round((a-c),3))
        # return diff


def setStations(data):

    def extractValue(record):
        values = (record.back_sight, record.inter_sight, record.fore_sight)
        # print(values)
        val = [v for v in values if v]
        return val[0]

    stn = None
    stations = []
    for record in data:
        if record.back_sight is not None:
            if record.fore_sight is not None:
                onlyFS = Record('', '',
                                str(record.fore_sight), str(record.remark))
                stn.station.append(extractValue(onlyFS))
                record.fore_sight = None
            stn = InstrumentStation()
            stations.append(stn)
        stn.station.append(extractValue(record))
    # print(stations)
    return stations


def level_diff(stations):
    for stn in stations:
        stn.level_difference()


if __name__ == '__main__':
    data = readFile('Levelling.csv')
    stations = setStations(data)
    level_diff(stations)
    print(stations)
