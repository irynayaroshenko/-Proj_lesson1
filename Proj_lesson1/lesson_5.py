import datetime

# print(divmod(13, 2))
# print(13 // 2)
# print(13 % 2)

"""count = 1_000_000_0
a = []
start = datetime.datetime.now()
while count > 0:
    if count % 2 == 0:
        a.append(count)
    count -= 1
finish = datetime.datetime.now()
print(finish - start)

start = datetime.datetime.now()
while count > 0:
    a.append(count)
    count -= 2
finish = datetime.datetime.now()
print(finish - start)

start = datetime.datetime.now()
while count > 0:
    if divmod(count, 2)[1] == 0:
        a.append(count)
    count -= 1
finish = datetime.datetime.now()
print(finish - start)"""


"""counter = 1_000_000
counter2 = 0
start = datetime.datetime.now()
while counter != 0:
    # counter2 = counter
    counter -= 1

finish = datetime.datetime.now()
print(counter, counter2)
print(finish-start)

print(type(range(2)))
print(list(range(10)))


st = datetime.datetime.now()

for x in range(0, 10000, 3):
    if x != 666:
        print(x, end=" ")
    else:
        print("---")
print(datetime.datetime.now() - st)

st = datetime.datetime.now()
x = 0
while x < 10000:
    print(x, end=" ")
    x += 3
print(datetime.datetime.now() - st)"""

