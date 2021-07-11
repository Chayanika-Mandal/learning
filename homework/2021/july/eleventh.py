# %%
string = "hello"

for element in string:
    print(ord(element))

# %%
# # Question 1:
# Find the next string of a given string. Assume that all the input characters
# will be in uppercase.


def function(string: str) -> str:
    pass


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
