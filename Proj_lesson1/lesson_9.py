# get info about size of our data, how much it takes from memory
# print([1, 2, 3, 4, 5, 'stryuhi'].__sizeof__())

# IPS - iterations per second

# the most complexity has sort() method

# get value hash
# print(hash(3.14))
# print(hash('abc'))
# print(hash(42))
# print(hash(-900))
# print(hash(0))
# print(hash((42, 0)))
# print(hash([3.14, 17]))  # unhashable type: 'list'

# hash method sha256

import hashlib
m = hashlib.sha3_256()
m.update(b'Hello!')
print(m.hexdigest())
print(m)
