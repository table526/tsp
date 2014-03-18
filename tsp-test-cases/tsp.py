import networkx as nx
import numpy as np

g = nx.read_gexf('r10.gexf');
num = g.number_of_nodes();
for node in g.nodes(data = True):
	node[1]['dist'] = float('inf');
	node[1]['heur'] = float('inf');
	node[1]['fact'] = float('inf');
trace = [];
cost = 0.0;

heap = np.array([]);

index = g.nodes().index('0');
tmpNode = g.nodes(data = True)[index];
tmpNode[1]['dist'] = 0.0;
mst = nx.minimum_spanning_edges(g.subgraph(g.neighbors(tmpNode[0])));
tmpNode[1]['heur'] = 0.0;
for e in list(mst):
	tmpNode[1]['heur'] += e[2]['weight'];
tmpNode[1]['fact'] = tmpNode[1]['dist'] + tmpNode[1]['heur'];
heap = np.append(heap, [tmpNode]);
heap = np.append(heap, [tmpNode]);
print heap
print heap.min()
