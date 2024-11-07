from typing import List


# def listSlice(lst: List, start: int, end: int):
#     print(lst[start : end + 1])


# my_list = ["Ram", 6, 4, 100, 203.63, True, -45]
# listSlice(my_list, 2, 4)

"""1. Make a list
   2. ask input form user integer
   3. make another list contains the last n elements of original list"""


# def usingSli(lst: List, n: int):
#     l = len(lst)
#     result = lst[: l - n - 1 : -1]
#     print(result)


# my_list = ["Ram", 6, 4, 100, 203.63, True, -45]
# usingSli(my_list, 3)


# def interchange(lst: List):
#     temp = lst[0]
#     lst[0] = lst[-1]
#     lst[-1] = temp


# my_list = ["Ram", 6, 4, 100, 203.63, True, -45]
# interchange(my_list)
# print(my_list)


def twehalf(lst: List):
    mid: int = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    print(first_half)
    print(second_half)


my_list = ["Ram", 6, 4, 100, 203.63, True, -45, 8]
twehalf(my_list)
