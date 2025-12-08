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
# (previous code would only be able to handle 2 string lines, I think, so we gotta re-do.)



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
# Yeah, because you need an "i" iterator inside the loop, it's good to name your parameter something real like "height" for some clarity 
def triangle(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = i
        print((' ' * spaces) + ('*' * stars))

# 6

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
print(f"The {adjective} {noun} {verb} {adverb} over the lazy {noun}.")
print(f"The {noun} {adverb} {verb} up to Joe's {adjective} turtle.")

# Skipping second pass of 6

# 7 (I probably couldn't figure it out and retyped it)

def is_double_num(num):
    num_string = str(num)
    center = len(num_string) // 2
    left_number = num_string[:center]
    right_number = num_string[center:]
        
    return left_number == right_number
        
def twice(num):   
    if is_double_num(num):
        return num
    else:
        return num * 2

# Second pass: (still needed help but less so)

def twice(num):
    mid = len(str(num)) // 2
    mid_idx = int(mid) # these two lines are kind of funny
    
    if len(str(num)) % 2 != 0:
        return num * 2
    elif str(num)[:mid_idx] != str(num)[mid_idx:]:
        return num * 2
    else:
        return num
    
# 8

def get_grade(g1, g2, g3):
    score = (g1 + g2 + g3) / 3
    
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90: 
        return 'B'
    elif 70 <= score < 80: 
        return 'C'
    elif 60 <= score < 70: 
        return 'D'
    else:
        return 'F'
    
# Skipping second pass of 8

# 9

def clean_up(string):
    result = ''
    
    for char in string:
        if char.isalpha():
            result += char
        else:
            if len(result) == 0:
                result += ' '
            elif result[-1] != ' ':
                result += ' '
                
    return result


print(clean_up("---what's my +*& line?") == " what s my line ")

# Second pass (aside from doing ones like this in study sessions...)

...

# 10

def century(year):
    century_number = (year - 1) // 100 + 1
    last_two = century_number % 100
    
    if last_two in (11, 12, 13):
        suffix = 'th'
    else:
        last_digit = century_number % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
            
    return f"{century_number}{suffix}"

# Second pass:

