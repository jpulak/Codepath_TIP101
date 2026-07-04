#Problem 3: Valid Palindrome
'''Write a function valid_palindrome() that takes in a string s 
as a parameter and returns True if s can be a palindrome after
 deleting at most one character from it and False otherwise.

def valid_palindrome(s):
    pass
Example Usage:

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
Example Output:

True
True
False
'''

def valid_palindrome(s):
    left =0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            skipleft = s[:left] + s[left+1:]
            skipright = s[:right] + s[right +1:]
        
            if skipleft == skipleft[::-1] or skipright == skipright[::-1]:
                return "can work when removed"
            else:
                return False
    return True


print(valid_palindrome("aba"))   # True
print(valid_palindrome("abca"))  # True
print(valid_palindrome("abc"))   # False