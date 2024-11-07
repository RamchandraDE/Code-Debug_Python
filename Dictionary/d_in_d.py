details = {
    "ram": {
        "age": 25,
        "Gender": "Male",
        "Address": "Mckinney",
        "Phone": 100,
        "physics": 68,
        "Maths": 95,
        "chemistry": 85,
    },
    "head": {
        "age": 30,
        "Gender": "male",
        "Address": "Australia",
        "Phone": 6565,
        "physics": 0,
        "Maths": 90,
        "chemistry": 75,
    },
}

for key, details in details.items():
    total = details.get("physics", 0) + details["chemistry"] + details["Maths"]
    print(f"{key} has scored {total} marks")

# print(sum([
#     student_details["ram"]["physics"],
#     student_details["ram"]["Maths"],
#     student_details["ram"]["chemistry"]
# ]))


# print2 = sum(
#     [
#         student_details["ram"]["physics"],
#         student_details["ram"]["Maths"],
#         student_details["ram"]["chemistry"],
#     ]
# )
# print(f"Ram has scored {print2}")

# print1 = sum(
#     [
#         student_details["head"]["physics"],
#         student_details["head"]["Maths"],
#         student_details["head"]["chemistry"],
#     ]
# )

# print(f"Head has scored {print1}")
