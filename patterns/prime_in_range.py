"""
Make a fun that accepts 2 int as argument.(n1, n2) n1 should be smaller than n2

n1 > n2
Print Prime

printPrime(2,10)
2,3,5,7

using Nested for Loop
"""


def printPrime(n1, n2):
    for num in range(n1, n2 + 1):
        factors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factors += 1
        if factors == 2:
            print(num)


printPrime(0, 15)
