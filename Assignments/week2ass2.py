# without Annotations
"""def large_num(num1=None, num2=None, num3=None) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2

        else:
            return num3
    else:
        return -1


x = large_num(3, 4, 1)

print(f"{x} is the large number")


# With Annotations


def largest2(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3

    else:
        return -1


print(largest2(3, 4, 1))"""


"""def twofun(base: float, exponent: float) -> float:
    return base**exponent


##x = twofun(10, 5)
# print(x)

base_val = 2
exp_val = 4
result_val = twofun(base_val, exp_val)
print(f"{base_val} raised to the power of {exp_val} is {result_val}")"""


"""


def middle_num(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    else:
        return num3


def check(num: int) -> bool:
    return num % 3 == 0 and num % 4 == 0


num1: int = int(input("Enter 1st num = "))
num2: int = int(input("Enter 2st num = "))
num3: int = int(input("Enter 3st num = "))

x = middle_num(num1, num2, num3)
print(x)
check(x)

if check(x):
    print(f"{x} is divisible by both 3 and 4.")
else:
    print(f"{x} is not divisible by both 3 and 4")"""


"""def input_num(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3


def check_avg(avge: float, fourth_num: int) -> bool:
    return avge >= fourth_num


num1: int = int(input("Enter 1st num = "))
num2: int = int(input("Enter 2st num = "))
num3: int = int(input("Enter 3st num = "))
num4: int = int(input("Enter 4st num = "))

x: float = input_num(num1, num2, num3)

result = check_avg(x, num4)

print(f"The avg of {num1}, {num2} and {num3} is: {x}")

if result:
    print(f" The avg if greater tha or equal to {num4}")
else:
    print(f"The avg is less than {num4}")"""


def avg_num(num1: int, num2: int, num3: int) -> float:
    return num1 + num2 + num3 / 3


def check_avg(avge: int, fourth: int) -> bool:
    return avge >= fourth


num1: int = int(input("Enter 1st num = "))
num2: int = int(input("Enter 2st num = "))
num3: int = int(input("Enter 3st num = "))
num4: int = int(input("Enter 4st num = "))

x: float = avg_num(num1, num2, num3)
result = check_avg(x, num4)

print(f"The avg of {num1}{num2}{num3} is equal to {x:.2f}")

if result:
    print(f"The avg if gretaer than or equal to {num4}")
else:
    print(f"The avg is less than {num4}")
