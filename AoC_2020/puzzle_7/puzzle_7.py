from time import time
imports = time()
# import networkx as nx
from networkx.algorithms.dag import ancestors
from networkx import DiGraph
# import matplotlib.pyplot as plt
from re import match, findall
# import pygraphviz
# import pydot
# from networkx.drawing.nx_agraph import write_dot


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


def count_of_subbags(bag: str ="shiny gold", total: int = 0) -> int:
    count_subbags = 0
    edges = G.out_edges(bag)

    if len(edges):
        for edge in edges:
            count_subbags += G.get_edge_data(*edge)['weight'] * count_of_subbags(edge[1])
    else:
        return 1 #count_subbags += G.get_edge_data(*edge)['weight']

    return count_subbags + 1


start = time()
# bags, contain = load_input("input_test_7.txt")
# bags, contain = load_input("input_test2_7.txt")
bags, contain = load_input("input_7.txt")

loading = time()

# G = nx.DiGraph()
G = DiGraph()
G.add_nodes_from(bags)
for i, con in enumerate(contain):
    G.add_edges_from([(bags[i], c[1], {"weight": int(c[0])}) for c in con])

# super_bags = nx.algorithms.dag.ancestors(G, "shiny gold")
super_bags = ancestors(G, "shiny gold")
# print(super_bags)
print(f'Number of super bags: {len(super_bags)}')

total_bags = count_of_subbags()
print(f'Total number bags in shiny gold: {total_bags - 1}') # -1 for shiny gold

end = time()
print(f"loading input: {loading - start}, solving: {end - loading}")
print(f"imports: {start - imports}")


# needs uncomment some of the imports
# def plot_graph(G):
#     # Write a plot to DOT format and plot graph by Graphviz.
#     A = nx.nx_agraph.to_agraph(G)  # convert to a graphviz graph
#     A.write("bags.dot")  # write to dot file
#     A.layout('dot')  # graph style
#     A.draw("bags_graph.svg")
