import networkx as nx
import matplotlib.pyplot as plt
from re import match, findall
import pygraphviz
import pydot
from networkx.drawing.nx_agraph import write_dot
import scipy


def load_input(filename: str):
    with open(filename, 'r') as lines:
        bags = []
        contain = []
        for line in lines:
            b, c = parse_input(line.strip())
            bags.append(b)
            contain.append(c)
    return bags, contain


def parse_input(text: str):
    bag = match(r'(\w+ \w+)', text).group()
    contains_bags = findall(r'(\d+) (\w+ \w+)', text)
    return bag, contains_bags


# bags, contain = load_input("input_7.txt")
bags, contain = load_input("input_7.txt")

G = nx.DiGraph()
G.add_nodes_from(bags)
for i, con in enumerate(contain):
    G.add_edges_from([(bags[i], c[1], {"weight": int(c[0])}) for c in con])
nx.draw(G, with_labels=True)
#
# plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
A = nx.nx_agraph.to_agraph(G)  # convert to a graphviz graph
# X1 = nx.nx_agraph.from_agraph(A)  # convert back to networkx (but as Graph)
# X2 = nx.Graph(A)  # fancy way to do conversion
# G1 = nx.Graph(X1)  # now make it a Graph

# A.write("k5.dot")  # write to dot file
# write_dot(A, "grid.dot")
A.layout('dot')
A.draw("bags_graph.svg")

# plt.show()


