import networkx as nx

filename = "input.txt"

G = nx.Graph()

with open(filename) as text:
    for i,row in enumerate(text):
        src, dsts = row.strip().split(":")
        for node in dsts.strip().split():
            G.add_edge(src, node)
            G.add_edge(node, src)

G.remove_edges_from(nx.minimum_edge_cut(G))

a, b = nx.connected_components(G)

print(len(a) * len(b))