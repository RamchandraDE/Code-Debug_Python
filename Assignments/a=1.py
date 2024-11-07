a = 1
b = 20
while a < b:
    c = 2
    while c <= a:
        if a % c == 0:
            if a == 2:
                print("number is prime: ", a)
            break
        else:
            if c == (a - 1):
                print("number is prime: ", a)
            c = c + 1

    a = a + 1
