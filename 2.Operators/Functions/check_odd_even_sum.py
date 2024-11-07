def total(num1: int, num2: int) -> int:
    total = num1 + num2
    return total


def check(num: int) -> None:
    if num % 2 == 0:
        print(f"Even")
    else:
        print(f"Odd")


num1 = int(input("enter a 1st num = "))
num2 = int(input("enter a 2st num = "))
x = total(num1, num2)
print(x)
check(x)
