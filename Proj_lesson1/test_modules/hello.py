# a = 5
# c = 'hello ljs!dvki lsjg'

from collections import defaultdict

d = defaultdict(int)
print(d)

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)