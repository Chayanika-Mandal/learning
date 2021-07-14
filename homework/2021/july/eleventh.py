# %%
string = "hello"

for element in string:
    print(ord(element))

# %%
# # Question 1:
# Find the next string of a given string. Assume that all the input characters
# will be in uppercase.


def function(string: str) -> str:
    my_list = []
    for index, character in enumerate(string):
        my_list.append(character)
    for index, character in enumerate(my_list):
        if index == len(my_list) - 1:
            if character != "Z":
                ascii_val = ord(character) + 1
                my_list[index] = chr(ascii_val)
            else:
                ascii_val = ord(character) - 25
                my_list[index] = chr(ascii_val)
                ascii_val = ord(character) + 1
                my_list[index - 1] = chr(ascii_val)
        for index, character in enumerate(my_list):
            if ord(character) > 90:
                if index != 0:
                    ascii_val = ord(character) - 26
                    my_list[index] = chr(ascii_val)
                    ascii_val = ord(character) + 1
                    my_list[index - 1] = chr(ascii_val)
                else:
                    my_list.insert(0, "A")
    return my_list


print(function("ZZZZ"))


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
