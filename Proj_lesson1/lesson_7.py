# use unixtimestamp for working with dates
# set to check
# nest list sorting
# l = [1, 2, 3]
# l[0] = ''
# print(l)
#
#
# def f(my_list=None):
#     if my_list is None:
#         my_list = []

from sys import platform

def linux_print():
    print('Printing from Linux...')

def win32_print():
    print('Printing from Windows...')

def darwin_print():
    print('Printing from macOS...')

printer = globals()[platform + '_print']

printer()