from typing import Tuple


# def fourthElement(tup: Tuple) -> None:
#     if len(tup) < 4:
#         print("Not Enough elements")
#         return

#     print(tup[-4])


# fourthElement((1, 2, 3))
# fourthElement((54, 2, 34, 55, 67, 78))


# def repetedItem(tup: Tuple):
#     repeted_elements = []
#     for i in range(len(tup)):
#         if tup[i] in tup[i + 1 :] and tup[i] not in repeted_elements:
#             repeted_elements.append(tup[i])

#     return repeted_elements


# my_tuple = (1, 2, 3, 2, 4, 3, 5, 6, 4)
# repeted = repetedItem(my_tuple)
# if len(repeted) > 0:
#     print(f"Repeted items = {repeted}")
# else:
#     print("No repeted elements found")

""" check element exists
    ask from user
    if tuple existe print YES"""


# def checkExist(element, t):
#     return element in t


# my_tup = (1, 2, 3, 4, 5)

# e = int(input("Enter a num = "))

# if checkExist(e, my_tup):
#     print("YES")

# else:
#     print("NO")


# def reverseTuple(t: Tuple):

#     return tuple(reversed(t))


# my_tuple = (1, 2, "ram", False, "OK")

# r = reverseTuple(my_tuple)
# print(r)


# def checkLetter(my_string):
#     isletter = False
#     isNumber = False

#     for ch in my_string:
#         ascii_code = ord(ch)
#         if ascii_code >= 48 and ascii_code <= 57:
#             isNumber = True
#         elif (ascii_code >= 65 and ascii_code <= 90) or (
#             ascii_code >= 97 or ascii_code <= 122
#         ):
#             isletter = True

#     return isletter and isNumber


# print(checkLetter("abc#$#1d"))


# def printFirstandLast(string):
#     if len(string) < 2:
#         print("Not enough characters")
#         return
#     print(string[:2] + string[-2:])


# printFirstandLast("code")
# printFirstandLast("aeroplane")
# printFirstandLast("c")


# def secondHalf(string):
#     length = len(string)
#     return string[length // 2 + 1 :]


# print(secondHalf("Ramacha"))


# def secondHalfString(string: str) -> str:
#     length = len(string)
#     return string[length // 2 + 1 :]


# print(secondHalfString("aeroplane"))
# print(secondHalfString("delhi"))
# print(secondHalfString("pavbhaji"))


# def countAlphabet(string):
#     count = 0
#     for ch in string:
#         if ch.isalpha():
#             count += 1
#         return count


# print(countAlphabet("Ramachandraredd y"))
# print(countAlphabet("Rchandrare"))


# def countSpaces(string):
#     count = 0
#     for ch in string:
#         if ch == "a":
#             count += 1
#     return count


# print(countSpaces("Rama chandra Reddy Karnati"))


def countNot(string):
    count = 0
    for ch in string:
        if not ch.isalpha():
            count += 1
    return count


print(countNot("a bv ^$*"))
