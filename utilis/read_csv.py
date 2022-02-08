from utilis.record import Record


def readFile(filename):
    records = []
    with open(filename) as f:
        for line in f:
            line = line.strip()

            if line[0].isalpha():
                continue
            token = [cell.strip() for cell in line.split(',')]
            records.append(Record(*token))
            # print(token)

    return records
