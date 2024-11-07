my_string = "python is good"

x = list(my_string)
print(x)

r = "".join(i for i in x[::-1])
print(r)
