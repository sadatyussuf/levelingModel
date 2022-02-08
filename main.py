from levels.compute_levels import extract_tbm, level_diff, setStations
from read_csvfile import readFile

# return data
if __name__ == '__main__':
    data = readFile('Levelling.csv')
    stations = setStations(data)
    diff = level_diff(stations)
    extract_tbm(stations)
