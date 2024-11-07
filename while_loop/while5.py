def calculateFactorSum(n1, n2):
    i = 1
    factor = 0
    while i <= n1:
        if i % n2 == 0:
            factor = factor + i
        i += 1
    print(factor)


calculateFactorSum(30, 7)
