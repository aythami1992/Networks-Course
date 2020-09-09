# %%
import pandas as pd
import networkx as nx
import matplotlib as matlib
#%%
G=nx.Graph()
G.add_edges_from([('A','K'),('A','B'),('A','C'),('B','C'),('B','K'),('C','E'),('C','F'),('D','E'),('E','F'),('E','H'),('F','G'),('J','I')])

nx.clustering(G,'B')

# %%  
#                             Global clustering coefficient
# Redefinición a las redes de dos modos (tanto binarios y ponderadas) Opsahl (2009) y una generalización a redes ponderados Opsahl y Panzarasa (2009)
# Approach 1
nx.average_clustering(G)
# Approach 2: Percentage of ''open triads''// Transitivity= (3*closed triads)/open triads
nx.transitivity(G)

#CLOSED TRIADS triads: Most nodes have high LLC ;     The high degree node has low LCC;             
#OPEN TRIADS:  Most nodes have low LLC ;      High degree node have high LCC; 
# %% 
#                                             Video 2
#Path: Is a sequence of nodes connected by an edge
#Path lenght: Numer pf steps it contains from beginning to end
G=nx.Graph()
G.add_edges_from([('A','K'),('A','B'),('A','C'),('B','C'),('B','K'),('C','E'),('C','F'),('D','E'),('E','F'),('E','H'),('F','G'),('G','I'),('J','I')])

nx.draw_networkx(G)
# %%              2. Distance measures
nx.shortest_path(G,'A','H')
#This function helps us to figure out the road shortest between 2 nodes
nx.shortest_path_length(G,'A','H')
#It tells us how many edges there are between 2 nodes
# %%   2.1 Breadth First Search
T=nx.bfs_tree(G,'A')
# With this function we going to find the differents nodes

nx.draw_networkx(T)
# %%  Average distance between every pair of nodes
nx.average_shortest_path_length(G)

# Diameter: Maximum distance between any pair of nodes
nx.diameter(G)

# %% How to summarize the distances between all pairs of nodes in a graph?

# Eccentricity of a node n is the largest distance between n and all other nodes
nx.eccentricity(G)
# This way we can get the minimum eccentricity, that is the radius.
nx.radius(G)
# Periphery of a graph is the set of nodes that have eccentricity equal to the diameter
nx.periphery(G)
#The opposite concept is the center: set of nodes that have eccentricity equals to the radius
# %%
nx.center(G)
# %%                  EJEMPLO
G=nx.karate_club_graph()
G=nx.convert_node_labels_to_integers(G,first_label=1)
# %%
nx.average_shortest_path_length(G)
# %%
nx.eccentricity(G)
# %%
nx.periphery(G)
# %%
nx.center(G)
# %%
nx.diameter(G)
# %%
T=nx.bfs_tree(G,1)
# %%                               
#                                             Video 3: Distance components
