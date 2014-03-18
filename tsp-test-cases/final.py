import os
import sys
import networkx as nx
import numpy as np

g = nx.read_gexf(sys.argv[1]);
num = g.number_of_nodes();

states = nx.Graph();
first = sorted(g.nodes())[0];
states.add_node(first, label = first, trace = [first], dist = 0.0, heur = 0.0, fact = 0.0);
nodeId = [first];
keys = [0.0];

result_trace = [];
result_cost = 0.0;
while len(keys) > 0:
	tmpIndex = keys.index(min(keys));
	tmpId = nodeId[tmpIndex];
	nodeId.remove(tmpId);
	keys.remove(min(keys));
	tmpNode = states.node[tmpId];
	if len(tmpNode['trace']) == num:
		result_trace = tmpNode['trace'];
		result_cost = tmpNode['dist'];
		break;
	neighbors = g.nodes();
	for visited in tmpNode['trace']:
		neighbors.remove(visited);
	for v in neighbors:
		name = tmpNode['label'] + v;
		states.add_node(name);
		states.node[name]['trace'] = tmpNode['trace'] + [v];
		states.node[name]['label'] = name;
		states.node[name]['dist'] = tmpNode['dist'] + g.edge[tmpNode['trace'][-1]][v]['weight'];
		remain = neighbors;
		remain.remove(v);
		mst = nx.minimum_spanning_edges(g.subgraph(remain));
		states.node[name]['heur'] = 0.0;
		for e in mst:
			states.node[name]['heur'] += e[2]['weight'];
		states.node[name]['fact'] = states.node[name]['dist'] + states.node[name]['heur'];
		nodeId.append(name);
		keys.append(states.node[name]['fact']);
	
print "Tour: " + ' '.join(result_trace);
print "Cost:" + str(result_cost);

