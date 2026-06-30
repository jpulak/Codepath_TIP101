#Problem 3: Evaluate Palindrome
'''The is_palindrome() problem can also be solved
 without using the two-pointer technique
   (as you may have seen it in previous units)! 
   Evaluate the time and space complexity of your
     two-pointer solution.

Then, evaluate the time and space complexity of the
 following solution:

def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s
Which has better time complexity?
Which has better space complexity?
both have same space ocmplexity O(1)
two poitner has better time

'''

# NON TWO POINTER
# Time complexity: O(n)
# Space complexity: O(n)
def is_palindrome(s):
    reverse = s[::-1] # O(n) space and time: https://www.geeksforgeeks.org/python-reversing-list/
    return reverse == s
        
# TWO POINTER
# Time complexity: O(n)
# Space complexity: O(1)
def is_palindrome(s):
    left = 0
    right = len(s) - 1 # O(1) time/space(Getting length of list is an O(1) operation in python: https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/)
    while left < right: # O(n/2) --> O(n) time 
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True