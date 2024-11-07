from typing import Dict


def countDict(dik):
    return len(dik.keys())


print(countDict({}))
print(countDict({"name": "xyz"}))

# def checkDict(dick):
#     count = 0
#     for i in dick.keys():
#         count += 1
#     if count == 0:
#         return True
#     return False


# print(checkDict({}))
# print(checkDict({"name": "xyz"}))


# def createDict(n):
#     my_dict = {}
#     for i in range(1, n + 1):
#         my_dict[i] = i**2
#     return my_dict


# print(createDict(5))
# # marks = {
#     "physics": 32,
#     "comp": 95,
#     "science": 85,
#     "math": 67,
#     "eng": 80,
# }


# print(max(marks.values()))

# heighest = 0
# subject = ""

# for sub, mark in marks.items():
#     if 33 > heighest:
#         heighest = mark
#         sub = subject

# print(subject)
