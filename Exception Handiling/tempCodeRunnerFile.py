try:
    my_list = [23, 45, 2, 45, 67]
    index = int(input("Enter a num = "))
    print(my_list[index])
except IndexError:
    print("Index out of range")
except:
    print("Some error occurred")