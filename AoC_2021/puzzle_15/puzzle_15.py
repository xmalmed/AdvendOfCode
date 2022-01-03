from utils.puzzle import Puzzle
from numpy import zeros, append, fromstring


def next_nodes(size):
    steps = []
    for r in range(size):
        step = []
        for i in range(r + 1):
            step.append((i, r - i))
        steps.append(step)
    for i, s in enumerate(steps[-2::-1]):
        steps.append([(x[0] + i + 1, x[1] + i + 1) for x in s])
    return steps


def update_all_neighbours(node, maze, path, size, depth):
    depth += 1
    if depth >= 8:  # magic constant to prevent too many recursions
        return
    path_here = path[node]
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= node[0] + dx < size and 0 <= node[1] + dy < size:
            neighbour_node = (node[0] + dx, node[1] + dy)
            neighbour_path = path[neighbour_node]
            neighbour_node_distance = maze[neighbour_node]
            if neighbour_path > neighbour_node_distance + path_here:
                path[neighbour_node] = neighbour_node_distance + path_here
                update_all_neighbours(neighbour_node, maze, path, size, depth)


def extend_neighbours(node, maze, path, size):
    path_here = path[node]
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if 0 <= node[0] + dx < size and 0 <= node[1] + dy < size:
            neighbour_node = (node[0] + dx, node[1] + dy)
            neighbour_path = path[neighbour_node]
            neighbour_node_distance = maze[neighbour_node]
            if neighbour_path > neighbour_node_distance + path_here:
                path[neighbour_node] = neighbour_node_distance + path_here
                update_all_neighbours(neighbour_node, maze, path, size, 0)


def find_path(maze, path, size):
    steps = next_nodes(size)
    for step in steps:
        for node in step:
            extend_neighbours(node, maze, path, size)
    return path


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

    path = zeros((size, size)) + 9999
    path[(0, 0)] = 0

    path = find_path(maze, path, size)
    print(path)

    # ========================
    # part 2
    size *= 5
    path = zeros((size, size)) + 99999
    path[(0, 0)] = 0

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

    path = find_path(full_maze, path, size)
    print(path)
