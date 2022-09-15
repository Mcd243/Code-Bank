"""Kruskal"s algorithm for finding Minimum Spanning Tree
   for Graphs lecture
   March 2020: making use of networkx
   March 2021: pylint, tuples etc
"""
import networkx as nx


# EDGES contains edges in the format (node, node, weight)
# weight could represent the length
EDGES = [(1, 2, 7), (1, 4, 5), (2, 3, 8), (2, 4, 9),
         (2, 5, 7), (3, 5, 5), (4, 5, 15), (4, 6, 6),
         (5, 6, 8), (5, 7, 9), (6, 7, 11)]

# get a set of all nodes to add to the graph
# uses two set comprehensions and the Union operator
nodes = {x[0] for x in EDGES} | {x[1] for x in EDGES}

# create a networkx graph containing the nodes
mst = nx.Graph()
mst.add_nodes_from(nodes)

# Sort the edges by weight first
EDGES.sort(key=lambda a: a[2])

while not nx.is_connected(mst):
    # remove first edge from EDGES as current
    current, EDGES = EDGES[0], EDGES[1:]
    print(f"checking edge {current}: ", end="")
    # Add edge to mst only if there is no path linking the nodes in current
    # otherwise 'forget' the edge as adding it would create a cycle
    if not nx.has_path(mst, current[0], current[1]):
        mst.add_edge(current[0], current[1], weight=current[2])
        print("ADDED to graph")
    else:
        print("NOT ADDED - would create a cycle")

print(f"No need to check {EDGES}, graph is now connected")
print(f"{mst.number_of_edges()} edges in MST:")
# print the edges. data=True includes weights
for ed in mst.edges(data=True):
    print(ed)




#https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
