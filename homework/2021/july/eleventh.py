# %%
# # Question 1:
# Find the next string of a given string. Assume that all the input characters
# will be in uppercase.
import string

UPPERCASE = list(string.ascii_uppercase)


def get_next(letter):
    new_index = UPPERCASE.index(letter) + 1
    try:
        return UPPERCASE[new_index]
    except IndexError:
        return "A"


def function(letters):
    listed = list(reversed(list(letters)))
    new = []
    if letters[-1] != "Z":
        new = list(letters)
        new[-1] = get_next(new[-1])
    else:
        carry = 0
        for letter in listed:
            next_letter = get_next(letter)
            if next_letter == "A":
                carry = 1
                new.insert(0, next_letter)
                continue
            if carry == 1:
                carry = 0
                new.insert(0, next_letter)
            else:
                new.insert(0, letter)
        if letters[0].upper() == "Z":
            new.insert(0, "A")
    return "".join(new)


function("ZZ")


def test_function():
    assert function("A") == "B"
    assert function("Z") == "AA"
    assert function("ZZZZ") == "AAAAA"
    assert function("ZAABF") == "ZAABG"
    assert function("CDA") == "CDB"
    assert function("BAZ") == "BBA"
    assert function("ABC") == "ABD"
    assert function("BZZ") == "CAA"
    assert function("A") == "B"
    assert function("Z") == "AA"
    assert function("ZZ") == "AAA"
    assert function("L") == "M"
    assert function("CDA") == "CDB"
    assert function("ZZZZ") == "AAAAA"


# %%
# # Question 2:
# Given two strings, s1 and s2, create a new string by appending s2 in the
# middle of s1.
# s1 = "Ault"
# s2 = "Kelly"
# output = "AuKellylt"
s1 = "Ault"
s2 = "Kelly"
s1_list = []
for character in s1:
    s1_list.append(character)
s1_list.insert(len(s1) // 2, s2)
print(s1_list)
s1_new = ""
for element in s1_list:
    s1_new += element
print(s1_new)

# %%
