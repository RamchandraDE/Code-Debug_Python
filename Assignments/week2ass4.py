# def factorial():
#     num = int(input("Enter a num = "))
#     return num**num


# x = factorial()
# print(x)


# def factorial(n):
#     result = 1
#     i = 1
#     while i <= n:
#         result = result * i
#         i += 1
#     return result


# result = factorial(4)
# print(result)


# def pattern(n):
#     i = 1
#     num = 10
#     while i <= n:
#         print(num, end=" ")
#         num = num + 10
#         i = i + 1
#     print()


# pattern(5)


# def pattern(n):
#     i = 1
#     num = 1
#     while i <= n:
#         print(num, end=" ")
#         num = num * 2
#         i = i + 1
#     print()


# pattern(7)


# def pattern(n):
#     i = 1
#     num = 1
#     while i <= n:
#         print(num, end=" ")
#         num = (num * 10) + 1
#         i += 1
#     print()


# pattern(int(input("Enter a num = ")))


# def average():
#     total = 0
#     count = 0
#     while True:
#         num = int(input("Enter a num = "))
#         if num == 0:
#             break
#         total = total + num
#         count = count + 1
#     print(f"Avg of all num = {total/count}")


# average()


def pattern(n):
    i = 1
    while i <= n:
        print(i**2, end=" ")
        i += 1
    print()


pattern(10)
