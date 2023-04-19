"""
1. Write a Python program to compute the difference between two lists.
Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']
Expected Output:
first-second: ['a', 'b']
second-first: ['e']

def compute_difference(first: list, second: list) -> tuple:
    # write your code here
    pass

def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result4 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result4 == ([1], [4])
"""
def compute_difference(first: list, second: list) -> tuple:  # result1 fail, other pass
    first_diff, second_diff = [], []
    for i in first:
        if i not in second:
            first_diff.append(i)
    for i in second:
        if i not in first:
            second_diff.append(i)
    print(first_diff, second_diff)
    return first_diff, second_diff

def compute_difference(first: list, second: list) -> tuple:  # result4 fail, other pass

    for i in first:
        if i in second:
            first.remove(i)
            second.remove(i)
    # for i in second:
    return first, second

# З варіанту вище я хотіла зробити функцію в функції, де б одна робила першу перевірку, після закінчення якої
# запускаєть друга (внутрішня) функція і перевіряє те ж саме, але з лістами, які повернула перша перевірка.
# Нижче моя спроба, але вона failed, бо там якась дика рекурсія вийшла. Знаю, що там дикість, але не знаю, з якого боку
# підійти, щоб виправити (може, там місцями треба щось поміняти). Як це виправити, щоб було по логіці, яку я описала?

# def compute_difference(first: list, second: list) -> tuple:
#     for i in first:
#         if i in second:
#             first.remove(i)
#             second.remove(i)
#
#     def recheck_diff(f, s):
#         compute_difference(f, s)
#
#     recheck_diff(first, second)
#     return first, second

# Цей варіант видав ChatGPT, але мені здається, якось можна гарніше. Але поки не знаю, як.
def compute_difference(first: list, second: list) -> tuple:
    def check_diff(f, s):
        for i in f:
            if i in s:
                f.remove(i)
                s.remove(i)
        return f, s

    first_diff, second_diff = check_diff(first, second)
    second_diff, first_diff = check_diff(second_diff, first_diff)
    return first_diff, second_diff

"""
2. Given an array of int nums and an integer target, return indices of the 2 numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

def sum_of_two(nums: list, target: int) -> list:
    # write your code here
    pass

def test_sum_of_two():
    result1 = sum_of_two([2,7,11,15], 9)
    assert result1 == [0, 1]

    result2 = sum_of_two([3,2,4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3,3], 6)
    assert result3 == [0, 1]
    
    result4 = sum_of_two([4, 9, 12, 0, 7, -1, 9], 6)
    assert result4 == [4, 5]
"""
# def sum_of_two(nums: list, target: int) -> list:
#     for i in range(len(nums)):
#         if nums[i] + nums[i + 1] == target:
#             return [i, i + 1]

"""
3. Write a program that takes a list of integers as input and returns a new list that contains only the elements
that are unique (i.e., that appear only once in the list). For example, if the input list is [1, 2, 3, 2, 4, 5, 5],
the output list should be [1, 3, 4]. You can not use set data structure. It`s also forbidden to use the count method.

def unique_elements(arr: list) -> list:
    # write your code here
    pass

def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]

    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == []

    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []
"""
# def unique_elements(arr: list) -> list:       # result1, result3 pass, result2 fail
#     unique_lst = []
#
#     for i in arr:
#         count = 0
#         for j in arr:
#             if i == j:
#                 count += 1
#         if count == 1:
#             unique_lst.append(i)
#     print(unique_lst)
#     return unique_lst

"""
4. Write a program that takes a list of integers as input and returns a new list that contains only the elements
that appear an odd number of times in the list. For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output
list should be [1, 3, 4].

```python
def odd_elements(arr: list) -> list:
    # write your code here
    pass

def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]

    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result1 == [1, 3, 4, 6]
```
"""
# def odd_elements(arr: list) -> list:
#     result = []
#     for i in arr:
#         if i in result:
#             continue
#         if arr.count(i) % 2:
#             result.append(i)
#     return result

"""
5. Write a program that takes a list of integers as input and returns the second-largest element in the list.
If the list has fewer than two elements, the program should return None. For example, if the input list is
[1, 2, 3, 2, 4, 5, 5], the program should return 5.

def second_largest_element(arr: list) -> int:
    # write your code here
    pass

def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5

    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4

    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None
"""
# def second_largest_element(arr: list) -> int:          # result1, result2 pass, result3 fail
#     if len(arr) < 2:
#         return
#     arr.sort()
#     return arr[-2]

# def second_largest_element(arr: list) -> int:            # result2, result3 pass, result1 fail
#     arr_set = set(arr)
#     arr = list(arr_set)
#     if len(arr) < 2:
#         return
#     arr.sort()
#     return arr[-2]

"""
6. Optional (hard): Longest Increasing Sequence
Have the function longest_increasing_sequence take the list of positive integers and return the length of the longest
increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest
to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several
different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6].
For this input, your program should return 3 because that is the length of the longest increasing subsequence.

Examples
Input: [9, 9, 4, 2]
Output: 1

Input: [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
Output: 7

def longest_increasing_sequence(arr: list) -> int:
    # write your code here
    pass

def test_sum_of_two():
    result1 = longest_increasing_sequence([9, 9, 4, 2])
    assert result1 == 1

    result2 = longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90])
    assert result2 == 7

    result3 = longest_increasing_sequence([4, 3, 5, 1, 6])
    assert result3 == 3
    
    result4 = longest_increasing_sequence([85, 90, 86, 56, 63, 64, 5, 66, 89, 8])
    assert result4 == 5
"""
# def longest_increasing_sequence(arr: list) -> int:
#     lis = 0
#     while len(arr) > 1:
#         temp = arr[:1]
#         for i in range(len(arr)):
#             if arr[i] > temp[-1]:
#                 temp.append(arr[i])
#         if len(temp) > lis:
#             lis = len(temp)
#         arr = arr[1:]
#     return lis

# Other solution:
def longest_increasing_sequence(arr):
    n = len(arr)
    # Ініціалізувати список довжиною n з усіма значеннями як 1
    # (для того, щоб потім його змінювати і передавати результати роботи)
    lis = [1] * n

    # Цикл по масиву з другого елемента(бо перший як найменьше вже враховано)
    for i in range(1, n):
        # Перевірте всі попередні елементи, які можуть утворювати підпослідовність з поточним елементом
        for j in range(i):
            if arr[j] < arr[i]:
                # Якщо поточний елемент більший за
                # попередній елемент то це підпослідовність, оновити LIS поточного елемента до максимального
                # його поточного LIS і LIS попереднього елемента плюс 1
                # (Тут кожне значення буде відповідати розміру послідовності з наступним елементом)
                lis[i] = max(lis[i], lis[j] + 1)

    # Повертаємо найбільше значення з послідовності
    print(max(lis))
    return max(lis)


longest_increasing_sequence([1, 2, 3, 2, 5, 1, 2, 3, 4])

"""
7. Sort the following list by population. Calculate average and total population for cities from this list:
"""
# cities = [
#     ('New York City', 8550405),
#     ('Los Angeles', 3792621),
#     ('Chicago', 2695598),
#     ('Houston', 2100263),
#     ('Philadelphia', 1526006),
#     ('Phoenix', 1445632),
#     ('San Antonio', 1327407),
#     ('San Diego', 1307402),
#     ('Dallas', 1197816),
#     ('San Jose', 945942),
# ]
#
# popul_sort = sorted(cities, key=lambda x: x[1])
# print(popul_sort)
