# try:
#     a = 5
#     b = 0
#     print(a / b)
# except:
#     print("some error occured")

# print("----")
# # print(5 / 1)


try:
    my_list = [23, 45, 2, 45, 67]
    index = int(input("Enter a num = "))
    print(my_list[index])
except IndexError:
    print("Index out of range")
except:
    print("Some error occurred")
# my = {"name": "ram", "age": 56, "gender": "male"}
# try:

#     key_name = input("Enter Key = ")
#     print(my[key_name])
# except KeyError:
#     print(f"{key_name} is not present in the dictionary ")
# except:
#     print(f"Kuch aur error hai")
