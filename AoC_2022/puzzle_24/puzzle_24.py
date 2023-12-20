from utils.puzzle import Puzzle
import networkx as nx


def add_edges(y, x, i):
    ii = (i + 1) % C
    xp = x + 1
    xm = x - 1
    yp = y + 1
    ym = y - 1

    if (y, x, ii) in G.nodes:
        G.add_edge((y, x, i), (y, x, ii))
    if (y, xp, ii) in G.nodes:
        G.add_edge((y, x, i), (y, xp, ii))
    if (y, xm, ii) in G.nodes:
        G.add_edge((y, x, i), (y, xm, ii))
    if (yp, x, ii) in G.nodes:
        G.add_edge((y, x, i), (yp, x, ii))
    if (ym, x, ii) in G.nodes:
        G.add_edge((y, x, i), (ym, x, ii))


def add_storms(x, y, dx=0, dy=0):
    for i in range(C):
        f = (y, x, i)
        if f in frames:
            frames[f] += 1
        else:
            frames[f] = 1
        x = (x + dx) % X
        y = (y + dy) % Y


if __name__ == "__main__":
    p = Puzzle()
    # test = True
    test = False
    if test:
        data = p.load_input("input_test.txt")
        X = 6
        Y = 4
        C = 12
    else:
        data = p.load_input()
        X = 100
        Y = 35
        C = 700

    G = nx.DiGraph()
    frames = {}
    for y, l in enumerate(data[1:-1]):
        for x, ch in enumerate(l[1:-1]):
            match ch:
                case ">":
                    add_storms(x, y, dx=1)
                case "<":
                    add_storms(x, y, dx=-1)
                case "v":
                    add_storms(x, y, dy=1)
                case "^":
                    add_storms(x, y, dy=-1)
                case ".":
                    continue

    for x in range(X):
        for y in range(Y):
            for i in range(C):
                if (y, x, i) not in frames:
                    G.add_node((y, x, i))

    for i in range(C):
        G.add_node((-1, 0, i))
        G.add_node((Y, X - 1, i))

    for n in G.nodes:
        add_edges(n[0], n[1], n[2])

    G.add_node("end")
    G.add_node("start")
    for i in range(C):
        G.add_edge((Y, X - 1, i), "end")
        G.add_edge((-1, 0, i), "start")

    path1 = nx.shortest_path(G, (-1, 0, 0), "end")
    t1 = len(path1) - 2

    path2 = nx.shortest_path(G, path1[-2], "start")
    t2 = len(path2) - 2

    path3 = nx.shortest_path(G, path2[-2], "end")
    t3 = len(path3) - 2

    print(t1, t2, t3, t1 + t2 + t3)

