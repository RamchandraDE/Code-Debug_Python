# def printNum(n1, n2):
#     if n1 < n2:
#         i = n1
#         while i <= n2:
#             print(i, end=" ")
#             i += 1
#         print()
#     elif n2 < n1:
#         i = n2
#         while i <= n1:
#             print(i, end=" ")
#             i += 1
#         print()

#     else:
#         print(n1)


# printNum(50, 30)

"""OR"""

def printNum(n1, n2):
    start = n1 if n1 < n2 else n2
    end = n2 if n1 < n2 else n1
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printNum(30, 20)
