#!/usr/bin/env/python
def dicts():
	#graph = {}
	i = 0
	global edge
	edge = {}
	with open("edges", "r") as f:
		for line in f:
			line = line.rstrip('\n')
			x = line.split(' ')
			if x[0] not in edge:
				edge[x[0]] = [x[1]]
			else:
				edge[x[0]].append(x[1]) 
			if x[1] not in edge:
				edge[x[1]] = []
	print edge


dicts()

def gener():
	global edge
	graph = {key: {} for key in edge.keys()}

	for key in edge:							
		forsearch = key 						
		for k in edge.keys():					
			for v in edge[k]:
				if forsearch in v:
					'''if edge[key] == []:	
						graph[k] = {forsearch : {}}
					else:'''
					graph[k][v] = graph[forsearch]
		
	#print graph
	return graph

graph = gener()
'''print graph['a']['b']['c']['f']
print graph['a']
print graph['a']['b']
print graph['a']['c']
print graph['a']['e']'''
print graph['a']['e']['d']
print graph['a']['e']['b']['c']['f']['g']
'''print graph['b']['c']
print graph['e']['d']
print graph['e']['b']'''
	