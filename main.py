from levels.compute_levels import adj_reduced_level, adjusted, check_calculation, extract_tbm, level_diff, reduced_level, setStations
from read_csvfile import readFile


if __name__ == '__main__':
    data = readFile('Levelling.csv')
    stations = setStations(data)
    rise_fall = level_diff(stations)
    tbms = extract_tbm(stations)
    rl = reduced_level(rise_fall, tbms)
    corrections = check_calculation(rise_fall, rl, tbms)
    adj = adjusted(rise_fall, corrections)
    adj_reduced_level(rl, adj)
