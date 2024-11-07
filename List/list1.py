# my_list = [11, 2, "Ram", False, 0.85, True, " "]
# print(my_list)
# print(type(my_list))

lst = [67, 34, 24, 67, 87, 98, 0.04837]

# for i in range(-1, -(len(lst) + 1), -1):
#     print(lst[i], end=" ")


for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")

# for i in range(0, len(lst)):
#     print(lst[i], end=" ")

# print()
# for i in range(len(lst)):
#     print(lst[i], end=" ")
