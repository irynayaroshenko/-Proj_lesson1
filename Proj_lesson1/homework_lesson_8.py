"""
1. Write a game where user should guess a capital of the country that you have in your dictionary.
You should show user a random country from the list and ask him to guess the capital.
- If user input right capital, print "You are right!", add him a point and ask him to guess another country.
- If not, you should ask again.
- User should be able to quit the game by typing "exit".
- You should print current score after each round.
- Also, you should print the final score before user quit the game.

Optional:
Give user a hint if he guesses wrong. Hint should look like first letter of the capital.
If user makes another mistake, you should print one more letter from the capital.

If user make a mistake you should decrement his lives. Initial amount of lives is 3.
Game will end when user has no lives left.
You should print the final score after user has no lives left.
"""
from random import choice

capitals = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'USA': 'Washington',
    'Canada': 'Ottawa',
    'Switzerland': 'Bern',
    'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo',
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki',
    'Poland': 'Warsaw',
    'Romania': 'Bucharest',
    'Bulgaria': 'Sofia',
    'Greece': 'Athens'}

score = 0
lives = 3
hint = 0

def random_country(data: dict):
    return choice(list(data.keys()))

def ask_question():
    rand_country = choice(list(capitals.keys()))
    answ_input = input(f'What is the capital of {rand_country}? > ').lower()
    return rand_country, answ_input

def is_correct(country: str, ans: str):
    return ans.lower() == capitals[country].lower()


def try_again(y_n_input: str):
    return y_n_input.lower() in ('y', 'yes')


def quit_game():
    print(f"\t**Game is over.**\nFinal score is {score}. Thanks for playing!")


print("** Let's start a game called 'Guess the capital' **\nEach correct answer gives you 1 point. \
You have 3 lives. To quit the game - type 'exit'.\n")

while lives > 0:
    rand_country = choice(list(capitals.keys()))
    capital = capitals[rand_country].lower()
    answ_input = input(f'What is the capital of {rand_country}? > ')
    if is_correct(rand_country, answ_input):
        score += 1
        play = input(f'You are right! Score: {score}.\nContinue playing? (Y/N) > ')
        if try_again(play):
            continue
        quit_game()
        break
    # lives -= 1  # problem here: Incorrect. You have 0 lives left.
    # hint += 1
    while answ_input != capital and lives != 0:
        lives -= 1
        hint += 1
        print(f"Incorrect. You have {lives} lives left. Hint: the capital of {rand_country} starts\
with {capitals[rand_country][:hint]}.")
        answ_input = input('Next guess: ').lower()
    hint = 0
    if lives == 0:
        quit_game()
        break
    score += 1
    play = input(f'You are right! Score: {score}.\nContinue playing? (Y/N) > ')
    if try_again(play):
        continue
    quit_game()
    break



#     else:
#         while answ_input != capital:
#             lives -= 1
#             if lives == 0:
#                 quit_game()
#                 break
#             hint += 1
#             print(f"Incorrect. You have {lives} lives left. Hint: the capital of {rand_country} starts\
# with {capitals[rand_country][:hint]}.")
#             answ_input = input('Next guess: ').lower()
#         hint = 0
#         score += 1
#         play = input(f'You are right! Score: {score}.\nContinue playing? (Y/N) > ')
#         if not try_again(play):
#             quit_game()
#             break





# while True:
#     while is_correct(country_to_guess, answer):
#         correct = True
#         if not try_again(play):
#             quit_game()
#             exit()
#
#         country_to_guess = random_country(capitals)
#         answer = input(f'What is the capital of {country_to_guess}? > ')
#         continue
#
#     if not correct:
#         lives -= 1
#         print(f"{answer.title()} is not a capital of {country_to_guess}. You have {lives} lives left.")
#         if lives == 0:
#             quit_game()
#             exit()
#
#     correct = False
#     print(f"Hint: the capital of {country_to_guess} starts with {capitals[country_to_guess][:1]}.")
#     answer = input(f'What is the capital of {country_to_guess}? > ')



# while lives > 0:
#     country_to_guess = random_country(capitals)
#     answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#
#     while is_correct(country_to_guess, answer):
#         score += 1
#         print(f"You are right! You earned a point.\nYour score is {score}.")
#         play = input("Continue playing? (Y/N) > ")
#         if try_again(play):
#             continue
#
#         quit_game()
#         exit()
#
#     lives -= 1
#     if lives == 0:
#         print(f"You lost all your lives. The capital of {country_to_guess} is {capitals[country_to_guess]}.")
#         quit_game()
#         exit()
#
#     print(f"{answer.title()} is not the capital of {country_to_guess}. You have {lives} lives left.")
#     print(f"Hint: the capital of {country_to_guess} starts with {capitals[country_to_guess][0]}.")

# def random_country(data: dict):
#     return choice(list(data.keys()))
#
#
# def is_correct(ans: str):
#     if ans == capitals[country_to_guess].lower():
#         return True
#     else:
#         return False
#
#
# def try_again(y_n_input: str):
#     if y_n_input in ('y', 'yes'):
#         return True
#     else:
#         return False
#
#
# def quit_game():
#     print(f"\t**Game is over.**\nFinal score is {score}. Thanks for playing!")
#
#
# print("** Let's start a game called 'Guess the capital' **\nEach correct answer gives you 1 point. \
# You have 3 lives. To quit the game - type 'exit'.\n")
#
# country_to_guess = random_country(capitals)
# answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#
# while True:
#     while is_correct(answer):
#         score += 1
#         print(f"You are right! You earned a point.\nYour score is {score}.")
#         play = input("Continue playing? (Y/N) > ").lower()
#         if try_again(play):
#             country_to_guess = random_country(capitals)
#             answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#             continue
#         elif not try_again(play):
#
#         else:
#             quit_game()
#             break
#
#     while lives > 1:
#         lives -= 1
#         print(f"{answer.title()} is not a capital of {country_to_guess}. You have {lives} lives left.")
#         print(f"Hint: the capital of {country_to_guess} starts with {capitals[country_to_guess][:1]}.")
#         answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#         continue
#     quit_game()
#     break


# while True:
#     if is_correct(answer):
#         score += 1
#         print(f"You are right! You earned a point.\nYour score is {score}.")
#         play = input("Continue playing? (Y/N) > ").lower()
#         if try_again(play):
#             country_to_guess = random_country(capitals)
#             answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#             continue
#         else:
#             quit_game()
#             break
#     else:
#         while lives > 1:
#             lives -= 1
#             print(f"{answer.title()} is not a capital of {country_to_guess}. You have {lives} lives left.")
#             print(f"Hint: the capital of {country_to_guess} starts with {capitals[country_to_guess][:1]}.")
#             answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#             continue
#         quit_game()
#         break


# def user_answer(text: str):
#     score = 0
#     while text != 'exit'.lower():
#         if text == capitals[country_to_guess].lower():
#             score += 1
#             print(f"You are right! You earned a point.\nYour score is {score}.")
#             play = input("Continue playing? (Y/N) > ").lower()
#             while play not in ('n', 'no', 'not'):
#                 country_to_guess = random_country(capitals)
#                 answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#                 user_answer(answer)
#             return quit_game()
#     return quit_game()

# while True:
#     answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#
#     if answer == 'exit':
#         quit_game()
#         break
#     elif answer == capitals[country_to_guess].lower():
#         score += 1
#         print(f"You are right! You earned a point.\nYour score is {score}.")
#         play = input("Continue playing? (Y/N) > ")
#         while not 'n'.lower() and 'no'.lower():
#             answer = input(f'What is the capital of {country_to_guess}? > ').lower()
#
#         quit_game()
#         break
#     else:
#         lives -= 1
#         print(f"{answer.title()} is not a capital of {country_to_guess}. You have {lives} lives left.")
#         print(f"Hint: the capital of {country_to_guess} starts with {capitals[country_to_guess][:1]}.")
#         next_try = input()

"""
4. Given an array nums of size n, return the majority element.
The majority element is the element that appears more than any other element.
You may assume that the majority element always exists in the array.
"""
# from collections import defaultdict
#
# def majority_element(nums: list) -> int:
#     numb_count_dict = defaultdict(int)
#     for i in nums:
#         numb_count_dict[i] += 1
#
#     tuple_lst = list(numb_count_dict.items())
#     maj_elem = max(tuple_lst, key=lambda x: x[1])[0]
#     return maj_elem
#
# def test_majority_element():
#     result1 = majority_element([3, 2, 3])
#     assert result1 == 3
#
#     result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
#     assert result1 == 2
#
# test_majority_element()

"""
6. Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3 Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1 Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    def length_of_longest_substring(s: str) -> int:
        pass

    def test_length_of_longest_substring():
        result1 = length_of_longest_substring('abcabcabc')
        assert result1 = 3

        result2 = length_of_longest_substring('bbbbb')
        assert result2 = 1

        result3 = length_of_longest_substring("pwwkew")
        assert result3 = 3
"""
def length_of_longest_substring(s: str) -> int:
    pass