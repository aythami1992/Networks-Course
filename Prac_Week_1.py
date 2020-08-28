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
# %%
