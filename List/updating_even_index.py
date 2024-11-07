# Using Fucnion
from typing import List


def evenIndedxUpdate(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0


my_list = [54, 43, 19, 85, 11, 94, 32]
evenIndedxUpdate(my_list)
print(my_list)
# Output = [ 0,43, 0, 85, 0, 94, 0]
