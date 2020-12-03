
class Node:

	def __init__(self, key):
		self.key = key
		self.successors = []
		self.weight_successors = {}

	# return the key
	def getKey(self):
		return self.key

	# return the successors of node
	def getSuccessors(self):
		return self.successors

	# add a node successor passing the node and the weight
	def addSuccessor(self, node, weight):
		# adds if successor node not exists
		if node.getKey() not in self.weight_successors:
			self.successors.append(node)
			self.weight_successors[node.getKey()] = weight

	# returns weight of successors
	def getWeightSuccessors(self):
		return self.weight_successors


class Graph:

	def __init__(self):
		self.nodes = {} # key: key of node, value: instance of Node

	# adds a node in the graph passing a key
	def addNode(self, key_node):
		if key_node in self.nodes: # checks if the key already exists
			print('Error: key %s already exists!!' % key_node)
		else:
			node = Node(key_node) # creates a instance of Node
			self.nodes[key_node] = node # stores the node

	# connects the nodes
	def connect(self, key_source, key_destination, weight):
		# checks if the keys exists in the graph
		if key_source in self.nodes and key_destination in self.nodes:
			if key_source != key_destination: # checks if the keys are differents
				if weight > 0: # checks if the weight is positive
					self.nodes[key_source].addSuccessor(self.nodes[key_destination], weight)
				else:
					print('Error: false price!')
			else:
				print('Error: same location!!')
		else:
			print('Error: this location does not exist!!')


	# returns price
	def getWeightEdge(self, key_source, key_successor):
		if key_source in self.nodes and key_successor in self.nodes: # checks if the keys exists
			if key_source != key_successor: # checks if the keys are differents
				weight_successors = self.nodes[key_source].getWeightSuccessors()
				if key_successor in weight_successors: # checks if key_successor is a successor
					return weight_successors[key_successor] # returns the weight
				else:
					print('Error: successor not exists!!')
			else:
				print('Error: same keys!!')
		else:
			print('Error: key not exists!!')


	# returns the keys of all successors of a node
	def getSuccessors(self, key_node):
		if key_node in self.nodes:
			nodes = self.nodes[key_node].getSuccessors()
			keys_successors = [node.getKey() for node in nodes]
			return keys_successors
		else:
			print('Error: key not exists!!')


	# returns all nodes
	def getNodes(self):
		return self.nodes