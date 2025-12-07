# Easy 3
# 1

def repeat(string, number):
    for num in range(number):
        print(string)

repeat('Hello', 3)

# Second pass:

def repeat(string, repeats):
    for repeats in range(1, repeats + 1): # So yeah when we're dealing with repeat activities, we benefit from ranges starting at 0 and ending one before, can just do that
        print(string)

repeat('Hello', 3)

# 2

def crunch(s):
    result = ''
    for char in s:
        if not result or char != result[-1]:
            result += char
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# Second pass (same, yeah this is by far the easiest):

def crunch(s):
    result = ''
    for char in s:
        if not result or char != result[-1]: # *result* -1, not string
            result += char
    return result

# Further exploration, re.sub & itertools (I didn't know these, LSBot helped):

import re

def crunch(string):
    return re.sub(r'(.)\1+', r'\1', string)

### Or:

from itertools import groupby

def crunch(string):
    return ''.join(key for key, group in groupby(string))
    # groupby groups consecutive identical elements.
    # We take the `key` (the character) from each group.
    # ''.join() combines them back into a string.

# 3

