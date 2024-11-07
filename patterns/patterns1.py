# Nested Loops

# for i in range(5, 0, -1):
#     for j in range(5, 0, -1):
#         print(i, end=" ")

#     print()


# def pattern(n):
#     for i in range(1, n + 3):
#         for j in range(1, i + 1):
#             print(i, end=" ")
#         print()


# pattern(4)


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(10)
