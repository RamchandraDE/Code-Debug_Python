# my_list = [2, 3.75, 0.04, 59, 354, 6, 7.777, 8, 9]

# a = 5
# if type(a) == int:
#     print("Yes")

# else:
#     print("No")

# lst = [2, 3.75, 0.04, 59, 354, 6, 7.777, 8, 9]

# only_int = [i for i in lst if type(i) == int]
# only_float = [i for i in lst if type(i) == float]

# print(only_int)
# print(only_float)


# def checkdiv(n: int) -> bool:
#     if n % 2 == 0 and n % 3 == 0:
#         return True
#     else:
#         return False


# my_list = [i for i in range(1, 51) if checkdiv(i) == True]

# print(my_list)


def prime(n: int) -> bool:
    fact = 0
    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1
    if fact == 2:
        return True
    else:
        return False


a = [i for i in range(1, 51) if prime(i) == True]
print(a)
