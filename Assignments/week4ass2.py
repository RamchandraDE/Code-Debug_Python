# Q1
from typing import List
from math import sqrt


# def genpower(num: int) -> List[int]:
#     return [2**i for i in range(0, int(sqrt(num)) + 1) if 2**i < num]


# x = genpower(100)
# print(x)


# def factorial(n: int) -> List[int]:
#     total = 1
#     for i in range(1, n + 1):
#         total = total * i
#     return total


# print(factorial(3))


# num = 7

# for i in range(2, num):
#     if num % i == 0:
#         print("Not A Prime")
#         break
# else:
#     print("prime")


# def checkPrime(n: int):
#     factors = 0
#     for i in range(1, n+1):


# def removeDuplicates(lst: List) -> None:
#     result = []
#     [result.append(i) for i in lst if i not in result]
#     print(result)


# my_list = [43, 23, 4, 2, 44, 3, 23, 45, 1, 1, 2, 3, 2]
# removeDuplicates(my_list)


# def sumOfList(list1, list2):
#     if len(list1) != len(list2):
#         print("List must have the same length")
#         return
#     return [list1[i] + list2[i] for i in range(len(list1))]


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# x = sumOfList(list1, list2)

# print(x)


# def add(list1, list2):
#     result = []

#     for i in range(0, len(list1)):
#         result.append(list1[i] + list2[i])

#     return result


# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# x = add(list1, list2)
# print(x)

numbers = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 1, 2, 2, 2, 1, 2, 3, 1, 2, 2]

result = []

[result.append(num) for num in numbers if numbers.count(num) > 3 and num not in result]
print(result)
