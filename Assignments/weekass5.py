# def ram(n):
#     i = 2
#     num = 2
#     while i <= n:
#         print(num, end=" ")
#         num = (num * 10) + 2
#         i += 1
#     print()


# ram(10)


# def terms(n):
#     i = 1
#     num = 0
#     while i <= n:
#         num = num + (1 / i)
#         i += 1
#     return num


# print(terms(5))


# def num(x: int, n: int) -> float:
#     i = 1
#     total = 0
#     y = 1
#     while i <= n:
#         total = total + (x / y)
#         y += 2
#         i += 1
#     return total


# print(num(6, 4))


# def num(x: int, n: int) -> float:
#     i = 1
#     total = 0
#     y = 1
#     while i <= n:
#         if i % 2 != 0:
#             total = total + (x**y)
#         else:
#             total = total - (x**y)

#         y += 2
#         i += 1
#     return total


# print(num(6, 4))


# def addDigits(num):
#     n = num
#     total = 0
#     while n > 0:

#         total = total + (n % 10)
#         n = n // 10
#     return total


# print(addDigits(123))


# def factorial(n):
#     i = 1
#     count = 1
#     while i <= n:
#         count = count * i
#         i += 1
#     return count


# def sumPattern(n):
#     i = 1
#     total = 0
#     while i <= n:
#         total = total + (1 / factorial(i))
#         i += 1
#     return total


# print(sumPattern(5))


# def checkPrime(n):
#     factors = 0
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             factors += 1
#         i += 1
#     if factors == 2:
#         return True

#     else:
#         return False


# def printPrimeFactors(n):
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             if checkPrime(i):
#                 print(i, end=" ")
#         i += 1
#     print()


# printPrimeFactors(20)
# printPrimeFactors(7)
# printPrimeFactors(72)
