class AVLTree(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.root = None

	def addNode(self, key, val):
		if(self.root == None):
			self.root = Node(key, val)
		else:
			self.root = addNodeUtil(self, self.root, key, val)


	def addNodeUtil(self, node, key, val):
		if (node == None):
			return Node(key, val)
		else:
			if(node.key < key):
				node.right = addNodeUtil(node.right, key, val)
			else:
				node.left = addNodeUtil(node.left, key, val)
			node.height = updateHeight(node)
			balance = getBalance(self, node)

			#left-left case
			if(balance>1 && node.left.key > key):
				node = rightRotate(self, node)
			#right right case
			else if(balance < -1 && node.right.key < key):
				node = leftRotate(self, node)
			#left right case
			else if(balance >1 && node.left.key < key):
				node.left = leftRotate(self, node.left)
				node = rightRotate(self, node)
			#right left case
			else if(balance < -1 && node.right.key > key):
				node.right = rightRotate(self, node.right)
				node = leftRotate(self, node)
			return node

	def removeNode(self, key):
		removeNodeUtil(self.root, key)

	def removeNodeUtil(self, node, key):
		if(node == None):
			return node
		if(key < node.key):
			node.left = removeNodeUtil(node.left, key)
		else if(key > node.key):
			node.right = removeNodeUtil(node.right, key)
		else:
			if(node.left == None || node.right == None):
				temp = Node()
				if(node.left == None):
					temp = node.right 
				else if(node.right == None):
					temp = node.left
				else:
					temp = None
				node = temp
			else:
				temp = getMinValueNode(node.right)
				node.updateKeyValue(temp)
				node.right = removeNodeUtil(node.right, temp.key)
		if(node == None):
			return node
		node.height = updateHeight(node)
		balance = getBalance(node)
		if(balance>1):
			if(getBalance(node.left)>0):
				node = rightRotate(node)
			else if(getBalance(node.left)<0):
				node.left = leftRotate(node.left)
				node = rightRotate(node)
		else if(balance<-1):
			if(getBalance(node.right)<0):
				node = leftRotate(node)
			else if(getBalance(node.right)>0):
				node.right = rightRotate(node.right)
				node = leftRotate(node)

		return node


	def getNext(self, key):
		node = getLowerBoundNode(key)
		nextNode = getInorderSucc(node)
		if nextNode == None
			nextNode =  getMinValueNode(self.root)
		return nextNode
	def getLowerBoundNode(key):
		current = self.root
		while current != None:
			if current.key < key:
				lower = current
				current = current.right
			else if current.key > key
				current = current.left
			else:
				lower = current
				break
		return lower
		
	def getInorderSucc(self, node):
		if(node == None):
			return None
		if(node.right != None):
			return getMinValueNode(node.right)
		else:
			current = self.root
			succ = None
			while current.key != node.key:
				if(current.key > node.key):
					succ = current
					current = current.left
				else if(current.key < node.key):
					current = current.right
				else:
					break
			return succ
	def getNextN(self, key, n):

	def getHeight(self, node):
		if(node == None):
			return 0
		return node.height

	def getBalance(self, node):
		return getHeight(node.left) - getHeight(node.right)
	def leftRotate(self, node):
		rightChild = node.right
		rightLeftGrandChild = rightChild.left
		rightChild.left = node
		node.right = rightLeftGrandChild

		rightChild.height = updateHeight(rightChild)
		node.height = updateHeight(node)
		return rightChild

	def rightRotate(self, node):
		leftChild = node.left
		leftRightGrandChild = leftChild.right
		leftChild.right = node
		node.left = leftRightGrandChild

		leftChild.height = updateHeight(leftChild)
		node.height = updateHeight(node)
		return leftChild

	def updateHeight(self, node):
		return max(getHeight(node.left), getHeight(node.right)) +1

	def getMinValueNode(self, node):
		current = node
		if(current == None):
			return None
		else:
			while current.left != None:
				current = current.left
			return node
class Node(object):

	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.left = None
		self.right = None
		self.height = 1
	def updateKeyValue(self, node):
		self.key = node.key
		self.val = node.val


				