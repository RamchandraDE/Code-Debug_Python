details = {
    "Anirudh": [78, 43, 22],
    "Rama": [11, 56, 23],
    "Muskan": [98, 91, 3],
}


highest_marks = 0
highest_marks_s_name = ""

for k, v in details.items():
    if sum(v) > highest_marks:
        highest_marks = sum(v)
        highest_marks_s_name = k


print(highest_marks_s_name)
print(highest_marks)


# for k, v in details.items():
#     total = 0
#     heighest = 0
#     for i in v:
#         # if max(details)
#         total = total + i
#         if total > heighest:
#             heighest = total
#     print(f"{k} has marks scored {total}")
# print(f"{k} has scored {heighest} marks")
