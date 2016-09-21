# consistent-hash
An easy to use python library implementing consistant hash. INternally it uses AVL tree for storing the servers hash_key

#Usecases:
Most commonly in distributed service.
*To identify the correct server to forward the query
*To create distributed cache (https://www.akamai.com/es/es/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf)
*To partition your data

#Usage:
### Creating ring:
```
from hashring.ring import Ring
ring = Ring(no_of_replica_servers, hash_function_to_be_used)
#default value of no_of_replica_servers is 50, and hash_function_to_be_used is farmhash.hash32
```
### Adding servers to the ring
```
ring.add([<server name>])
ring.add(['127.0.0.1:9000'])
```
### Removing server:
```
ring.removeServer(['127.0.0.1:9000'])
```
### Getting server name for particular key:
```
ring.lookup('foo')
```
###Getting prefrence list for a key:
```
ring.lookupN('foo', <n>)
ring.lookupN('foo', 10)
```

### Pre order traversal of ring
```
ring.printTree()
```

# Documentation:
A good introduction for consistant hash can be found on: http://michaelnielsen.org/blog/consistent-hashing/
