lst = [10, 20, 30, 40, 50, 60, 70, 80]


result = 0
for i in range(len(lst)):
    result += lst[i]
print(result)

if result % 2 == 0:
    print("True")
else:
    print("False")
