#Problem 3: Backspace Compare
'''Write a function backspace_compare() that takes in two strings s and t as parameters that both might have the backspace character #. The backspace character removes the character in front of it. The function returns True if they are equal when both are typed into empty text editors and False otherwise. Note that after backspacing an empty text, the text will continue empty.

def backspace_compare(s, t):
    pass
Example Usage:

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))
Example Output:

True
True
False
'''