import farmhash
from tree.avl_tree import AVLTree

class Ring(object):
	"""docstring for Ring"""
	def __init__(self, noOfReplica=50, hashfunc=farmhash.hash32, options={}):
		self.noOfReplica = noOfReplica
		self.hashfunc = hashfunc
		self.tree = AVLTree()
		self.servers = {}

	def addServer(self, name):
		if self.hasServer(name):
			return
		else:
			self.addServerReplicas(name)

	def addServerReplicas(self, name):
		self.servers[name] = True
		for i in range(self.noOfReplica):
			key = self.hashfunc(name + str(i))
			self.tree.addNode(key, name)

	def removeServer(self, name):
		if self.hasServer(name) == False:
			return
		else:
			self.removeServerReplica(name)
			del self.servers[name]

	def removeServerReplica(self, name):
		self.servers[name] = False
		for i in range(self.noOfReplica):
			key = self.hashfunc(name + str(i))
			self.tree.removeNode(key)

	def lookup(self, key):
		hashkey = self.hashfunc(key)
		return self.tree.getNext(hashkey).val
		#return self.tree.getNext(hashkey)

	def lookupN(self, key, n):
		starting_hashkey = self.hashfunc(key)
		server_list = []
		cur_hashkey = starting_hashkey
		for i in range(n):
			node = self.tree.getNext(cur_hashkey)
			server_list.append(node.val)
			cur_hashkey = node.key
		return server_list

	def hasServer(self, name):
		if self.servers.has_key(name) :
			return True
		else:
			return False

	def printRing(self):
		self.tree.printTree()

		