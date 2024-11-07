def allnum(n1: int, n2: int):
    i = n1
    total = 0
    while i <= n2:
        if i % 3 == 0 and i % 6 == 0:
            total = total + i
        i += 1
    print(total)


allnum(1, 20)
