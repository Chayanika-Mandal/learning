import pytest


# %% [markdown]
# # Sample
# WAF that returns the sum of its two arguments
def sample(a, b):
    return a + b


def test_sample():
    assert sample(2, 5) == 7
    assert sample(8, 0) == 8


# %% [markdown]
# # Question 1:
# WAF called `function_1` to check whether a number is in a given range or not.
#
# - Input: `function_1(3, 10, 5)`
# - Output: `True`
#
#
# - Input: `function_1(1, 10, -1)`
# - Output: `False`


def function_1(a, b, c):
    if a < b and c < b and c > a:
        return True
    elif b < a and b < c and a > c:
        return True
    else:
        return False


def test_function_1():
    assert function_1(3, 10, 5) is True
    assert function_1(1, 10, -1) is False


# %% [markdown]
# # Question 2:
# WAF called `function_2` that takes a list and returns a new list with unique
# elements of the first list.
#
# - Input: `function_2(['hello', 1, 2, 1, 1, 'hello', 'hi'])`
# - Output: `['hello', 1, 2, 'hi']`


def function_2(my_list):
    if type(my_list) is not list:
        raise TypeError(f"Expected type {list}, got {type(my_list)}")
    else:
        new_list = []
        for character in my_list:
            if character not in new_list:
                new_list.append(character)
        return new_list


def test_function_2():
    assert function_2(["h", 1, 2, 1, 1, "h", "hi"]) == ["h", 1, 2, "hi"]
    assert function_2([1, 2, 3]) == [1, 2, 3]


# %% [markdown]
# # Questions 3:
# WAF called `function_3` to check if a number is perfect or not.
#
# - Input: `function_3(6)`
# - Output: `True`
#
#
# - Input: `function_3(28)`
# - Output: `True`
#
#
# - Input: `function_3(5)`
# - Output: `False`


def function_3(num):
    if type(num) is not int:
        raise TypeError(f"Expected type {int}, got {type(num)}")
    sum = 0
    for any_integer in range(1, num):
        if num % any_integer == 0:
            sum += any_integer
    if sum == num:
        return True
    else:
        return False


def test_function_3():
    assert function_3(6) is True
    assert function_3(28) is True
    assert function_3(5) is False


# %% [markdown]
# # Question 4:
# WAF called `function_4` to check if the given input string is a pangram or
# not. Pangrams are words or strings which contain every letter of the
# alphabet at-least once.
#
# - Input: `function_4('the quick brown fox jumped over the lazy dog')`
# - Output: `True`


def function_4(my_panagram):
    my_alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    my_panagram_2 = my_panagram.lower()
    for alphabet in my_alphabet:
        if alphabet not in my_panagram_2:
            return False
    return True


def test_function_4():
    assert function_4("the quick sly brown fox jumped over the lazy dog") is True
    assert function_4("random") is False


# %% [markdown]
# # Question 5:
# WAF called `function_5` to accept a variable number of arguments and return
# their average.
#
# - Input: `function_5(1, 2, 3, 4)`
# - Output: 2.5


def function_5(*args):
    sum = 0
    for element in args:
        if type(element) == int:
            sum += element
        else:
            raise TypeError(f"args expected {int} found {type(element)}")
    return sum / len(args)


def test_function_5():
    assert function_5(1, 2, 3, 4) == 2.5
    assert function_5(3) == 3
    assert function_5(2, 10) == 6
