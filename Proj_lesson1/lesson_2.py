apple = 5
# we can declare type
cherry: int = 10

print(cherry)
cherry = 'bubble'  # warning that we use another type, but we still can do it
print(cherry)

# if we want name or text with grammatically incorrect, we use #noqa near line
some_text = 'this tex with misttake' # noqa

num = 0.3 + 0.3 + 0.3 - 0.5  # we get 0.3999999999999999 instead of 0.4
print(num)
print(num == 0.4)  # returns False
print(round(num, 1) == 0.4)  # returns True
num_2 = 0.234 + 0.3
print(num_2)  # 0.534 - shows 3 numbers after . (the number of digits we have in longer number)

print([1, 2, 3].__len__())  # old, not used now
print(len([1, 2, 3]))

print(divmod(10, 3))  # returns result of // and % in one func
