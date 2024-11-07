from typing import List

# 1st Question
# def countOddEven(lst):
#     even_count = 0
#     odd_count = 0
#     for i in range(0, len(lst)):
#         if lst[i] % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#     print(f"Total Even Num = {even_count}")
#     print(f"Total Even Num = {odd_count}")


# my_list = [34, 11, 91, 59, 33, 22]
# countOddEven(my_list)
# print(my_list)


# 2nd Question
# def countOddEven(lst):
#     even_sum = 0
#     odd_sum = 0
#     for i in range(0, len(lst)):
#         if lst[i] % 2 == 0:
#             even_sum = even_sum + lst[i]
#         else:
#             odd_sum = odd_sum + lst[i]

#     print(f"Total Even sum = {even_sum}")
#     print(f"Total odd sum = {odd_sum}")


# my_list = [34, 11, 91, 59, 33, 22]
# countOddEven(my_list)
# print(my_list)


# 3rd Question
# def findLargest(lst: List[int]) -> int:
#     largest = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] > largest:
#             largest = lst[i]
#     return largest


# my_list = [34, 11, 91, 59, 33, 22]
# x = findLargest(my_list)
# print(x)


# 4th Question

# def findSmall(lst: List[int]) -> int:
#     smallest = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] < smallest:
#             smallest = lst[i]
#     return smallest


# my_list = [34, 11, 91, 59, 33, 22]
# x = findSmall(my_list)
# print(x)

# 5th question


# def updateEvenOdd(lst: List) -> int:
#     for i in range(0, len(lst)):
#         if lst[i] % 2 == 0:
#             lst[i] = 0
#         else:
#             lst[i] = 1


# my_list = [34, 11, 91, 59, 33, 22]
# updateEvenOdd(my_list)
# print(my_list)


# 6th Ques


# def updateEvenOdd(lst: List) -> int:
#     for i in range(0, len(lst)):
#         if lst[i] % 2 == 0:
#             lst[i] = lst[i] + 1

#         else:
#             lst[i] = lst[i] - 1


# my_list = [34, 11, 91, 59, 33, 22]
# updateEvenOdd(my_list)
# print(my_list)

# 7th Ques


def calculatePrime(lst: List):
    for i in range(0, len(lst)):
        factors = 0
        num = lst[i]
        for j in range(1, num + 1):
            if num % j == 0:
                factors += 1
        if factors == 2:
            print(num, end=" ")


my_list = [34, 11, 91, 59, 33, 22]

calculatePrime(my_list)
