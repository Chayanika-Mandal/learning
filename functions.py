# %% [markdown]
# A function is a set of instructions that is stored in an identifier and can
# be reused across the program.
#
# The syntax of defining a function is:
# ```python
# def <FUNCTION_NAME>([arguments[, optional-arguments]]):
#   STATEMENTS
#   [return]
# ```
#
# To call a function, simply write its name, followed by parenthesis
# and optional args and kwargs.
# ```python
#  <FUNCTION_NAME>([arguments[, optional-arguments]])

# The Importance of Python Functions
# 1. Abstraction and Reusability
# 2. Modularity
# 3. Namespace Separation

# %%
# The simplest possible function
def say_hello():
    print("Hello There!")


say_hello()


# %%
# A function that accepts arguments
def say_hi(first_name, last_name):  # name = "Diptesh"
    print(f"Hi {first_name}, how are you?")
    print(first_name + " " + last_name)


say_hi("Diptesh", "Choudhuri")


# Abstraction and re-usability
# %%
def say_hi(first_name, last_name, age=12):
    """
    This function says hi and prints information about a person.
    """
    print(f"Hi {first_name}, how are you?")
    print(first_name + " " + last_name + ", Age:" + str(age))


say_hi("Diptesh", "Choudhuri", 19)

say_hi("Chayanika", "Mandal")


# %% [markdown]
# A function is also allowed to **return** values from inside it. But the
# returned values MUST be in the scope of the function.
# A `return` statement ALWAYS stops the execution of a function.

# %%
def get_full_name(first_name, last_name):
    """This function takes in a first_name and a last_name
    and concatenates (adds) them to generate the full name and
    returns it"""
    full_name = first_name + " " + last_name
    return full_name


o = get_full_name("Diptesh", "Choudhuri")
print(o)


# %%
def f():
    s = "-- Inside f()"
    print(s)


print("Before calling f()")
f()
print("After calling f()")


# %%
def say_age(age):
    print("we have entered the function")
    if type(age) is not int:
        raise ValueError(f"`age` expected type {int}, got {type(age)}")
    if age == 15:
        return "You are 15 years old"
    elif age > 15:
        return "You are more than 15 years old"
    else:
        return "You are less than 15 years old"


variable = say_age(23)
print(variable)


# %%
def return_some_str():

    return "hello "


p = return_some_str().title()
print(p)


# %%
def double(x):
    print(x * 2)
    # return x * 2


x = 5
x = double(x)
print(x)


# %%
def average(*args):
    for element in args:
        if type(element) == str:
            raise TypeError(f"Expected type {int}, got {type(element)}")
    return sum(args) / len(args)


print(average(1, 2, 3, 5))
print(average(1, 2, 3, "hello"))


# %%
def func(a, b, c, *args):
    print(a, b, c, args)


func(1, 2, 4, 5, 6, 7, 8)
