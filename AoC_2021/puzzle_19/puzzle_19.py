from utils.puzzle import Puzzle
from re import match

def get_distances(scan):
    distances = []
    for i in range(len(scan) - 1):
        for j in range(i + 1, len(scan)):
            d = (scan[i][0] - scan[j][0])**2 + (scan[i][1] - scan[j][1])**2 + (scan[i][2] - scan[j][2])**2
            distances.append((i, j, d))
    return distances

if __name__ == '__main__':
    p = Puzzle()
    # data = p.load_input()
    # data = p.load_input('input_test.txt')
    data = p.load_input('input_test2.txt')
    scans = {}
    scan = 0
    scans[scan] = []
    for line in data:
        if match(r'--- scanner', line):
            continue
        elif line == '':
            scan += 1
            scans[scan] = []
        else:
            scans[scan].append( tuple(int(x) for x in line.split(',')) )

    distances = {}
    for i, s in scans.items():
        distances[i] = get_distances(s)




