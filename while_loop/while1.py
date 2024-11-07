def printMtoN(n1, n2):
    if n1 > n2:
        return
    i = n1
    while i <= n2:
        print(i, end=" ")
        i += 1


printMtoN(1, 13)
