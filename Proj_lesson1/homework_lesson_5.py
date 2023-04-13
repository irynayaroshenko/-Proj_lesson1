"""
Write a program that calculate Fibonacci series. The Fibonacci series is a series of numbers in which each number
is the sum of the two preceding numbers. The first two numbers are 1 and 1. The third number is 1 + 1 = 2,
the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
"""
def fibonacci(n):
    if n == 1:
        return 1
    n1, n2 = 1, 1
    for _ in range(n - 2):
        n1, n2 = n2, n1 + n2
    return n2


number = int(input("Calculate Fibonacci series for (int): "))
print(f'Fibonacci sequence for {number} is {fibonacci(number)}.')

"""
1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
"""
for i in range(100):
    if not i % 3:
        print(i, end=' ')  # add print() in the end if you run all the code (not each task separately)

"""
2. Get a number from user input and iterate from 0 to that number.
A. Print 'foo' if the number is divisible by 3.
B. Print 'bar' if the number is divisible by 5.
C. Print 'foobar' if the number is divisible by both 3 and 5.
"""
num = int(input("Give me some positive natural number: "))
for i in range(num + 1):
    if not i % 3 and not i % 5:
        print('foobar')
    elif not i % 3:
        print('foo')
    elif not i % 5:
        print('bar')

"""
1. Write a function called square() with one argument of int type and returns the value of that number raised
to the second power.
"""
def square(x):
    return x ** 2

print(f'{square(int(input("Put number to square: ")))}')
"""
2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent
temperature in Fahrenheit. It should take a number as an argument from user input and return a number to the console.
"""
def convert_cel_to_fahr(c):
    return (c * 1.8) + 32


cels = int(input("Temperature in C: "))
print(f'Equals to {convert_cel_to_fahr(cels)} in Fahrenheit.')
"""
3. Write a function that implement case swapping. It should return the same result as swapcase() method.
Your function should accept one str argument and convert all lower case values to upper case and vice versa.
def swapcase(input_string: str) -> str:
    # do something

print(swapcase('HelLo')) 
> 'hELlO
"""
def swapcase(input_string: str) -> str:
    str_lst = list(input_string)
    for i in range(len(str_lst)):
        if str_lst[i].islower():
            str_lst[i] = str_lst[i].upper()
        elif str_lst[i].isupper():
            str_lst[i] = str_lst[i].lower()
    str_result = ''.join(str_lst)
    return str_result


text = input()
print(swapcase(text))

"""
Optionally.

Draw a square with *
"""
def square(x):
    for i in range(x):
        for j in range(x):
            print('*', end='')
        print()


num = int(input("Side of square (positive int): "))
square(num)

"""
Draw a rectangle with *
"""
def rectangle(x, y):
    for i in range(x):
        for j in range(y):
            print('*', end='')
        print()


x, y = int(input('Side A (positive int): ')), int(input('Side B (positive int): '))
rectangle(x, y)

"""
Draw a right_triangle with *
"""
# With inner loop
def right_triangle(a):
    for i in range(1, a + 1):
        for j in range(i):
            print('*', end=' ')
        print()


# Without inner loop
def right_triangle(a):
    for i in range(1, a + 1):
        print('* ' * i, end='')
        print()


n = int(input('Side of right triangle (positive int): '))
right_triangle(n)

"""
Draw a rectangle with *. Only outlines.
"""
def rectangle(a, b):
    for i in range(a):
        if i == 0 or i == a - 1:
            print('*' * b)
        else:
            print('*' + ' ' * (b - 2) + '*')


x, y = int(input('Side A (positive int): ')), int(input('Side B (positive int): '))
rectangle(x, y)
