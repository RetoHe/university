import time
from graph import *
from priority_queue import *

def run(graph, key_node_start, key_node_goal, verbose=False, time_sleep=0):
	if key_node_start not in graph.getNodes() or key_node_goal not in graph.getNodes():
		print('Error: key_node_start \'%s\' or key_node_goal \'%s\' not exists!!' % (key_node_start, key_node_goal))

	else:
		queue = PriorityQueue()
		keys_successors = graph.getSuccessors(key_node_start)

		# adds the keys of successors in priority queue
		for key_sucessor in keys_successors:
			weight = graph.getWeightEdge(key_node_start, key_sucessor)
			# each item of queue is a tuple (key, cumulative_cost)
			queue.insert((key_sucessor, weight), weight)


		reached_goal, cumulative_cost_goal = False, -1
		while not queue.is_empty():
			# remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
			key_current_node, cost_node = queue.remove()
			if(key_current_node == key_node_goal):
				reached_goal, cumulative_cost_goal = True, cost_node
				break

			if verbose:
				# shows a friendly message
				print('Expands node \'%s\' with cumulative cost %s ...' % (key_current_node, cost_node))
				time.sleep(time_sleep)

			# get all successors of key_current_node
			keys_successors = graph.getSuccessors(key_current_node)

			if keys_successors: # checks if contains successors
				# insert all successors of key_current_node in the queue
				for key_sucessor in keys_successors:
					cumulative_cost = graph.getWeightEdge(key_current_node, key_sucessor) + cost_node
					queue.insert((key_sucessor, cumulative_cost), cumulative_cost)

		if(reached_goal):
			print('\nReached goal! Cost: %s\n' % cumulative_cost_goal)
		else:
			print('\nUnfulfilled goal.\n')


if __name__ == "__main__":

	# build the graph...
	graph = Graph()
	graph.addNode('Frankfurt')
	graph.addNode('Würzburg')
	graph.addNode('Mannheim')
	graph.addNode('Nürnberg')
	graph.addNode('Karlsruhe')
	graph.addNode('Landeck')
	graph.addNode('Innsbruck')
	graph.addNode('Rosenheim')
	graph.addNode('Salzburg')
	graph.addNode('München')
	graph.addNode('Linz')
	graph.addNode('Passau')
	graph.addNode('Ulm')
	graph.addNode('Stuttgart')
	graph.addNode('Zürich')
	graph.addNode('Basel')
	graph.addNode('Bern')
	graph.addNode('Memmingen')
	graph.addNode('Bayreuth')
	#connect the graphs
	graph.connect('Frankfurt', 'Würzburg', 111)
	graph.connect('Frankfurt', 'Mannheim', 85)
	graph.connect('Mannheim', 'Nürnberg', 230)
	graph.connect('Mannheim', 'Frankfurt', 85)
	graph.connect('Mannheim', 'Karlsruhe', 67)
	graph.connect('Landeck', 'Innsbruck', 73)
	graph.connect('Innsbruck', 'Landeck', 73)
	graph.connect('Innsbruck', 'Rosenheim', 93)
	graph.connect('Rosenheim', 'Innsbruck', 93)
	graph.connect('Rosenheim', 'Salzburg', 81)
	graph.connect('Rosenheim', 'München', 59)
	graph.connect('Salzburg', 'Rosenheim', 81)
	graph.connect('Salzburg', 'Linz', 126)
	graph.connect('Linz', 'Salzburg', 126)
	graph.connect('Linz', 'Passau', 102)
	graph.connect('Passau', 'Linz', 102)
	graph.connect('Passau', 'Nürnberg', 220)
	graph.connect('Passau', 'München', 189)
	graph.connect('Nürnberg', 'Passau', 220)
	graph.connect('Nürnberg', 'Bayreuth', 75)
	graph.connect('Nürnberg', 'Würzburg', 104)
	graph.connect('Nürnberg', 'Ulm', 171)
	graph.connect('Nürnberg', 'München', 170)
	graph.connect('Nürnberg', 'Mannheim', 230)
	graph.connect('Ulm', 'Nürnberg', 171)
	graph.connect('Ulm', 'Stuttgart', 107)
	graph.connect('Ulm', 'Memmingen', 55)
	graph.connect('Ulm', 'München', 123)
	graph.connect('München', 'Ulm', 123)
	graph.connect('München', 'Memmingen', 115)
	graph.connect('München', 'Nürnberg', 170)
	graph.connect('München', 'Passau', 102)
	graph.connect('München', 'Rosenheim', 59)
	graph.connect('Memmingen', 'München', 115)
	graph.connect('Memmingen', 'Zürich', 184)
	graph.connect('Memmingen', 'Ulm', 55)
	graph.connect('Zürich', 'Memmingen', 184)
	graph.connect('Zürich', 'Bern', 120)
	graph.connect('Zürich', 'Basel', 85)
	graph.connect('Bern', 'Basel', 91)
	graph.connect('Bern', 'Zürich', 120)
	graph.connect('Basel', 'Bern', 91)
	graph.connect('Basel', 'Zürich', 85)
	graph.connect('Karlsruhe', 'Basel', 191)
	graph.connect('Karlsruhe', 'Mannheim', 67)
	graph.connect('Karlsruhe', 'Stuttgart', 64)
	graph.connect('Stuttgart', 'Karlsruhe', 64)
	graph.connect('Stuttgart', 'Würzburg', 140)
	graph.connect('Stuttgart', 'Ulm', 107)
	graph.connect('Bayreuth', 'Nürnberg', 75)
	graph.connect('Würzburg', 'Frankfurt', 111)
	graph.connect('Würzburg', 'Stuttgart', 140)
	graph.connect('Würzburg', 'Ulm', 183)
	graph.connect('Würzburg', 'Nürnberg', 104)

	print("Bitte gib den Startpunkt der Route ein:")
	start_node = str(input("> "))
	print("Bitte gib den Endpunkt der Route ein:")
	goal_node = str(input("> "))

	run(graph=graph, key_node_start=start_node, key_node_goal=goal_node, verbose=True, time_sleep=1)
