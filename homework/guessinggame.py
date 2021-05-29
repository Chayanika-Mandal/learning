from random import randrange
n = randrange(101)
num = int(input("Guess a number between 0 and 100.\n"))
while num != n:
    if num > n:
        num = int(input("too large.\n"))
    elif num < n:
        num = int(input("too small.\n"))
    if num == n:
        print("success")

