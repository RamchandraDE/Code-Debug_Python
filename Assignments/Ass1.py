'''a = 5
b = 10

# print(a > 5 and b >= 10)
# F T = F

# print(a >= 5 or NOT b > 10)

# T T = T

# print(not(a>5 and b > 5))
# T F = F

# print(not (a < 10 or not b < 10))

# F F = F

# print(not(not a <= 5 or not b >= 10))

# T or R = t

"""user = float(input("Enter a kilomerter = "))
user = user * 0.609
print(user)"""

num1 = int(input("Enter a number1 = "))
num2 = int(input("Enter a number2 = "))
num3 = int(input("Enter a number3 = "))

total = num1 + num2 + num3

avg = total / 3

print(f"the avg of {num1}, {num2}, {num3} is {avg}")


person = int(input("Enter rupee's = "))

convert = person * 100
print(f"rupee {person} is equal to {convert}")

square = float(input("Enter a number = "))

side = square**2

print(side)'''

games_played = int(input("Num of game played = "))
games_won = int(input("Num of games won = "))
games_lost = int(input("Num of games lost = "))

games_tied = games_played - games_won - games_lost

total_points = (games_won * 4) + (games_tied * 2)

print(f"num of ties {games_tied}")
print(f"total points: {total_points}")

num = int(input("Enter a num = "))

if num % 3 == 0:
    print(f"{num} is divisible by 3.")
else:
    print(f"{num} is not div by 3")



user = int(input("Enter a num = 0"))

if user % 2 == 0:
    print(f"{user} is ODD")

else:
    print(f"{user} is even")

 length = float(input("enter a len = "))
 breadth = float(input("enter a breadth = "))

if length == breadth:
   print("It's a square")

else:
   print("it's a rectangle")