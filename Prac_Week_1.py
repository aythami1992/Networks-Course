# %%
import os
import networkx as nx

# %%
##  Uninderect network: Edges have no direction
G=nx.Graph()
G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('D','E')
# %%
#  Direct network: Edges have direction
G=nx.DiGraph()
G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('D','E')
# %%
#Weight network: Not all relationship have the same importance.
#Weighted network is a network where edges are assigned a (tipically numerical) weight
G=nx.Graph()
G.add_edge('A','B', weight='6')
G.add_edge('B','C', weight='9')
# %%
#Signed networks: Some networks can carry information about friendship or antagonism based on conflict or disagreement
G=nx.Graph()
G.add_edge('A','B', sign='+')
G.add_edge('C','D', sign='-')
# %%
#Other edge atributtes: Edges can carry many other labels or attributes
G=nx.Graph()
G.add_edge('A','B', relation='Family')
G.add_edge('B','C', relation='Coworker')
# %%
#Multigraphs: A pair of nodes can have different types of relationships simultaneously
G=nx.MultiGraph()
G.add_edge('A','B', relation='Family')
G.add_edge('A','B', relation='Coworker')
G.add_edge('C','D', relation='Neighbor')
# %% (markdown)
##                    Video 3
# We can join diferent types of graph
G=nx.Graph()
G.add_edge('A','B',weight='6', relation='Coworker')
G.add_edge('B','C',weight='12',relation='Job')

G.get_edge_data('A','B')['weight']
# %%
##                     Video 4
# Bipartite graphs: A graph whose node can be split into two sets L and R and every edge connects an node 
#                   in L with a node in R
from networkx.algorithms import bipartite
B=nx.Graph()
B.add_nodes_from(['A','B','C','D','E'], bipartite=0)  # Label 1, set of nodes 0
B.add_nodes_from(['1','2','3','4'], bipartite=1)
B.add_edges_from([('A','1'),('B','1'),('C','1'),('D','2'),('E','3'),('E','4')])

nx.draw_networkx(B)
# %%
bipartite.is_bipartite(B)
#%%
#Projected graphs
B=nx.Graph()
B.add_edges_from([('A','1'),('B','1'),('C','1'),('D','1'),('H','1'),('B','2'),('C','2'),('D','2'),('E','2'),('G','2'),('E','3'),('F','3'),('H','3'),('J','3'),('E','4'),('I','4'),('J','4')])

X=set(['A','B','C','D','E','F','G','H','I','J'])
P=bipartite.projected_graph(B,X)
nx.draw_networkx(P)
#%%    
#                       Video 5
import numpy as np
import pandas as pd

G1=nx.Graph()
G1.add_edges_from([(0,1),
                   (0,2),
                   (0,3),
                   (0,5),
                   (1,3),
                   (1,6),
                   (3,4),
                   (4,5),
                   (4,7),
                   (5,8),
                   (8,9)])

nx.draw_networkx(G1)
# %%
Prueba1=open("G_adjlist (1).txt")
Prueba1.readlines()

# %%
G2= nx.read_adjlist('G_adjlist (1).txt', nodetype=int)
G2.edges()
# %%
#                  Adjacency Matrix
G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

G_mat
# %%
G3=nx.Graph(G_mat)
G3.edges()
# %% 
G4=nx.read_edgelist('H_adjlist (1).txt', data=[('Weight',int)])

G4.edges(data=True) 
# %%
#                     PANDAS
panda=pd.read_csv('H_adjlist (1).txt', delim_whitespace=True, header=None, names=['N1','N2','weight'])
panda
# %%
G5=nx.from_pandas_edgelist(panda,'N1', 'N2', edge_attr='weight')
G5.edges(data=True)

# %%
