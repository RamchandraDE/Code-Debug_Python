# dictonary = {}

# count = int(input("Count = "))
# for _ in range(count):
#     value = []
#     key = input("Enter key = ")
#     num_val = int(input("Enter num = "))
#     for i in range(num_val):
#         v = int(input(f"Enter a num {i}"))
#         value.append(v)
#     dictonary[key] = value


# details = {
#     "A": [1, 2, 3],
#     "B": [4, 5, 6],
# }

from typing import Dict, List


# def mergeList(dictonary: Dict) -> List:
#     result = []
#     for v in dictonary.values():
#         result = result + v
#         for i in v:
#             result.append(i)
#         return result


# print(mergeList({"A": [1, 2, 3], "B": [4, 5, 6]}))


# def countChar(string):
#     fre = {}
#     for char in string:
#         if char in fre:
#             fre[char] = fre[char] + 1
#         else:
#             fre[char] = 1
#     return fre


# print(countChar("heellllllloo"))


# def evenDict(dictonary):
#     # for k, v in dictonary.items():
#     #     even_list = []
#     #     for i in v:
#     #         if i % 2 == 0:
#     #             even_list.append(i)
#     #         dictonary[k] = even_list
#     #     return dictonary

#     filtered_dic = {}
#     for key, value in dictonary.items():
#         filtered_dic[key] = [num for num in value if num % 2 == 0]
#     return filtered_dic


# input_dict = {"a": [1, 2, 3, 4, 5], "b": [10, 21, 12, 14, 15]}
# filtered = evenDict(input_dict)
# print(filtered)


# def mergeDict(dictionary1, dictionary2):
#     new_dict = {}
#     for key in dictionary1:
#         if key in dictionary2:
#             new_dict[key] = dictionary1[key] + dictionary2[key]
#         else:
#             new_dict[key] = dictionary1[key]

#     for key in dictionary2:
#         if key not in dictionary1:
#             new_dict[key] = dictionary2[key]
#     return new_dict


# dict1 = {"x": [1, 2, 3], "y": [4, 5, 6]}
# dict2 = {"x": [7, 8, 9], "y": [10, 11, 12], "z": [99, 100, 111]}
# result = mergeDict(dict1, dict2)
# print(result)


# def merge(d1, d2):
#     nd = {}
#     for key in d1:
#         if key in d2:
#             nd[key] = d1[key] + d2[key]
#         else:
#             nd[key] = d1[key]

#     for key in d2:
#         if key not in d1:
#             nd[key] = d2[key]
#     return nd


# di1 = {"a": [1, 2, 3], "b": [4, 5, 6]}
# di2 = {"a": [7, 8, 9], "b": [0, 10, 11], "c": [23, 45, 67]}
# x = merge(di1, di2)
# print(x)


# def addVal(d1, d2):
#     new = {}
#     for key in d1:
#         new[key] = d1[key] + d2.get(key, 0)

#     for key in d2:
#         if key not in d1:
#             new[key] = d2[key]
#     return new


# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 200, "b": 200, "d": 400}
# x = addVal(d1, d2)
# print(x)


# data = {
#     "x": list(range(11, 20)),
#     "y": list(range(21, 30)),
#     "z": list(range(31, 40)),
# }

# for key, value in data.items():
#     print(value[4])


# def perStu(total_marks):
#     return (total_marks / 500) * 100


# students = [
#     {"name": "Rama", "marks": [12, 43, 56, 76, 77]},
#     {"name": "king", "marks": [35, 56, 54, 58, 63]},
#     {"name": "rohit", "marks": [20, 50, 50, 78, 77]},
#     {"name": "travis", "marks": [72, 63, 56, 96, 47]},
#     {"name": "pat", "marks": [23, 63, 66, 76, 47]},
# ]

# for student in students:
#     total_marks = sum(student["marks"])
#     percentage = perStu(total_marks)
#     print(
#         f"name:{student['name']}, totalmarks:{total_marks}, percentage: {percentage:.2f}%"
# )


# students = {
#     "Anirudh": [12, 43, 1, 76, 23],
#     "Akul": [78, 82, 80, 43, 62],
#     "Nihar": [13, 72, 32, 89, 53],
#     "Anusha": [43, 12, 79, 82, 85],
#     "Muskan": [54, 87, 72, 86, 84],
# }

# all_total_marks = []
# for marks in students.values():
#     total = sum(marks)
#     all_total_marks.append(total)

# all_total_marks.sort()

# print(all_total_marks)


# def delkeys(dictionary, k):
#     dictt = dictionary.copy()

#     keys_to_revove = []
#     for key, value in dictt.items():
#         if type(value) == int and value > k:
#             dictt.pop(key)

#     for key in keys_to_revove:
#         dictt.pop(key)

#     return dictt


# test_dict1 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "xyzx": "CS"}
# test_dict2 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "qqqq": "CS"}
# K1 = 7
# K2 = 1

# output1 = delkeys(test_dict1, K1)
# output2 = delkeys(test_dict2, K2)

# print(output1)
# print(output2)


# def removeKeys(dictionary: Dict, K: int):
#     # Uncomment this, if you want to change in original dictionary
#     dictt = dictionary.copy()

#     keys_to_remove = []
#     for key, value in dictt.items():
#         if type(value) == int and value > K:
#             dictt.append(key)

#     for key in keys_to_remove:
#         dictt.pop(key)

#     return dictt


# test_dict1 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "xyzx": "CS"}
# test_dict2 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "qqqq": "CS"}
# K1 = 7
# K2 = 1

# output1 = removeKeys(test_dict1, K1)
# output2 = removeKeys(test_dict2, K2)

# print(output1)
# print(output2)


def clearDic(d):
    for key in d:
        d[key] = []


a = {"c1": [1, 2, 3], "b": [12, 23, 45, 5], "c": [7, 6, 8, 9]}

clearDic(a)
print(a)
