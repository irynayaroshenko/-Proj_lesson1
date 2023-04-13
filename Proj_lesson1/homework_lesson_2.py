# 1. Write a program that gets two int variables and swap their values.
# Do it in 3 different ways.

# Way 1
num1, num2 = int(input()), int(input())
print(f'num1 = {num1}, num2 = {num2}')
num1, num2 = num2, num1
print(f'num1 = {num1}, num2 = {num2}')

# Way 2
numb1, numb2 = int(input()), int(input())
print(f'numb1 = {numb1}, numb2 = {numb2}')
temp = numb1
numb1 = numb2
numb2 = temp
print(f'numb1 = {numb1}, numb2 = {numb2}')

# Way 3
number1, number2 = int(input()), int(input())
print(f'number1 = {number1}, number2 = {number2}')
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print(f'number1 = {number1}, number2 = {number2}')

# 2. Write a program that gets 2 numbers from the user. Print to the console their difference.
# Enter first number: 5
# Enter second number: 3
# Difference is 2
first_num, second_num = int(input('Enter first number: ')), int(input('Enter second number: '))
print(f'Difference is {first_num - second_num}')

# 3. Write a program that get 2 numbers from the user. Print to the console maximum of this two variable.
# Enter first number: 75
# Enter second number: 34
# Maximum is: 75
first_num, second_num = int(input('Enter first number: ')), int(input('Enter second number: '))
print(f'Maximum is: {max(first_num, second_num)}')

# 4. Optional: Write a program that gets 3-digit number from the user and reverses it.
# Enter a number: 123
# Reversed number is 321
# You can use only numbers and their operators. Don`t use string here!
num = int(input('Enter a number: '))
first_digit = num // 100
second_digit = (num % 100) // 10
third_digit = num % 10
print('Reversed number is ', third_digit, second_digit, first_digit, sep='')
