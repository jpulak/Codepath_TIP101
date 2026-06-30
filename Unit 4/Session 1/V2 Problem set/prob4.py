#Problem 4: Make Palindromes
'''You are given a string s consisting of lowercase 
English letters, and are allowed to perform operations 
on it. In one operation, you can replace a character in 
s with another lowercase English letter.

Write a function make_palindrome() that takes in a string 
s and turns it into a palindrome with the minimum number
 of operations as possible. If there are multiple 
 palindromes that can be made using the minimum number of
   operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (
of the same length) if in the first position where a and b
differ, string a has a letter that appears earlier in the 
alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.

def make_palindrome(s):
    pass
Example 1:

s = "egcfe"
print(make_palindrome(s))
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller
Example 2:

s = "abcd"
print(make_palindrome(s))
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# a palindrome cannot be created in 1 operation
Example 3:

s = "seven"
print(make_palindrome(s))
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations
'''

def make_palindrome(s):
    left = 0
    right = len(s) -1
    s = [*s]
    while left < right:
        if s[left] != s[right]:
            if s[left]< s[right]:
                s[right] = s[left]
            else:
                s[left]= s[right]
        left +=1
        right -=1
    return "".join(s)

s = "egcfe"
print(make_palindrome(s))
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller

s = "abcd"
print(make_palindrome(s))
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# a palindrome cannot be created in 1 operation

s = "seven"
print(make_palindrome(s))
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations