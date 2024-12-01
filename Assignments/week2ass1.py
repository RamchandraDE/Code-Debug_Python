# def maxi(num1, num2, num3):
#     result = max(num1, num2, num3)
#     print(f"{result} is the max number")


# def mini(num1, num2, num3):
#     result = min(num1, num2, num3)
#     print(f"{result} is the min number")


# num1 = 37
# num2 = 59
# num3 = 12

# maxi(num1, num2, num3)
# mini(num1, num2, num3)


def maxi(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the max num")
    elif b >= c:
        print(f"{b} is max value")
    else:
        print(f"{c} is the max value")


def mini(a, b, c):
    if a <= b and a <= c:
        print(f"{a} is the minimum number")
    elif b <= c:
        print(f"{b} is the minimum value")
    else:
        print(f"{c} is the minimum value")


num1 = 44
num2 = 54
num3 = 432

maxi(num1, num2, num3)
mini(num1, num2, num3)
