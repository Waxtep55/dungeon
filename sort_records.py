from operator import itemgetter

def sort_records(filename):
    file = open(filename, 'r')
    data = []
    for line in file.readlines():
        if line == '':
            continue
        name, points = map(str, line.split())
        data.append([name, int(points)])
    file.close()
    data_out = sorted(data, key=itemgetter(1), reverse=True)
    file = open(filename, 'w')
    file.write('')
    file.close()
    file = open(filename, 'a')
    for player in data_out:
        file.write(player[0] + ' ' + str(player[1]) + '\n')
    file.close()