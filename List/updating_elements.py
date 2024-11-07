from typing import List


def xyz(a: List) -> None:
    print(id(a))
    a[0] = 100


a: List = [43, 54, 65, 32, 111]
print(id(a))

xyz(a)
print(a)
