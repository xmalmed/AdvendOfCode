from utils.puzzle import Puzzle
from numpy import zeros, append, fromstring

FAR = float("inf")


def get_next_nodes(node, size, node_list=[(0, 1), (1, 0)]):
    nodes = []
    for dx, dy in node_list:
        if 0 <= node[0] + dx < size and 0 <= node[1] + dy < size:
            nodes.append((node[0] + dx, node[1] + dy))
    return nodes


def extend_path(current_node, next_node, maze, path, size):
    current_path = path[current_node]
    next_path = path[next_node]
    next_distance = maze[next_node]
    if next_path > next_distance + current_path:
        path[next_node] = next_distance + current_path
        update_visited_paths(next_node, maze, path, size)


def update_visited_paths(node, maze, path, size):
    neighbours = get_next_nodes(node, size, [(-1, 0), (0, -1), (0, 1), (1, 0)])
    for neighbour in neighbours:
        if path[neighbour] == FAR:
            continue
        extend_path(node, neighbour, maze, path, size)


def run_path_search(nodes, maze, path, size):
    while nodes:
        node = nodes.pop(0)
        neighbours = get_next_nodes(node, size)
        for neighbour in neighbours:
            extend_path(node, neighbour, maze, path, size)
            if neighbour not in nodes:
                nodes.append(neighbour)


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)
    # data = p.load_input('input_test2.txt', string=True)

    size = len(data)
    maze = zeros((size, size))
    for i, line in enumerate(data):
        x = fromstring(" ".join(list(line)), sep=" ")
        maze[i, :] = x

    path = zeros((size, size)) + FAR
    path[(0, 0)] = 0
    nodes = [(0, 0)]

    run_path_search(nodes, maze, path, size)
    print(path)

    # part 2
    size2 = size * 5
    path2 = zeros((size2, size2)) + FAR
    path2[(0, 0)] = 0
    nodes = [(0, 0)]

    maze_row = maze
    for i in range(1, 5):
        new_maze = maze + 1
        new_maze[new_maze == 10] = 1
        maze = new_maze
        maze_row = append(maze_row, new_maze, 1)
    full_maze = maze_row
    for j in range(1, 5):
        new_maze = maze_row + 1
        new_maze[new_maze == 10] = 1
        maze_row = new_maze
        full_maze = append(full_maze, new_maze, 0)

    run_path_search(nodes, full_maze, path2, size2)
    print(path2)
