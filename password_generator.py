# WAF to generate a random alphabetical string and alphabetical string of a
# fixed length.

import random
import string

LETTERS = string.ascii_letters + string.digits


def password_generator(length):
    my_string = ""
    for _ in range(0, length):
        n = random.randrange(0, len(LETTERS))
        nth_char = LETTERS[n]
        my_string += nth_char
    return my_string


def test_function():
    assert password_generator(4) != password_generator(4)
    assert len(password_generator(4)) == 4
    assert password_generator(10) != password_generator(10)
    assert len(password_generator(10)) == 10
