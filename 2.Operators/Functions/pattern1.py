# def pattern(n):
#     i = 1
#     num = 10
#     while i <= n:
#         print(num, end=" ")
#         num = num + 10
#         i += 1


# pattern(10)


# def pattern(n):
#     i = 1
#     num = 1
#     while i <= n:
#         print(num, end=" ")
#         num = num * 2
#         i += 1


# pattern(10)


# def pattern(n):
#     i = 1
#     num = 1
#     while i <= n:
#         print(num, end=" ")
#         num = (num * 10) + 1
#         i += 1


# pattern(10)


# def average():
#     total = 0
#     count = 0
#     while True:
#         num = int(input("Enter a num = "))
#         if num == 0:
#             break
#         total = total + num
#         count = count + 1
#     print(f" avg is {total/count}")


# average()


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


# def pattern(n):
#     i = 1
#     num = 1
#     while i <= n:
#         print(num + 1, end=" ")
#         num = num * 10
#         i += 1


# pattern(10)


"""i = 1
num = 0
while i <= 10:
    print(num + 1, end=" ")
    if num == 0:
        num = 10
    else:
        num = num * 10
    i += 1"""


def pat(n):
    i = 0
    num = 1
    while i < n:
        print(num, end=" ")
        if i % 2 == 0:
            num += 2
        else:
            num += 3
        i += 1


pat(10)
