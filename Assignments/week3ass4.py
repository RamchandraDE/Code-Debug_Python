# Q1 Answer
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# odd = []
# even = []

# for i in my_list:
#     if i not in even:
#         if i % 2 == 0:
#             even.append(i)

#         else:
#             odd.append(i)


# print(even)
# print(odd)

# Q2 Answer
# from typing import List

# my_list = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]


# def nums(lst: List[int]) -> None:
#     result = []

#     # for i in range(0, len(lst)):
#     #     if lst[i] not in result:
#     #         result.append(lst[i])

#     for i in lst:
#         if i not in result:
#             result.append(i)
#     print(result)


# # my_list = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
# nums(my_list)

# Q3
# from typing import List

# lst1 = [34, 11, 91, 59, 33, 22]
# lst2 = [78, 11, 23]


# def my_list(lst1: List, lst2: List) -> bool:
#     for i in lst1:
#         if i in lst2:
#             return True
#     return False


# print(my_list(lst1, lst2))

# Q4
# from typing import List


# my_list = [2, 4, 5, 6, 7, 8, 8, 9]


# def sumAvg(lst: List[int | float]) -> None:
#     total = 0
#     for i in lst:
#         total = total + i
#     print(f"Total = {total}")

#     average = total / len(lst)
#     print(f"Average = {average}")


# sumAvg(my_list)

# Q5

# from typing import List

# lst1 = [34, 11, 91, 59, 33, 22]
# lst2 = [78, 11, 23]


# def my_list(lst1: List, lst2: List) -> List:
#     result = []
#     for i in lst1:
#         if i in lst2:
#             result.append(i)
#     return result


# x = my_list(lst1, lst2)
# print(x)

# 6 Q

# from typing import List


# def my_list(lst: List, n: int) -> None:

#     lst.pop(n)


# _list = [2, 3, 4, 5, 5, 6, 7, 7, 8]

# my_list(_list, 8)
# print(_list)

# 7
from typing import List

# My_list = [10, 25, 30, -10, 1, 9]
# My_list2 = [58, 11, -15, 20, 6, 1]


# def sameLength(lst: List[int], lst2: List[int]) -> List[int]:
#     result = []
#     for i in range(0, len(lst)):
#         result.append(lst[i] + lst2[i])
#     return result


# x = sameLength(My_list, My_list2)
# print(x)

# Q8


# def num():
#     ori_list = []
#     for i in range(10):
#         lst = int(input(f"Enter a num = "))
#         ori_list.append(lst)

#     rever_list = ori_list[::-1]

#     return ori_list, rever_list


# # original, rever_list = num()

# x = num()
# print(x, end=" ")
# my_list = []

# for i in range(10):
#     num = int(input(" Enter a num = "))
#     my_list.append(num)


# reverse_num = []

# for i in range(len(my_list) - 1, -1, -1):
#     reverse_num.append(my_list[i])

# print(reverse_num)

# Q9

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def addi(lst: List[int]):
#     if len(lst) == 1:
#         print("Cannot add 2nd and last 2nd element as not enough elements in list")
#         return
#     print(lst[1] + lst[-2])


# addi(my_list)

# Q10


# def removeEven(lst: List[int]) -> None:
#     result = []
#     for i in lst:
#         if i % 2 == 1:
#             result.append(i)
#     print(result)


# my_list = []
# for _ in range(10):
#     num: int = int(input("Enter a num = "))
#     my_list.append(num)

# removeEven(my_list)


# Q11

# my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0, 1, 2, 4, 5]


def prt(lst: List[int]) -> None:
    result = []
    for i in lst:
        if lst.count(i) > 3:
            if i not in result:
                result.append(i)
    print(result)


my_list: List[int] = [1, 2, 3, 4, 5, 5, 5, 7, 2, 9, 2, 1, 2, 1, 5]
prt(my_list)

# from typing import List


# def printGreaterThanThree(lst: List[int]) -> None:
#     result = []
#     for i in lst:
#         if lst.count(i) > 3:
#             if i not in result:
#                 result.append(i)
#     print(result)


# my_list: List[int] = [34, 96, 34, 65, 51, 27, 96, 96, 11, 34, 34, 34, 51, 51, 51]

# printGreaterThanThree(my_list)
