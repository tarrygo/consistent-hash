import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hashring.ring import Ring

ring = Ring()
servers = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5', '127.0.0.6', '127.0.0.7', '127.0.0.8', '127.0.0.9','127.0.0.10']
for server in servers:
	ring.addServer(server)

print("Constructed ring: ")
ring.printRing()

print("-------------------------")
print("the preference list for key")
print ring.lookupN('foo', 2)


ring.removeServer('127.0.0.1')

print("Ring after removing 127.0.0.1")
ring.printRing()

print("the preference list for key")
print ring.lookupN('foo', 2)
