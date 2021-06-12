# %% [markdown]
# # Question 1
# WAF to interchange the last two elements of an interable.
#
# 1. Input: `['1', 34, 'hello']`
#
#    Output: `['hello', 34, '1']`
#
# 2. Input: `'hello world'`
#
#    Output: `'dello worlh'`

# 3. Input: `(1, 2, 3, 5)`
#
#    Output: `(5, 2, 3, 1)`
my_list = ["hello", "my", "world"]
def interchange(my_list = my_list):
    my_list.insert(0, my_list[len(my_list) - 1])
    my_list.pop()
    my_list.insert(len(my_list), my_list[1])
    del my_list[1]
    print(my_list)
interchange()


def interchange_2(mystring):
    my_list_3 = mystring.split()
    my_list_3.insert(0, my_list_3[len(my_list_3) - 1])
    my_list_3.pop()
    my_list_3.insert(len(my_list_3), my_list_3[1])
    del my_list_3[1]
    print(my_list_3)
interchange_2('hello world')

def interchange_3(my_string):
    my_list_3 = []
    for element in my_string:
        my_list_3 += element
    my_list_3.insert(0, my_list_3[len(my_list_3) - 1])
    my_list_3.pop()
    my_list_3.insert(len(my_list_3), my_list_3[1])
    del my_list_3[1]
    my_string_2 = ""
    for character in my_list_3:
        my_string_2 += character
    print(my_string_2)
interchange_3("hello world")


# %% [markdown]
# # Question 2
# WAF to find the number of even and odd elements in a list of
# integers.
#
# Input: `[1, 2, 3, 4, 7]`
#
# Output: `Even: 2, Odd: 3`
 
my_list_2 = [1, 2, 3, 4, 5]
def finding_odd_even(my_list_2):
    n = 0
    for element in my_list_2:
        if element % 2 == 1:
            n += 1
    print(f"the number of odd integers in the list is {n}.")
    print(f"The number of even integers in the list is {len(my_list_2) - n}")
finding_odd_even(my_list_2)
# %%
