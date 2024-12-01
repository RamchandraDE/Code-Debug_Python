# print 1 to 10

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i = i + 1


"""
Ask a num from user N 
1 to N

"""


# def print1toN(n):
#     i = 1
#     while i < n:
#         print(i, end=" ")
#         i = i + 1


# print1toN(23)


"""
print(n1,n2) | n1<n2

"""


# def printMtoN(n1, n2):

#     while n1 <= n2:
#         print(n1, end=" ")
#         n1 += 1
#     print()


# printMtoN(1, 7)
# printMtoN(125, 132)


# def printMtoN1(n1, n2):
#     i = n1
#     while i <= n2:
#         print(i, end=" ")
#         i += 1


# printMtoN1(1, 7)


# def printNumbers(n1, n2):
#     if n1 < n2:
#         i = n1
#         while i <= n2:
#             print(i, end=" ")
#             i += 1
#         print()

#     elif n1 > n2:
#         i = n2
#         while i <= n1:
#             print(i, end=" ")
#             i += 1
#         print()
#     else:
#         print(n1)


# printNumbers(10, 15)
# printNumbers(14, 11)
# printNumbers(10, 10)


# def printNinja(n1, n2):
#     start = n1 if n1 < n2 else n2
#     end = n2 if n1 < n2 else n1
#     while start <= end:
#         print(start, end=" ")
#         start += 1
#     print()


# # printNinja(10, 20)
# printNinja(20, 10)


# def print10to1(n1, n2):
#     i = n1
#     while i >= n2:
#         print(i, end=" ")
#         i -= 1


# print10to1(10, 1)


# i = 1
# total = 0
# while i <= 10:
#     total = total + i
#     i += 1

# print(total)


# def div_by_3_and_5(n1, n2):
#     i = n1
#     while i <= n2:
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, end=" ")
#         i += 1
#     print()


# div_by_3_and_5(1, 60)


# def calSum(n1, n2):
#     if n1 > n2:
#         return "n1 should be smaller"
#     i = n1
#     total = 0
#     while i <= n2:
#         total = total + i
#         i += 1
#     return total


# x = calSum(1, 10)
# print(x)

# x = calSum(7, 3)
# print(x)


# def multitable(n):
#     i = 1
#     while i <= 10:
#         print(f"{n} x {i} = {n*i}")
#         i += 1


# multitable(10)


# def calsum(n1, n2):
#     total = 0
#     i = n1
#     while i <= n2:
#         if i % 5 == 0:
#             total = total + i
#         i += 1
#     return total


# ans = calsum(43, 68)
# print(ans)


def pat(num):
    if num > 0:
        start = -num
        end = num
    else:
        start = num
        end = -num
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


pat(-9)
