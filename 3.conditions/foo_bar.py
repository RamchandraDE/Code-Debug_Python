"""
Ask  a num from from user

if num is div by 3 - FOO
if num is div by 5 - BAR
if num is div by 3 and 5 - FOOBAR

ELSE:
FOOFOOBARBAR
"""

num: int = int(input("Enter a num = "))

if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 5 == 0:
    print("BAR")
elif num % 3 == 0:
    print("FOO")

else:
    print("FOOFOOBARBAR")
