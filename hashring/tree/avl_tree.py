class AVLTree(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.root = None
		self.max_node = None
		self.min_node = None

	def addNode(self, key, val):
		if(self.root == None):
			self.root = Node(key, val)
			self.max_node = self.root
			self.min_node = self.root
		else:
			self.root = self.addNodeUtil(self.root, key, val)

	def addNodeUtil(self, node, key, val):
		if (node == None):
			new_node =  Node(key, val)
			if key > self.max_node.key:
				self.max_node = new_node
			elif(key < self.min_node.key):
				self.min_node = new_node
			return new_node
		else:
			if(node.key < key):
				node.right = self.addNodeUtil(node.right, key, val)
			else:
				node.left = self.addNodeUtil(node.left, key, val)

			node.height = self.updateHeight(node)
			balance = self.getBalance(node)

			#left-left case
			if(balance>1 and node.left.key > key):
				return self.rightRotate(node)
			#right right case
			if(balance < -1 and node.right.key < key):
				return self.leftRotate(node)
			#left right case
			if(balance >1 and node.left.key < key):
				node.left = self.leftRotate(node.left)
				return self.rightRotate(node)
			#right left case
			if(balance < -1 and node.right.key > key):
				node.right = self.rightRotate(node.right)
				return self.leftRotate(node)

			return node

	def removeNode(self, key):
		self.root = self.removeNodeUtil(self.root, key)
		if key == self.min_node.key :
			self.min_node = self.getMinValueNode(self.root) 
		if key == self.max_node.key :
			self.max_node = self.getMaxValueNode(self.root)	

	def removeNodeUtil(self, node, key):
		if(node == None):
			return node
		if(key < node.key):
			node.left = self.removeNodeUtil(node.left, key)
		elif(key > node.key):
			node.right = self.removeNodeUtil(node.right, key)
		else:
			if(node.left == None or node.right == None):
				temp = None
				if(node.left == None):
					temp = node.right 
				else:
					temp = node.left
				node = temp
			else:
				temp = self.getMinValueNode(node.right)
				node.updateKeyValue(temp)
				node.right = self.removeNodeUtil(node.right, temp.key)
		if(node == None):
			return node
		node.height = self.updateHeight(node)
		balance = self.getBalance(node)
		if(balance>1):
			if(self.getBalance(node.left)>=0):
				node = self.rightRotate(node)
			elif(self.getBalance(node.left)<0):
				node.left = self.leftRotate(node.left)
				node = self.rightRotate(node)
		elif(balance<-1):
			if(self.getBalance(node.right)<=0):
				node = self.leftRotate(node)
			elif(self.getBalance(node.right)>0):
				node.right = self.rightRotate(node.right)
				node = self.leftRotate(node)
		return node

	def getNext(self, key):
		if(key>=self.max_node.key):
			return self.min_node
		else:
			nextBiggerNode = None
			current = self.root
			while current !=None:
				if(current.key>key):
					nextBiggerNode = current
					current = current.left
				elif(current.key<=key):
					current = current.right
			return nextBiggerNode

	def getLowerBoundNode(self, key):
		current = self.root
		lower = None
		while current != None:
			if current.key < key:
				lower = current
				current = current.right
			elif current.key > key:
				current = current.left
			else:
				lower = current
				break
		return lower
		
	def getInorderSucc(self, node):
		if(node == None):
			return None
		if(node.right != None):
			return self.getMinValueNode(node.right)
		else:
			current = self.root
			succ = None
			while current.key != node.key:
				if(current.key > node.key):
					succ = current
					current = current.left
				elif(current.key < node.key):
					current = current.right
				else:
					break
			return succ

	#def getNextN(self, key, n):

	def getHeight(self, node):
		if(node == None):
			return 0
		return node.height

	def getBalance(self, node):
		return self.getHeight(node.left) - self.getHeight(node.right)
		
	def leftRotate(self, node):
		rightChild = node.right
		rightLeftGrandChild = rightChild.left 
		rightChild.left = node
		node.right = rightLeftGrandChild
		
		#updating heights of rotated nodes 
		node.height = self.updateHeight(node)
		rightChild.height = self.updateHeight(rightChild)
		return rightChild

	def rightRotate(self, node):
		leftChild = node.left
		leftRightGrandChild = leftChild.right
		leftChild.right = node
		node.left = leftRightGrandChild
		
		#updating heights of rotated nodes 
		node.height = self.updateHeight(node)
		leftChild.height = self.updateHeight(leftChild)
		return leftChild

	def updateHeight(self, node):
		return max(self.getHeight(node.left), self.getHeight(node.right)) +1

	def getMinValueNode(self, node):
		current = node
		if(current == None):
			return None
		else:
			while current.left != None:
				current = current.left
			return current

	def getMaxValueNode(self, node):
		current = node
		if(current == None):
			return None
		else:
			while current.right != None:
				current = current.right
			return current

	def printTreeUtil(self, node):
		if(node != None):
			print(str(node.val) + ' ' + str(node.key) + " balance: " +str(self.getBalance(node)) + " height: " + str(node.height))
			self.printTreeUtil(node.left)
			self.printTreeUtil(node.right)

	def printTree(self):
		self.printTreeUtil(self.root)

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


				