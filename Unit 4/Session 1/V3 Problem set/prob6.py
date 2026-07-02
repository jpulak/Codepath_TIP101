#Problem 6: Squash Spaces
'''The two-pointer approach can also be used with two 
pointers that iterate forward through a list or string at
 different rates. Use two pointers to solve the following problem:

Write a function squash_spaces() that takes in a string s as 
a parameter and returns a new string with each substring with 
consecutive spaces reduced to a single space. Assume s can
 contain leading or trailing spaces, but in the result should be trimmed.
Do not use any of the built-in trim methods.

def squash_spaces(s):
    pass
Example Usage:

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))
Example Output:

hello world
what about this ?
this is my sentence
'''

def squash_spaces(s):
    # Initialize pointers and the output list
    ptr = 0
    output = []

    # Skip initial spaces
    while ptr < len(s) and s[ptr] == ' ':
        ptr += 1

    while ptr < len(s):
        if s[ptr] != ' ':
            # Add non-space characters directly to output
            output.append(s[ptr])
        else:
            # Add a space only if the last added character is not a space
            # and there are more characters after the current one
            if len(output) > 0 and output[-1] != ' ' and ptr + 1 < len(s) and s[ptr + 1] != ' ':
                output.append(s[ptr])

        ptr += 1

    # Join list into a final string
    return ''.join(output)

# def squash_spaces(s):
#     return " ".join(s.split())


print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))