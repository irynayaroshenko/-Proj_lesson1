# Practice chapter 1
"""
Guess result of expression without executing it:
a) 1 <= 1  ---> True
b) 1 != 1  ---> False
c) 1 != 2  ---> True

Make all of them true.
a) 3 __ 4      ---> 3 < 4
b) 10 __ 5     ---> 10 >= 5
c) 42 __ "42"  ---> 42 != "42"
"""


# Practice chapter 2

# Print the text in which there will be a quote with double quotes.
print('One of Poe’s most unsettling tales, "The Black Cat", actually contains two black cats.')

# Print the text in which there will be an apostrophe.
print('...it\'s like to live as a cat in this wonderful short story.')  # if to use ’ we won't need \

# Print one line that will be displayed on several lines
print("One of Kipling’s Just So Stories (1902),\nand the longest tale in that classic collection\nof origin stories...")

# Print text that doesn`t fit in one line but will be displayed in one line
print('Schrödinger’s cat: a cat, a flask of poison, \
and a radioactive source connected to a Geiger counter \
are placed in a sealed box.')


# Practice chapter 3

# Create a variable with data type string. Count the length of this line.
text = 'a string variable'
print(len(text))

# Create another variable with string data type. Output the result of concatenation of these two variables.
another_text = "another str var"
print(text + another_text)

# Print the two previous variables, but with a space between them.
print(text + ' ' + another_text)
print(f'{text} {another_text}')

# Get a string from user input. Check if the string is a palindrome.
def is_palindrome(string):
    return string[:] == string[::-1]


txt = input("Enter some word or text: ")
if is_palindrome(txt):
    print("Text is palindrome.")
else:
    print("Text is not palindrome.")


# Practice chapter 4

# The program receives user's name and age from input. You need to display the name and age in one line in several ways:
# String should look like this: "Your name is {name} and your {age} years old"
name = input("What is your name? ")
age = input("How old are you? ")
# a) by listing all the parameters in the print function
print('Your name is', name, 'and you are', age, 'years old.')
# b) by formatting a string using the format function
print("Your name is {name} and you are {age} years old.".format(name=name, age=age))
# c) by formatting a string with f-string
print(f"Your name is {name} and you are {age} years old.")
# d) additional (to use more options from theory list)
print("Your name is {0} and you are {1} years old.".format(name, age))


# Practice chapter 5
# Format string with a proper functions

# All letters must be written in lowercase.
string_1 = "Animals  "
print(string_1.lower())

# All letters must be capitalized.
string_2 = "  Badger"
print(string_2.upper())

# Remove all spaces:
string_3 = "   HoneyPot   "
# a) from the beginning of the line
print(string_3.rstrip())
# b) from the end of the line (Note: to check this line you need to comment previous line a)
print(string_3.lstrip())
# c) on both sides of the line (Note: to check this line you need to comment 2 previous lines a and b)
print(string_3.strip())

# Check the value of the startswith ('Be') function for each line.:
string_1 = "Bear"
print(string_1.startswith('Be'))  # True

string_2 = "bear"
print(string_2.startswith('Be'))  # False

string_3 = "BEAR"
print(string_3.startswith('Be'))  # False

string_4 = "bEar"
print(string_4.startswith('Be'))  # False

# Convert rows with methods from prev exercise to have positive result for each row.
# formatted_string = string_1.some_cool_function()
# formatted_string.startswith('Be')
# > True

string_2.capitalize()
print(string_1.startswith('Be'))  # True

string_3 = string_3.replace('E', 'e')
print(string_3.startswith('Be'))  # True

string_4 = string_4.swapcase()
print(string_4.startswith('Be'))  # True

# Find and replace all letters 's' with the letter 'x' in the following line:
line = 'Somebody said something to Samantha.'
print(line.replace('s', 'x'))  # if replace only 's' to 'x' as in task
print(line.lower().replace('s', 'x'))  # if replace 's' and 'S' to 'x'


# Leave only numbers in the following line using only string methods:
# '12345!,_6--'

# Method 1. Bad one but with 3 methods used
txt = '12345!,_6--'
txt = txt.strip('-')
txt_list = txt.split('!,_')
txt = ''.join(txt_list)
print(txt)

# Method 2
txt = '12345!,_6--'.strip('-').replace('!,_', '')
print(txt)


# (Optional) Find a secret message in the following text: 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'`
message = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
mes = message.replace('X', '_').replace('x', '_').strip('_')[::-1]
mes_lst = mes.split("_")
mes = ''.join(mes_lst)
print(mes)  # Its a secret line!


# (Optional) Граф Дракула народився у Жовтні 1429 року.
# Щороку його друзі дарували на день народження по 5 г золота. Кожен високосний рік – 10 г. Кожен ювілей – по 20 г.
# Чи зможе цього року Граф купити собі гелікоптер, якщо він коштує 250 тис. $., а кілограм золота 55 тис. $.

def is_leap(year):
    return not year % 4 and year % 100 != 0 or not year % 400


count = 0

for i in range(1430, 2024):
    if is_leap(i):
        count += 0.01
    elif i % 10 == 9:
        count += 0.02
    else:
        count += 0.005

count += 0.005  # total amount of gold for all the years with 0.005 g for the day of birth in 1429
print(f'In 2023 Dracula gets {count} kg of gold.')
print(f'Yes, he can buy a helicopter as he has {round(count * 55_000)}.')  # $251.900
