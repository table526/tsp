import networkx as nx
import numpy as np

g = nx.read_gexf('r10.gexf');
num = g.number_of_nodes();
info = np.empty((4, num));
info[0][:] = np.array(g.nodes());
info[1][:] = np.inf;
info[2][:] = np.inf;
info[3][:] = np.inf;
trace = [];
cost = 0.0;

index = np.where(nodeId == '0')[0];
dist[0][index] = 0.0;
mst = nx.minimum_spanning_edges(g.subgraph(g.nodes()[0 : index] + g.nodes()[index + 1 : num]));
heur[0][index] = 0.0;
for e in list(mst):
	heur[0][index] = heur[0][index] + e[2]['weight'];

