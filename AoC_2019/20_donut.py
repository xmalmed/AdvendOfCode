INPUT = [
    '         A         ',
    '         A         ',
    '  #######.#########',
    '  #######.........#',
    '  #######.#######.#',
    '  #######.#######.#',
    '  #######.#######.#',
    '  #####  B    ###.#',
    'BC...##  C    ###.#',
    '  ##.##       ###.#',
    '  ##...DE  F  ###.#',
    '  #####    G  ###.#',
    '  #########.#####.#',
    'DE..#######...###.#',
    '  #.#########.###.#',
    'FG..#########.....#',
    '  ###########.#####',
    '             Z     ',
    '             Z     '
]
# index: -2 row, -6 column
start = (2, 9)  # 4,15 in editor

PASSAGE = INPUT.copy()
PASSAGE[start[0]][start[1]] = 0
print(PASSAGE)

def directions(position):
    d = []
    move = (position[0] - 1, position[1])  # down
    if INPUT[move[0]][move[1]] != '#':
        d.append(move)

    move = (position[0] + 1, position[1])  # up
    if INPUT[move[0]][move[1]] != '#':
        d.append(move)

    move = (position[0], position[1] - 1)  # left
    if INPUT[move[0]][move[1]] != '#':
        d.append(move)

    move = (position[0], position[1] + 1)  # right
    if INPUT[move[0]][move[1]] != '#':
        d.append(move)

    return d


print(directions((3, 9)))
