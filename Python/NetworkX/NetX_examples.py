import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
G1.add_edges_from([(1,2), (1,3), (1,5), (1,6), (2,3), (2,4), (2,6), (3,4), (3,5), (4,5), (4,6), (5,6)])

G2 = nx.house_x_graph()   
G3 = nx.complete_bipartite_graph(3, 5)   
G4 = nx.lollipop_graph(10, 20) 

# change G to equal graph of choice
G = G3                                
# add code below to display graphs and summary info

subax1 = plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# add code below to plot the graph

plt.show()  


nx.draw(G1, pos=nx.circular_layout(G1))
#nx.draw(G1, pos=nx.random_layout(G1))
#nx.draw(G1, pos=nx.spectral_layout(G1))
#nx.draw(G1, pos=nx.spring_layout(G1))
#nx.draw(G1, pos=nx.shell_layout(G1))

#nx.draw(G2, pos=nx.circular_layout(G2))# draw G2 in spectral layout, no labels  
#nx.draw(G2, pos=nx.random_layout(G2))
#nx.draw(G2, pos=nx.spectral_layout(G2))
#nx.draw(G2, pos=nx.spring_layout(G2))
#nx.draw(G2, pos=nx.shell_layout(G2))


#nx.draw_networkx(G3, pos=nx.circular_layout(G3))   # draw G3 in shell layout, with labels 
#nx.draw_networkx(G3, pos=nx.random_layout(G3))
#nx.draw_networkx(G3, pos=nx.spectral_layout(G3))
#nx.draw_networkx(G3, pos=nx.spring_layout(G3))
#nx.draw_networkx(G3, pos=nx.shell_layout(G3))

#nx.draw(G4, pos=nx.circular_layout(G4))
#nx.draw(G4, pos=nx.random_layout(G4)) 
#nx.draw(G4, pos=nx.spectral_layout(G4)) 
#nx.draw(G4, pos=nx.spring_layout(G4)) 
#nx.draw(G4, pos=nx.shell_layout(G4)) 