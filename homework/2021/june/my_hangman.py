import random

my_list = [
    "atrocious",
    "happiness",
    "daechwita",
    "cumbersome",
    "metropolitan",
    "beauty",
    "narcisse",
    "classique",
    "cosmopolitan",
]

random_word = random.choice(my_list)
my_string = ""
for x in range(0, len(random_word)):
    my_string += "_ "
print(my_string)
n = int(input("Enter the number of guesses you want to make: "))
my_new_list = []
for element in my_string:
    my_new_list.append(element)
wrong_guess = 0
while wrong_guess < n:
    letter = input("Enter your guess: ")
    if letter in random_word:
        for index, character in enumerate(random_word):
            if character == letter:
                my_new_list[2 * index] = letter
    else:
        wrong_guess += 1
        print(f"You have done {wrong_guess} incorrect guesses till now.")
    x = ""
    for p in my_new_list:
        x += p
    print(x)
    my_list_2 = []
    for character in random_word:
        my_list_2.append(character)
        my_list_2.append(" ")
    if my_list_2 == my_new_list:
        print("you have completed the word! Congrats")
        break
else:
    print("You have completed all your guesses. Try again.")
