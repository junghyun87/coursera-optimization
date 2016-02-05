class ItemNode(object):
	def __init__(self,value,room,estimate,parent):
		self.value = value;
		self.room = room;
		self.estimate = estimate;
		self.left = None
		self.right = None
		self.parent = parent

class FindBest(object):
	def __init__(self, values, weights, items, capacity):
		self.bestNode = None
		self.values = values
		self.weights = weights
		self.items = items
		self.capacity = capacity


	def treeBuilding(self, node, depth):
		if node.room < 0:
			return
		elif depth+1 == self.items:
			#is the node best?
			if self.bestNode == None:
				self.bestNode = node
			else:
				if self.bestNode.value < node.value:
					self.bestNode = node
			return
		elif (self.bestNode != None) and (self.bestNode.value >= node.estimate):
			return
		else:
			node.left = ItemNode(node.value + self.values[depth], 
				node.room - self.weights[depth], node.estimate, node)
			node.right = ItemNode(node.value, node.room, node.estimate, node)
			self.treeBuilding(node.left,depth+1)
			self.treeBuilding(node.right,depth+1)

	def getSelectedItems(self):
		node = self.bestNode
		taken = []
		while node.parent != None:
			parent = node.parent
			if parent.left == node:
				taken.insert(0,1)
			elif parent.right == node:
				taken.insert(0,0)		
			node = node.parent
		return taken

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    #Implementing Branch and Bound
    findBest = FindBest(values, weights, items, capacity)
    rootNode = ItemNode(0,capacity,sum(values),None)
    findBest.treeBuilding(rootNode,0)
    value=findBest.bestNode.value

    #Identifing the selected items
    taken=findBest.getSelectedItems()

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'
