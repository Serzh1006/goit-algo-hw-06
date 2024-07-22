import networkx as nx
import matplotlib.pyplot as plt

options = {
    "node_color": "gold",
    "edge_color": "blue",
    "node_size": 1500,
    "width": 2,
    "with_labels": True,
    "font_size":8,
    "font_weight":'normal'
}

G = nx.Graph()
G.add_edge('San-Diego','Chicago', weight = 85)
G.add_edge('San-Diego','Houston', weight = 100)
G.add_edge('Houston','Detroit', weight = 50)
G.add_edge('New York','Houston', weight = 130)
G.add_edge('New York','Chicago', weight = 90)
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos,**options)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("\nСтупіні вершин")
print("Detroit-> 1 | Houston-> 3 | New York-> 2 | Chicago-> 2 | San-Diego-> 2")