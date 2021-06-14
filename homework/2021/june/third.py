# %%
# Question 1:
# Write a program that reads a string and displays the longest substring of
# the given string having just the consonants.

# string = input("What is the input string? ")

string = "myh Ello nae is faeiou BRT I ghy"

list_of_consonants = list()  # []

temporary = ""
for index, character in enumerate(string):
    if character == " ":
        continue
    if character.lower() not in ["a", "e", "i", "o", "u"] and not character.isdigit():
        temporary += character
        if index == len(string) - 1:
            list_of_consonants.append(temporary)
    else:
        if temporary:
            list_of_consonants.append(temporary)
        temporary = ""

# method 1: is capable of giving only one answer
# %%
length = 0
required_index = 0
for index, substring in enumerate(list_of_consonants):
    if len(substring) > length:
        required_index = index
        length = len(substring)

print(f"One possible output is: {list_of_consonants[required_index]}")

# method 2: is capable of giving multiple answers
# %%
list_of_consonants.sort(key=len, reverse=True)
for substring in list_of_consonants:
    if len(substring) == len(list_of_consonants[1]):
        print(f"One possible output is: {substring}")

# %%
# Question 2:
# WAP that reads a string and then prints a string that capitalizes every
# alternate character. Example: `pasSion` becomes `pAsSiOn`.
mystring = input("Enter string")
slice1 = mystring[::2]
slice2 = mystring[1::2]
slice3 = slice1.swapcase()
print(slice3)
newstring = ""
for required_index in range(0, len(slice1) - 1):
    newstring += slice3[required_index]
    newstring += slice2[required_index]
if len(mystring) % 2 == 1:
    newstring += slice3[len(slice3) - 1]
print(newstring)
