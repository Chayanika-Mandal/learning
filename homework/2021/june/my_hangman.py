import random
from typing import List


def get_representation(word: List[str]):
    """
    When `word` is ['h', 'e', '', 'l', 'l', '']
    then output will be 'h e _ l l _'
    """
    string = ""
    for character in word:
        if character != "":
            string += character
        else:
            string += "_"
    string = " ".join(list(string))
    return string


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

random_word = list(random.choice(my_list))

guessed = ["" for _ in range(0, len(random_word))]

total_guesses = int(input("Enter the number of guesses you want to make: "))

wrong_guess = 0

while wrong_guess < total_guesses:
    letter = input("\nEnter your guess: ")
    if letter in random_word:
        for index, character in enumerate(random_word):
            if character == letter:
                guessed[index] = letter
    else:
        wrong_guess += 1
        print(f"You have done {wrong_guess} incorrect guesses till now.")
    print((get_representation(guessed)))

    if guessed == random_word:
        print("You have completed the word! Congrats!")
        break
else:
    print("You have completed all your guesses. Try again.")
