# List in dictonary


details = {
    "Anirudh": [78, 43, 22],
    "Rama": [11, 56, 23],
    "Muskan": [98, 91, 3],
}

# for k, v in details.items():
#     print(f"{k} has scored {sum(v)}")

for k, v in details.items():
    total = 0
    for i in v:
        total = total + i
    print(f"{k} has scored {total} marks")
