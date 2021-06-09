# %% [markdown]
# # Question 1:
# Show the first n elements of the fibonacci series
#
# Example:
#   - input: 7
#   - output: 0 1 1 2 3 5 8

# %%
# n = int(input("Enter number"))
n = 7
a, b = 0, 1
for _ in range(2, n):
    print(a)
    print(b)
    temp = b
    a = b
    b = a + temp

# %% [markdown]
# # Question 2:
# WAP to print the factorial of n.
#
# Example:
#   - input: 5
#   - output: 120
numeral = int(input("Enter the number which you want the factorial of."))
factorial = 1
for element in range(1, numeral + 1):
    factorial *= element
print(factorial)

# %% [markdown]
# # Question 3:
# WAP to input the value of `x` and `n` and print the sum
# of the following series.
# 1 + x<sup>1</sup> + x<sup>2</sup> + x<sup>3</sup> + .... + x<sup>n</sup>
#
# Example:
#   - input: 2, 3
#   - output: 15

# %%
x = int(input("Enter x: "))
n = int(input("enter n: "))
sum = 0
for num in range(0, n + 1):
    sum += x ** num
print(sum)

# %% [markdown]
# # Question 4:
# WAP that inputs a line of text and prints each word in a separate line. Also,
# print the total number of words in that input.
#
# Example
#
# **Input:** Python is fun.
#
# **Output**:
# ```text
#  Python
#  is
#  fun.
#  Total words: 3
# ```
my_string = input("enter string")
my_list = my_string.split()
for character in my_list:
    print(character)
print(f"Total words are {len(my_list)}")

# %% [markdown]
# # Question 5:
# WAP to calculate the sum of digits present in an input string.
#
# **Input**: hello123
#
# **Output**: 6

my_num = input("Enter your string.")
n = 0
for character in my_num:
    if character.isdigit():
        n += int(character)
print(f"the sum of all the digits in {my_num} is {n}.")
