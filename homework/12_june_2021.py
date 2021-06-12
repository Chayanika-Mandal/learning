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


def function_1():
    pass


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


def function_2():
    pass


@pytest.mark.xfail
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


def function_3():
    pass


@pytest.mark.xfail
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


def function_4():
    pass


@pytest.mark.xfail
def test_function_4():
    assert function_4("the quick brown fox jumped over the lazy dog") is True
    assert function_4("random") is False


# %% [markdown]
# # Question 5:
# WAF called `function_5` to accept a variable number of arguments and return
# their average.
#
# - Input: `function_5(1, 2, 3, 4)`
# - Output: 2.5


def function_5():
    pass


@pytest.mark.xfail
def test_function_5():
    assert function_5(1, 2, 3, 4) == 2.5
    assert function_5(3) == 3
    assert function_5(2, 10) == 6
