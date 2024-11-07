"""
Anonymous Function
"""

# add = lambda a, b, c: a + b + c
# x = add(10, 20, 30)

# print(x)


# details = {
#     "Name" : "Rama",
#     "Telugu" : 76,
#     "English": 86,
#     "Maths"  : 78,
#     "chemistry" : 87,
#     "physics" : 80,
#     "Social"  : 70

# }


from typing import Dict


# def sortDict(dictionary: Dict, reverse=False):
#     return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


# my_dict = {1: 2, 3: 4, 5: 7, 3: 0, 4: 9}

# print(f"Ascending order = {sortDict(my_dict)}")
# print(f"Descending order = {sortDict(my_dict,reverse = True)}")


# def ispalindrome(word):
#     return word == word[::-1]


# def checkpalindrome(words):
#     for word in words:
#         if ispalindrome(word):
#             return True
#     return False


# x = abccba
# # ispalindrome(x)
# print(ispalindrome(x))


# def countNum(dictionary):
#     count = 0
#     for key, value in dictionary.items():
#         count = count + len(value)
#         return count


# my_dict = countNum(
#     {"m1": [34, 56, 78, 65, 43, 45, 67], "M2": [89, 67, 84], "M3": [82, 57]}
# )
# print(my_dict)


# def printDict(dictionary):
#     for key, value in dictionary.items():
#         print(key)
#         for k, v in value.items():
#             print(f"{k}: {v}")


# printDict(
#     {
#         "ram": {"M1": 89, "M2": 56, "m3": 89},
#         "rcr": {"M1": 49, "M2": 96, "M3": 89},
#     }
# )


# def convertList(l1, l2):
#     dictionary = {}
#     for i in range(len(l1)):
#         dictionary[l1[i]] = l2[i]
#     return dictionary


# keys = ["one", "two", "three", "four"]
# values = [1, 2, 3, 4]
# my_dict = convertList(keys, values)
# print(my_dict)


# def sortD(dictionary, reverse=False):
#     return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


# my_dict = {1: 2, 3: 4, 5: 6, 6: 7}
# print(my_dict)


# def dicti(dictionary):
#     return dict(sorted(dictionary.items(), key=lambda x: x[1]))


# my_dict = {"a": 2, "b": 5, "c": 90}
# print(my_dict)


# def maximum(dictionary):
#     max_val = 0
#     for v in dictionary.values():
#         if v > max_val:
#             max_val = v
#     return max_val


# def minimum(dictionary):
#     min_val = 0
#     for v in dictionary.values():
#         if v < min_val:
#             min_val = v
#     return min_val


# my_dict = {"a": 28, "b": 32.34, "c": 10, "d": 23.364}
# maxi = maximum(my_dict)
# mini = minimum(my_dict)

# print(f"Maximum {maxi} ")
# print(f"Minimum {mini} ")


# def maximum(dictionary: Dict) -> int | float:
#     max_num = float("-inf")  # Most negative number
#     for v in dictionary.values():
#         if v > max_num:
#             max_num = v
#     return max_num


# def minimum(dictionary: Dict) -> int | float:
#     min_num = float("inf")  # Most positive number
#     for v in dictionary.values():
#         if v < min_num:
#             min_num = v
#     return min_num


# my_dict = {"Anirudh": 54.6, "Akul": 12, "Nihar": 35.123, "Sanjay": 111}

# mini = minimum(my_dict)
# maxi = maximum(my_dict)

# print(f"Minimum = {mini}")
# print(f"Maximum = {maxi}")


# def findDiff(d1, d2):
#     present_in_d1 = []
#     present_in_both = []
#     for k in d1:
#         if k not in d2:
#             present_in_d1.append(k)
#         else:
#             present_in_both.append(k)

#     present_in_d2 = []
#     for k in d2:
#         if k not in d1:
#             present_in_d2.append(k)

#     print(present_in_d1)
#     print(present_in_d2)
#     print(present_in_both)


# findDiff({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5})


# def swapp(dictionary):
#     reversed_dict = {}
#     for k, v in dictionary.items():
#         reversed_dict[v] = k
#     return reversed_dict


# my_dict = {"a": 1, "b": 2, "c": 3}


# result = swapp(my_dict)
# print(my_dict)
# print(result)
# def avgScore(dictionary):
#     for key, marks in dictionary.items():
#         total = marks.get("Math", 0) + marks.get("Science", 0) + marks.get("English", 0)
#         average = total / 3
#         print(f"{key} = {average}")


# avgScore(
#     {
#         "John": {"Math": 85, "Science": 90, "English": 80},
#         "Alice": {"Math": 75, "Science": 88, "English": 92},
#         "Bob": {"Math": 90, "Science": 85, "English": 78},
#     }
# )


# def averageScore(dictionary: Dict) -> None:
#     for key, marks in dictionary.items():
#         total = marks.get("Math", 0) + marks.get("Science", 0) + marks.get("English", 0)
#         average = total / 3
#         print(f"{key} = {average}")


# averageScore(
#     {
#         "John": {"Math": 85, "Science": 90, "English": 80},
#         "Alice": {"Math": 75, "Science": 88, "English": 92},
#         "Bob": {"Math": 90, "Science": 85, "English": 78},
#     }
# )


# def sortKeys(dictionary):
#     return dict(sorted(dictionary.items(), key=lambda x: len(x[0])))


# my_dict = {"banana": 2, "apple": 1, "custardapple": 3}

# result = sortKeys(my_dict)

# print(result)
