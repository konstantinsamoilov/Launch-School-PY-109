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

def print_in_box(s):
    horizontal = '+' + ('-' * (len(s) + 2)) + '+'
    message_line = f'| {s} |'
    empty = '| ' + ' ' * len(s) + ' |'
    
    print(horizontal)
    print(empty)
    print(message_line)
    print(empty)
    print(horizontal)

# Second pass:

def print_in_box(string):
    print('+' + '-' * (len(string) + 2) + '+')
    print('|' + ' ' * (len(string) + 2) + '|')
    print('|' + ' ' + string + ' ' + '|')
    print('|' + ' ' * (len(string) + 2) + '|')
    print('+' + '-' * (len(string) + 2) + '+')

# Further exploration 1 first pass:

def print_in_box(s, width = None):
    if width is None:
        inner_content_width = len(s)
    else:
        inner_content_width = max(0, width - 4)
        
    content = s[:inner_content_width]
        
    horizontal = '+' + ('-' * (inner_content_width + 2)) + '+'
    message_line = '| ' + content.ljust(inner_content_width) + ' |'
    empty = '| ' + ' ' * inner_content_width + ' |'
        
    print(horizontal)
    print(empty)
    print(message_line)
    print(empty)
    print(horizontal)

# Further exploration 1 second pass:

def print_in_box(string, width=None):
    if width is None:
        print('+' + '-' * (len(string) + 2) + '+')
        print('|' + ' ' * (len(string) + 2) + '|')
        print('|' + ' ' + string + ' ' + '|')
        print('|' + ' ' * (len(string) + 2) + '|')
        print('+' + '-' * (len(string) + 2) + '+')
    else:
        print('+' + '-' * (width + 2) + '+')
        print('|' + ' ' * (width + 2) + '|')
        print('|' + ' ' + string[:width] + ' ' + '|')
        print('|' + ' ' * (width + 2) + '|')
        print('+' + '-' * (width + 2) + '+')

# Further exploration 2 (I think I didn't do it the first time):
# Previous code would only be able to handle 2 string lines, I think, so we gotta re-do

 




# 4

def stringy(num):
    if num % 2 == 0:
        return "10" * (num // 2)
    else:
        return "10" * (num // 2) + '1' # this is so insane

# Second pass:

def stringy(num):
    result = ''
    i = 0

    while i < num:
        if i % 2 != 0:
            result += '0'
        else:
            result += '1'
        i += 1
        
    return result

# 5

def triangle(num):
    for el in range(1, num + 1):
        print(' ' * (num - el) + '*' * el)
    
# Second pass:

