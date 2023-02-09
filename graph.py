[11:25 AM, 2/9/2023] .: okk
[1:16 PM, 2/9/2023] Nishanth: import networkx as nx
import matplotlib.pyplot as plt

#Create a Graph
G = nx.Graph()
 
#add a node
G.add_node(1)
G.add_nodes_from ([2,3,4,5])
 
#add edges
G.add_edge(1,2)
 
e = (2,3)
G.add_edge(*e) # the * unpacks the tuple
G.add_edges_from([(1,2),(1,3),(2,4),(2,5)])
 
nx.draw(G, with_labels =True)
plt.show()
