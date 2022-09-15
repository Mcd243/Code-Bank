
################# Reading a csv with Networkx #######################

F = nx.read_edgelist("friends.csv", delimiter=",", create_using=nx.DiGraph()) 