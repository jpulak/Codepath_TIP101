#Problem 3: Is Pangram
'''Write a function is_pangram() that takes in a
 string my_str as a parameter and returns True if 
 the string is a pangram and False if not. A 
 pangram is a sentence containing every letter 
 in the English alphabet.

def is_pangram(my_str):
    pass
Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
Example Output:

True
False'''

def is_pangram(my_str):
    alpha= 'abcdefghijklmnopqrstuvwxyz'
    my_str= my_str.lower()
    for char in alpha:
        if char not in my_str:
            return False
    return True

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))