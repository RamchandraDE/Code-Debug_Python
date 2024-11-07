# Is used to create list


def prime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [i for i in range(2, 101) if prime(i) == True]
print(my_list)
