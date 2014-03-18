##########################################################################################
#	Introduction: This is a program that can solve TSP problem using A* search and MST.  #
#	Name: tsp.py			Date: 2014/03/18                                             #
#	Author: Qichen Pan		AndrewId: pqichen                                            #
##########################################################################################


import os
import sys
import networkx as nx
import numpy as np

# Read graph from argument[1]
g = nx.read_gexf(sys.argv[1]);
num = g.number_of_nodes();

# Create and initialize the state graph
states = nx.Graph();
first = sorted(g.nodes())[0];	# put the first prefix starting with the first node into state graph

##
#	state graph node structure:
#		label(str): node name;
#		trace(list): prefix of the current path
#		dist(float): sum of edges' weights in the trace
#		heur(float): weights of mst of remaining nodes
#		fact(float): dist + heur
##
states.add_node(first, label = first, trace = [first], dist = 0.0, heur = 0.0, fact = 0.0);

# nodeId and keys are two lists to mimic heap operation
nodeId = [first];	
keys = [0.0];

# result_trace and result_cost store final results
result_trace = [];
result_cost = 0.0;

# Begin iteration
while len(keys) > 0:	# while the heap is not empty
	# pop the state node with minimum fact
	tmpIndex = keys.index(min(keys));
	tmpId = nodeId[tmpIndex];
	nodeId.remove(tmpId);
	keys.remove(min(keys));
	tmpNode = states.node[tmpId];

	# judge if the trace of the state node is the result we want
	if len(tmpNode['trace']) == num:
		result_trace = tmpNode['trace'];
		# add a returning edge from the last node to the first node
		result_cost = tmpNode['dist'] + g.edge[tmpNode['trace'][-1]][tmpNode['trace'][0]]['weight'];
		break;

	# deal with all tmpNode's neighbors
	neighbors = g.nodes();
	for visited in tmpNode['trace']:	# remove all visited node
		neighbors.remove(visited);
	for v in neighbors:
		# create new state node
		name = tmpNode['label'] + v;
		states.add_node(name);
		states.node[name]['trace'] = tmpNode['trace'] + [v];
		states.node[name]['label'] = name;
		states.node[name]['dist'] = tmpNode['dist'] + g.edge[tmpNode['trace'][-1]][v]['weight'];
		remain = neighbors[:];
		remain.remove(v);
		mst = nx.minimum_spanning_edges(g.subgraph(remain));	# use weight of mst of remaining nodes as heuristic
		states.node[name]['heur'] = 0.0;
		for e in mst:
			states.node[name]['heur'] += e[2]['weight'];
		states.node[name]['fact'] = states.node[name]['dist'] + states.node[name]['heur'];
		
		# put new state node into heap
		nodeId.append(name);
		keys.append(states.node[name]['fact']);

# output final result
print "Tour: " + ' '.join(result_trace);
print "Cost: " + str(result_cost);
