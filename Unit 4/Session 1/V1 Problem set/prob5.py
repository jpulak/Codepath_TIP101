#Problem 5: Palindrome
'''Write a function first_palindrome() that takes in a 
list of strings words as a parameter and returns the first 
palindromic string in the list. A string is palindromic if
 it reads the same forward and backward. If there is no 
 such string, return an empty string ""

def first_palindrome(words):
    pass
Example Usage:

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
Example Output:

ada
racecar
'''
'''
iterate through the list
do the palindrome algorithm, two pointer


'''

def palindrome(element):
    left = 0
    right = len(element) -1

    while left < right:
        if element[left] == element[right]:
            left +=1
            right -=1
        else:
            return False
    return True

def first_palindrome(words):
    for i in words:
        if palindrome(i):
            return i
    return " "
            
# def is_palindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# def first_palindrome(words):
#     for word in words:
#         if is_palindrome(word):
#             return word
#     return ""
                    

# test = 'racecar'
# print(first_palindrome(test))

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)