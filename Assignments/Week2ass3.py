# 1st answer
# def div_3_and_5(n1: int, n2: int) -> int:
#     i: int = n1
#     while i <= n2:
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, end=" ")
#         i += 1
#     print()


# div_3_and_5(10, 30)
# div_3_and_5(1, 60)

# 2nd answer


def calsum(n1: int, n2: int):
    if n1 > n2:
        return "n1 should be smaller"
    total = 0
    i = n1
    while i <= n2:
        total = total + i
        i += 1
    return total


x = calsum(1, 10)
print(x)

x = calsum(8, 7)
print(x)

SOL 3
def mulTable(num: int):
    i: int = 1
    while i <= 10:
        print(f"{num} X {i} = {num*i}")
        i += 1


mulTable(10)


# def calSum(n1: int, n2: int) -> int:
#     i = n1
#     total = 0
#     while i <= n2:
#         if i % 5 == 0:
#             total = total + i
#         i += 1
#     return total


# x = calSum(1, 100)
# print(x)


def printpattern(num: int):
    if num > 0:
        start: int = -num
        end: int = num
    else:
        start: int = num
        end: int = -num
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printpattern(1)
