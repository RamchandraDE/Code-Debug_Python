f = open("/Users/r-c-r/Downloads/PYTHON_DSA/15. File_Handling/hello.txt", "r")
x = f.read()


count = 0
for ch in x:
    count += 1
print(count)
f.close()
