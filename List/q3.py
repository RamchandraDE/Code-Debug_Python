a = [23, 23, 23, 23, 26, 78, 81]
b = []

for i in a:
    if i not in b:
        b.append(i)

while b.count(23) > 0:
    b.remove(23)

print(a)
print(b)
