"""Dictionaries"""
import random
d = {"one": 1, "two": 2}
d1 = {}
d2 = dict()
d3 = {}.fromkeys(range(0, 10), {"login": None, "password": None})  # generate dict
print(d3)
for x in d3:
    # print(x)
    # print(d3[x])
    d3[x].update({"login": random.randint(100, 500), "password": random.randint(100, 500)}) # in order not to have this warning
print(d3)  # see code below

d4 = {}.fromkeys(range(0, 10), {})
for x in d4:
    # print(x)
    # print(d3[x])
    d4[x].update({"login": random.randint(100, 500), "password": random.randint(100, 500)})
print(d4)

# data_new = {'ira@gmail.com': {'login': 'admin', 'password': 'admin1234'}}
# print(data_new['ira@gmail.com'])
# print(data_new['ira@gmail.com']['login'])
# print(data_new['ira@gmail.com']['login'].upper())
#
# print(data_new.items())
# print(data_new.get('ira@gmail.com'))
# print(data_new.get('iraaaa@gmail.com'))  # None
#
# print(data_new.get('ira@gmail.com').get('password'))
# data_new.update({1: "new", 2: "next"})
# print(data_new)
# data_new.update({2: "next-next"})
# print(data_new)
# print(data_new.keys())
# print(list(data_new.keys()))
# print(list(data_new.values()))
# print(list(data_new.items()))
#
#
# def login_data_check(log, pasw):
#     if log == data_new['ira@gmail.com']['login']:
#         if pasw == data_new['ira@gmail.com']['password']:
#             return 'Login successful.'
#         else:
#             return 'Incorrect password'
#     return 'Incorrect login'

# login, password = input('Enter login: '), input('Enter password: ')
# print(login_data_check(login, password))