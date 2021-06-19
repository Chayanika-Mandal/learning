import pytest


# %% [markdown]
# # Question 1:
# WAF to return the frequency of each character in a string.
def function_1(string):
    pass


@pytest.mark.xfail
def test_function_1():
    assert function_1("Hello") == {"H": 1, "e": 1, "l": 2, "o": 1}
    assert function_1("YAY 2") == {"Y": 2, "A": 1, "2": 1, " ": 1}


# %% [markdown]
# # Question 2:
# WAF to create a third dictionary from two dictionaries having common keys.
# in a way so that values of common keys are added in the third dictionary.
def function_2(dict1, dict2):
    pass


@pytest.mark.xfail
def test_function_2():
    assert function_2({"a": 200}, {"a": 100, "b": 200}) == {"a": 300, "b": 200}
    assert function_2(
        {"1": 100, "2": 200, "3": 300}, {"1": 300, "2": 200, "5": 400}
    ) == {"1": 400, "2": 400, "3": 300, "5": 400}


# %%
# Question 3:
# WAF to find the highest 2 values in a dictionary
def function_3(dict1):
    pass


def test_function_3():
    assert function_3({31: 111, 22: 222, 43: 455, 25: 555}) == (555, 455)
    assert function_3({1131: 111, 222: 222, 453: 555, 25: 555}) == (555, 555)
