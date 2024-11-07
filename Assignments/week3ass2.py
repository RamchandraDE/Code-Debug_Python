# Ques 1
# def patt(n):
#     for i in range(1, n + 1):
#         for j in range(n - i):
#             print(" ", end=" ")
#         for k in range(i, 0, -1):
#             print(k, end=" ")

#         print()


# patt(5)

# Ques 2


# def patt(n):
#     for i in range(n, 0, -1):
#         for j in range(i - 1):
#             print(" ", end=" ")
#         for k in range(n, i - 1, -1):
#             print(k, end=" ")
#         print()


# patt(5)


# def patt(n):
#     for i in range(1, n + 1):
#         for j in range(n - i):
#             print(" ", end=" ")
#         for k in range((2 * i) - 1):
#             print(i, end=" ")
#         print()


# def fun(n):
#     for i in range(n, 0, -1):
#         for j in range(n, i - 1, -1):
#             print(" ", end=" ")
#         for k in range((2 * i) - 1):
#             print(i, end=" ")
#         print()


# patt(5)
# fun(4)


def pat(n):
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for k in range(n // 2, -1, -1):
        for l in range(1, k + 1):
            print(l, end=" ")
        print()


pat(13)
