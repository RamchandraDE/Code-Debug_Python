student_details = {
    "ram": {
        "age": 25,
        "Gender": "Male",
        "Address": "Mckinney",
        "Phone": 100,
    },
    "head": {
        "age": 30,
        "Gender": "male",
        "Address": "Australia",
        "Phone": 6565,
    },
}

for name, details in student_details.items():
    for k, v in details.items():
        print(k, v)
