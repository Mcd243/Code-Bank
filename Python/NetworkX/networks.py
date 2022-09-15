################### Commands for creating a graph and adding nodes and edges 
# ##(adding edges will automatically create any nodes that are referred to):
https://networkx.org/documentation/stable/tutorial.html

G = nx.Graph() 	# initialise a new graph

G.add_node("One") 	# add one node

G.add_nodes_from(["Hello", "World"]) 	# add a list of nodes

G.add_edge("Hello", "World") 	# add one edge

G.add_edges_from([("One", "Hello"), ("One", "World")]) 	# add a list of edges

H = nx.DiGraph(G) 	# create a directed graph H from G

# Commands for listing nodes and edges: 

G.nodes()

G.edges()

# Removing all nodes and edges: 

G.clear()

############################# Now display the network #########################
https://networkx.org/documentation/stable/tutorial.html#drawing-graphs

# The principle is to first DRAW the graph using networkx, then SHOW it using pyplot. 

nx.draw(G) 	# draw graph without labels or axes, default layout

nx.draw_networkx(G) 	# draw graph with labels and axes

plt.show() 	# open a graph window to show the plot

plt.savefig("graph.png") 	# save the plot as a png file



############################# import networkx ##################################

import networkx as nx

#declare a network
G = nx.Graph()

#add a node
G.add_node(1)



G.add_nodes_from([2, 3])



G.add_nodes_from([

    (4, {"color": "red"}),

    (5, {"color": "green"}),

])

# incorporate one graph into another
H = nx.path_graph(10)

G.add_nodes_from(H)


# use the graph H as a node in G.
G.add_node(H)


################################### Edges ######################################

#G can also be grown by adding one edge at a time,

G.add_edge(1, 2)

e = (2, 3)

G.add_edge(*e)  # unpack edge tuple*

# adding a list of edges,
G.add_edges_from([(1, 2), (1, 3)])

