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
    # print(tbms)
    return tbms


def level_diff(stations):
    all_level_diff = []
    for stn in stations:
        all_level_diff.append(stn.level_difference())
    # print(all_level_diff)
    return all_level_diff


def reduced_level(level_diff, tbms):
    c = 0
    initial_rl = tbms[0]
    rd_level = []
    rd_level.append(initial_rl)
    for stn_data in level_diff:
        for data in stn_data:
            rd_lv = data + rd_level[c]
            rd_level.append(round(rd_lv, 3))
            c += 1
    # print(rd_level)
    return rd_level


def check_calculation(level_diff, rl, tbms):
    correction = None
    initial_rl = rl[0]
    final_rl = rl[-1]
    true_final_rl = tbms[1]

    rise_fall_total = 0
    # check rise and fall total
    for stn_data in level_diff:
        for data in stn_data:
            rise_fall_total += data
    # print(rise_fall_total)
    # check difference btn initail and final TBM
    diff_rl = round(final_rl - initial_rl, 3)
    # print(diff_rl)
    if rise_fall_total == diff_rl:
        correction = round(true_final_rl - final_rl, 3)
    # print(f'true={true_final_rl} - obv= {final_rl} = {correction}')
    return correction


def adjusted(level_diff, correction):
    # c = 0
    # initial_rl = tbms[0]
    num_stns = len(level_diff)
    adj_rd_level = []
    adj_rd_level.append(0)
    adj_per_stn = correction/num_stns

    adj = adj_per_stn
    for stn_data in level_diff:
        for _ in stn_data:
            adj_rd_level.append(adj)
        # increase by two
        adj += adj_per_stn
    # print(adj_rd_level)
    return adj_rd_level


def adj_reduced_level(reduced_level, adjusted):
    adj_reduced_level = []
    for i, _ in enumerate(adjusted):
        adj_rl = round(reduced_level[i] + adjusted[i], 3)
        adj_reduced_level.append(adj_rl)
    print(adj_reduced_level)
