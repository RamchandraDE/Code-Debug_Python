# student_data = {
#     "Alice": [85, 90, 88, 92, 89],
#     "Bob": [78, 82, 79, 81, 80],
#     "Charlie": [92, 95, 88, 85, 91],
# #     "Diana": [76, 80, 79, 82, 85],
#     "Eva": [88, 92, 85, 90, 87],
#     "Frank": [83, 85, 80, 86, 88],
#     "Gina": [90, 87, 92, 88, 86],
# }

# x = dict(sorted(student_data.items(), key=lambda x: sum(x[1])))

# for name, marks in x.items():
#     total_marks = sum(marks)
#     print(f"{name} has scored {total_marks}")
# student_data = {
#     "Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},
#     "Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
#     "Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
#     "Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
#     "Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
#     "Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
#     "Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
# }

# sorted_data = dict(sorted(student_data.items(), key=lambda x: sum(x[1]["marks"])))

# for name, marks in sorted_data.items():
#     total_marks = sum(marks["marks"])
#     print(f"{name} and total marks {total_marks}")


# student_data = [
#     ["Samantha", 18, "New York", 420],
#     ["David", 25, "Los Angeles", 380],
#     ["Sophie", 22, "Chicago", 390],
#     ["Michael", 20, "Houston", 410],
#     ["Liam", 19, "Phoenix", 430],
#     ["Olivia", 21, "Philadelphia", 400],
#     ["Daniel", 23, "San Antonio", 375],
# ]

# sorted_data = list(sorted(student_data, key=lambda x: x[3]))
# print(sorted_data, end=" ")


# student_data = [
#     {"Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]}},
#     {"Max": {"age": 22, "marks": [79, 85, 88, 90, 87]}},
#     {"Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]}},
#     {"Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]}},
#     {"Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]}},
#     {"Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]}},
#     {"Olivia": {"age": 24, "marks": [82, 86, 90, 87, 84]}},
# ]

# sorted_data = sorted(student_data, key=lambda x: sum(x[list(x.keys())[0]]["marks"]))

# for details in sorted_data:
#     name = list(details.keys())[0]
#     marks = details[name]["marks"]
#     total_marks = sum(marks)
#     print(f"{name} has scored {total_marks}")

student_data = [
    [78, 92, 85, "Alice"],
    [82, 79, 81, "Bob"],
    [92, 88, 85, "Charlie"],
    [80, 79, 82, "Diana"],
    [92, 85, 90, "Eva"],
    [85, 80, 86, "Frank"],
    [87, 92, 88, "Gina"],
]

sorted_data = sorted(student_data, key=lambda x: x[0] + x[1] + x[2])

for details in sorted_data:
    total_marks = details[0] + details[1] + details[2]
    name = details[3]
    print(f"{name} has scored {total_marks}")
