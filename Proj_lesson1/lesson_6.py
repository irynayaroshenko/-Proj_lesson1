"""Scope (prostir imen). global, local, non-local"""
"""try except need to be used when we know that somewhere in code we may have errors: when we work with data fron internet,
dorking with type errors (TypeError), etc.
"""
# in try - except: general word for all errors is except:
# but this is bad practice because we leave a lot of possible errors which we won't handle
# inputs, requests often go to try. Those data which we get from the third part
# several errors to pass: except (TypeError, ZeroDivisionError) as expt: print("Founded an error", expt)
# raise the exception manually
# x = -3
# if x < 0:
#     # pass
#     raise ValueError("Sorry, no number below zero")

tpl = (1, 2, 3), 4, 5
print(tpl)
print(tpl.count(4))

tp = tuple(range(10))
print(tp)

"""
Write a program that asks the user to input a string and an integer n. Then display the character at index n in
the string. You should handle an error properly and display proper error message.
"""
# st, n = input("Enter some text: "), int(input("Enter a number (int): "))
# try:
#     print(f'{n} character in text is {st[n]}.')
# except IndexError:
#     print(f"Text has less characters (can't display {n}th character).")

val_tuple = ((1, 2), (3, 4))
# 7.
def tuple_sum(tpl: tuple):
    return sum(tpl[0]) + sum(tpl[1])


print(tuple_sum(val_tuple))