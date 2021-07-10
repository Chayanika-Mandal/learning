# %% [markdown]
# # Question 1:
# WAP to count the frequency of each word in a file.
with open("seventh.txt", "r") as file:
    contents = file.read()
    contents_list = contents.split(" ")
    new_contents_list = []
    for content in contents_list:
        if "." in content:
            content = content.split(".")
        if str(content).isalpha():
            new_contents_list.append(content)
        else:
            for character in content:
                new_word = ""
                if str(character).isalpha():
                    new_word += character
            new_contents_list.append(content)
    my_dict = {}
    for character in contents_list:
        my_dict[character] = contents_list.count(character)
        print(my_dict)
# %% [markdown]
# # Question 2:
# WAP to choose a random word from a file.
import random

with open("seventh.txt", "r") as file:
    contents = file.read()
    contents_list = contents.split(" ")
    random_word = random.choice(contents_list)
    print(random_word)

# %% [markdown]
# # Question 3:
# WAP to combine each word from first list with the corresponding word in
# second list.
#
# Input:
# first = ["hello", "hi", "how"]
# first = ["key", "mouse", "pop", "wire", "wifi"]
#
# Output:
# hellokey
# himouse
# howpop
# wire
# wifi
first = ["hello", "hi", "how"]
second = ["key", "mouse", "pop", "wire", "wifi"]
my_list = []
for index, word in enumerate(first):
    if index < len(second):
        string = word + second[index]
        my_list.append(string)
    else:
        my_list.append(word)
for index, word in enumerate(second):
    if index < len(first):
        string = first[index] + word
    else:
        string = word
    if string not in my_list:
        my_list.append(string)
for element in my_list:
    print(element)

# %%
