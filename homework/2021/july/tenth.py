# %% [markdown]
# # Question 1:
# WAP to cycle through two lists of unequal length.
list_1 = ["yes", "no"]
list_2 = [1, 2, 3, 4, 5, 6]
# Your output should be
# 1yes
# 2no
# 3yes
# 4no
# 5yes
# 6no
for index, character in enumerate(list_2):
    num = index % len(list_1)
    character = str(character)
    character += str(list_1[num])
    print(character)

# %% [markdown]
# WAP to find the number of zeroes at the end of a factorial.
my_number = int(input("Write the number of which you require the factorial."))
factorial = 1
for number in range(1, my_number + 1):
    factorial *= number
factorial = str(factorial)
factorial_without_zeroes = factorial.rstrip("0")
print(
    f"The number of zeroes at the end of the factorial is {len(factorial) - len(factorial_without_zeroes)}"
)

# %%
# WAP to find the number of zeroes at the end of a factorial. Use another method.
my_number = int(input("Write the number of which you require the factorial."))
zeroes = 0
for integer in range(1, my_number // 5 + 1):
    zeroes += my_number // 5 ** integer
print(zeroes)
#%%
my_list = [0, -1, -2, 1, 2, 3, -5]


def fn1(num):
    if num == 0:
        return True
    else:
        return False


my_list = list(filter(lambda integer: integer == 0, my_list))
print(my_list)

# %%
