# # Conditions
# import random
#
# a = random.randint(0, 1)
# if a:
#     print("Heads")
# else:
#     print("Tails")
#
#
# heads = 0
# tails = 0
# for i in range(100):
#     a = random.randint(0, 1)
#     if a:
#         heads += 1
#     else:
#         tails += 1
#
# print(f'Heads: {heads}. Tails: {tails}.')
#
#
# throws = 10000
# h = 0
# t = 0
# tie = 0
# while throws > 0:
#     a = random.randint(0, 10000)
#     if a < 5000:
#         print("Heads")
#         h += 1
#     elif a > 5000:
#         print("Tails")
#         t += 1
#     else:
#         tie += 1
#     throws -= 1
# print(h, t, tie)

import random

rand_int = random.randint(1, 6)
guess = int(input("Shoot: "))

if guess == rand_int:
    print("Bang!")
else:
    print(f"Lucky bastard! Shoot was {rand_int}.")


