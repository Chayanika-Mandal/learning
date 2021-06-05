# %%
# Question 1:
# Write a program that reads a string and displays the longest substring of
# the given string having just the consonants.

string = input("What is the input string? ")
mylist = string.split()
mysecondlist = []
for element in mylist:
    if "a" and "e" and "i" and "o" and "u" not in element:
        mysecondlist.append(element)
mythirdlist = []
for substring in mysecondlist:
    mythirdlist.append(len(substring))
mythirdlist = mythirdlist.sort()
for component in mysecondlist:
    if len(component) == mythirdlist[len(mythirdlist) - 1]:
        print(component)




# %%
# Question 2:
# WAP that reads a string and then prints a string that capitalizes every
# alternate character. Example: `pasSion` becomes `pAsSiOn`.
mystring = input("Enter string")
slice1 = mystring[::2]
slice2 = mystring[1::2]
slice3 = slice1.swapcase()
print(slice3)
newstring = ("")
for index in range(0, len(slice1)-1):
    newstring += slice3[index]
    newstring += slice2[index]
if len(mystring)%2 == 1:
    newstring += slice3[len(slice3) - 1]
print(newstring)
# %%
