# %% [markdown]
# # Question 1:
# WAP to append a user input string to the end of a file.
user_input = input("Input your string")
with open("fourth.txt", "a") as my_file:
    my_file.write(user_input)

# %% [markdown]
# # Question 2:
# WAP to read a file and then write the contents of that file in the reversed
# order to the same file.
with open("fizzbuzz.txt", "r") as file:
    contents = file.read()
    reversed_contents = list(contents)
    reversed_contents.reverse()
    reversed_contents_string = "".join(reversed_contents)
with open("fizzbuzz.txt", "w") as file:
    file.write(reversed_contents_string)
# %% [markdown]
# # Question 3:
# You have to convert the contents of `fourth.txt` to a python list.
# %%
with open("fourth.txt", "r") as file:
    contents = file.read()
    contents = contents.strip("[")
    contents = contents.strip("]")
    contents = contents.split(", ")
    for index, element in enumerate(contents):
        if element.isdigit():
            contents[index] = int(element)
        else:
            contents[index] = element.strip('"')

    print(contents)

# %% [markdown]
# # Question 4:
# You have to write the result of FizzBuzz game to a file called `fizzbuzz.txt`
with open("fizzbuzz.txt", "w") as fizzbuzz:
    for integer in range(1, 101):
        temp = ""
        if integer % 3 == 0:
            temp += "Fizz"
        if integer % 5 == 0:
            temp += "Buzz"
        if temp == "":
            temp = str(integer)
        fizzbuzz.write(temp + "\n")
        # if integer % 3 == 0:
        #     if integer % 5 == 0:
        #         fizzbuzz.write("fizzbuzz\n")
        #     else:
        #         fizzbuzz.write("fizz\n")
        # elif integer % 5 == 0:
        #     fizzbuzz.write("buzz\n")
        # else:
        #     fizzbuzz.write(str(integer))
        #     fizzbuzz.write("\n")

# %%
