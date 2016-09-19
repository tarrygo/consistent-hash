import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hashring.ring import Ring
import unittest

class RingTest(unittest.TestCase):

	def setUp(self):
		self.ring  = Ring()
		self.servers = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5', '127.0.0.6', '127.0.0.7', '127.0.0.8', '127.0.0.9','127.0.0.10']
		self.sample_server = '127.0.0.1'

	def create_cluster(self):
		for server in self.servers:
			self.ring.addServer(server)

	def test_add_server(self):
		name = 'server1'
		self.ring.addServer(name)
		self.assertTrue(self.ring.hasServer(name))

	def test_add_server_2(self):
		name = 'server1'
		self.ring.addServer(name)
		self.assertFalse(self.ring.hasServer('server2'))

	def test_server_removal(self):
		self.create_cluster()
		self.ring.removeServer(self.sample_server)
		self.assertFalse(self.ring.hasServer(self.sample_server))

	def test_lookup(self):
		self.create_cluster()
		name = 'foo'
		server = self.ring.lookup(name)
		self.assertTrue(server in self.servers)

	def test_lookupN(self):
		self.create_cluster()
		name = 'foo'
		servers = self.ring.lookupN(name, 10)
		for server in servers: 
			self.assertTrue(server in self.servers)


if __name__ == '__main__':
    unittest.main()