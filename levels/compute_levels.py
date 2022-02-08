from levels import InstrumentStation
from read_csvfile import Record


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
                # checking for lines with both back_sight and fore_sight
                onlyFS = Record('', '',
                                str(record.fore_sight), str(record.remark))
                stn.station.append(extractValue(onlyFS))
                record.fore_sight = None
            stn = InstrumentStation()
            stations.append(stn)
        stn.station.append(extractValue(record))

        if record.tbm:
            stn.tbm = record.tbm

    # print(stations)
    return stations


def extract_tbm(stations):
    tbms = []
    for stn in stations:
        if stn.tbm:
            tbms.append(stn.tbm)
    print(tbms)
    return tbms


def level_diff(stations):
    all_level_diff = []
    for stn in stations:
        all_level_diff.append(stn.level_difference())
    print(all_level_diff)
    return all_level_diff
