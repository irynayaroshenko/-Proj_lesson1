'''
1. Figure out the result of the following expressions:
a) (1 <= 1) and (1 != 1)                 ---> False
b) not (1 != 2)                          ---> False
c) ("good" != "bad") or False            ---> True
d) ("good" != "Good") and not (1 == 1)   ---> False

2. Make all of them True by adding parentheses:
a) False == not True                   ---> False == (not True)
b) True and False == True and False    ---> (True and False) == (True and False)
c) not True and "A" == "B"             ---> not (True and "A" == "B")
'''

# 3. Get a positive number from user input. Find all factors of this number.
# Example:
# If the number is 6, the factors are: 1, 2, 3, 6
# If the number is 10, the factors are: 1, 2, 5, 10

# Way 1. for-loop
num = int(input('Give me a positive number: '))
factors = [1]

for i in range(2, num + 1):
    if not num % i:
        factors.append(i)

print(f'The factors of {num} are: {", ".join(map(str, factors))}.')

# Way 2. while-loop
num = int(input('Give me a positive number: '))
start = 1
print(f'The factors of {num} are: 1 ', end='')

while start < num:
    start += 1
    if not num % start:
        print(f'{str(start)}', end=' ')

# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all 3 sides from user input.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
a, b, c = int(input('Triangle side A: ')), int(input('Triangle side B: ')), int(input('Triangle side C: '))
if a == b == c:
    print('This triangle is equilateral.')
elif a != b and b != c and a != c:
    print('This triangle is scalene.')
else:
    print('This triangle is isosceles.')

# 5. (Optional): Write a Python program to get next day of a given date. Get day, month and year from the user input.
# Expected Output:
# Input a year: 2022
# Input a month [1-12]: 8
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2022-8-24

# Way 1. if-elif-else
def is_leap(year):
    return not year % 4 and year % 100 != 0 or not year % 400


y, m, d = int(input('Input a year: ')), int(input('Input a month [1-12]: ')), int(input('Input a day [1-31]: '))

if m == 12 and d == 31: y += 1  # year count

if d == 31 and m in (1, 3, 5, 7, 8, 10, 12) or d == 30 and m in (4, 6, 9, 11):  # day count
    d = 1
elif m == 2 and d == 28 and not is_leap(y) or m == 2 and d == 29 and is_leap(y):
    d = 1
else:
    d += 1

if m == 12:  # month count
    m = 1
else:
    m += 1

print(f'The next date is [yyyy-mm-dd]: {y}-{m}-{d}.')

# Way 2. datetime module
from datetime import datetime, timedelta

date_str = input("Input date in format [yyyy-mm-dd]: ")
date = datetime.strptime(date_str, "%Y-%m-%d")
next_day = date + timedelta(days=1)
print(f'The next date is [yyyy-mm-dd]: {next_day.strftime("%Y-%m-%d")}')

# 6. Write a program that takes number as it's input and doubles that number few times in a loop.
# Number of iterations and initial number should be taken from user input.
# You should display each result on a separate line. Here is some sample output:
# Input:
# initial number: 2
# number of iterations: 5
#
# Output:
# 4
# 8
# 16
# 32
# 64
init_num = int(input('Initial number: '))
iter_n = int(input('Number of iterations: '))

while iter_n > 0:
    init_num *= 2
    print(init_num)
    iter_n -= 1

# One line while-loop
while iter_n > 0: init_num *= 2; print(init_num); iter_n -= 1

# 7. Write a program that asks the user to enter a number, and then keeps asking for numbers until the user enters 0.
# Once the user enters 0, the program should print the sum of all the numbers entered by the user.
summ = 0
while True:
    number = int(input("Give me a number: "))
    if not number:
        break
    else:
        summ += number

print(f'Sum of all entered numbers is {summ}.')
