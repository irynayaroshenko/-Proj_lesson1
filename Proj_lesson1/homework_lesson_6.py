from random import randint
"""
Practice block 1
1. Create an outer function that will accept two parameters, a and b
2. Create an inner function inside an outer function that will calculate the addition of a and b
3. At last, an outer function will add 5 into addition and return it
"""
def outer(a, b):
    def inner():
        return a + b
    add = inner() + 5
    return add


print(outer(2, 3))

"""
Practice block 2
1. Write a program that asks user to enter an integer and convert it to int. If the user enters something that is not
an integer, program should catch an error and ask the user to enter an integer again. If user inputs an integer,
program should print this number and quit w/o any error.
2. Write a program that asks the user to input a string and an integer n. Then display the character at index n in
the string. You should handle an error properly and display proper error message.
"""
# 1.
while True:
    try:
        get_int = int(input("Input an integer: "))
        print(get_int)
        break
    except ValueError:
        print("It's not an integer. Input an integer: ")

# 2.
st, n = input("Enter some text: "), int(input("Enter a number (int): "))
try:
    print(f'{n} character in text is {st[n]}.')
except IndexError:
    print(f"Text has fewer characters (can't display {n}th character).")

"""
Practice block 3
1. Write a function that simulate a dice roll and returns the result from 1 to 6.

2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value

3. Simulate an election for two candidates. Program should take amount of regions and rating for 1st candidate in each
region (in percentage). Program should run election in every region. In every region, program should ask 10 000 voters.
Candidate count as a winner if he gains more than 50% of all votes. Program should print the result of the election for
each region and the winner
Example:
Enter number of regions: 2
Enter rating for 1st candidate in each region: 34, 56
Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate
Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate
Result: 2nd candidate won with 10900 votes and 54.5% of all votes
"""
# 1.
def dice_roll():
    return randint(1, 6)


print(dice_roll())

# 2.
def dice_roll_simulation(rolls):
    times = [0] * 6
    for _ in range(rolls):
        roll = dice_roll()
        times[roll - 1] += 1
    result = f'Dice roll results for {rolls} times:\n'
    for i in range(len(times)):
        result += f'{i + 1} - {times[i] + 1} times, '
    return result[:-2] + '.'


print(dice_roll_simulation(10000))

# 3.
regions = int(input('Enter number of regions: '))
voters = 10000
rate_for_1st = []
total_votes_1st, total_votes_2nd = 0, 0

for i in range(regions):
    rate_for_1st.append(randint(1, 100))
print(f"Rating for 1st candidate in each region (in %): {', '.join(map(str, rate_for_1st))}.")

for i in range(regions):
    votes_1st = int((rate_for_1st[i] / 100) * voters) + randint(10, 99)
    votes_2nd = voters - votes_1st
    total_votes_1st += votes_1st
    total_votes_2nd += votes_2nd
    print(f"Region {i + 1}: {votes_1st} votes for 1st candidate, {votes_2nd} votes for 2nd candidate.")

tot_per1 = int((total_votes_1st / (voters * regions)) * 100)
tot_per2 = int((total_votes_2nd / (voters * regions)) * 100)
if total_votes_1st > total_votes_2nd:
    print(f'Result: 1st candidate won with {total_votes_1st} votes and {tot_per1}% of all votes.')
elif total_votes_2nd > total_votes_1st:
    print(f'Result: 2nd candidate won with {total_votes_2nd} votes and {tot_per2}% of all votes.')
else:
    print('Second tour is ahead!')

"""
Practice block 4
1. Create a tuple with your first name, last name, and age.
2. Print your last name using indexing.
3. Create three variables in one line that extracted from tuple that you created in step 1.
4. Print your name letter by letter from this tuple
5. Create a new tuple that contains all info from the first tuple but remove first letter from all strings
6. Create a tuple with two values. First one is (1, 2), second one is (3, 4).
7. Create a program that calculates the sum of all values in the tuple and print it to the console.
"""
# 1.
pers_data = ('Iryna', 'Yaroshenko', 39)
# 2.
print(pers_data[1])
# 3.
name, surname, age = pers_data[0], pers_data[1], pers_data[2]
# 4.
for i in pers_data[0]:
    print(i)
# 5.
new_pers_data = (pers_data[0][1:], pers_data[1][1:], pers_data[2])
# 6.
val_tuple = ((1, 2), (3, 4))
# 7.
def tuple_sum(tpl: tuple):
    return sum(tpl[0]) + sum(tpl[1])


print(tuple_sum(val_tuple))
