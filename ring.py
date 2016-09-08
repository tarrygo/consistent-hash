class Ring(object):
	"""docstring for Ring"""
	def __init__(self, options):
		self.noOfReplica = options['noOfReplica'] || 50
		self.hashfunc = options['hashfunc'] || farmhash.hash32
		self.tree = new AVLTree()
		self.servers = {}

	def addServer(self, name):
		if hasServer(name):
			return
		else:
			addServerReplicas(name)
	def addServerReplicas(self, name):
		self.servers[name] = True
		while i < self.noOfReplica:
			key = self.hashfunc(name + i)
			self.tree.addNode(key)
			i++

	def removeServer(self, name):
		if !hasServer(name):
			return
		else:
			removeServerReplica(name)

	def removeServerReplica(self, name):
		self.servers[name] = False
		while i < self.noOfReplica:
			key = self.hashfunc(name + i)
			self.tree.removeNode(key)
			i++

	def lookup(self, key):
		hashkey = self.hashfunc(key)
		return getNext(hashkey)
	def hasServer(self, name):
		return servers[name]

		