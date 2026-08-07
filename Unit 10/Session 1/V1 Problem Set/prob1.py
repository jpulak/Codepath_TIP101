#Problem 1: Valid Parentheses
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
def is_valid(s):
	pass

Example Usage:

Example #1:
Input: s = "()"
Expected Output: True

Example #2:
s = "()[]{}"
Expected Output: True

Example #3: 
s = "(())"
Expected Output: True

Example #4:
s = "(]"
Expected Output: False

Example #5:
s = "([)]"
Expected Output: False
'''

def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

s = "([)]"
print(is_valid(s))