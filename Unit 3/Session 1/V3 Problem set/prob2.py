#Problem 2: Rotate Left
'''Write a function rotate_left() that takes in a 
string s and an integer n as parameters. The function 
returns a new string with the first n characters moved
 to the end of the string where 1 <= n <= len(str).

def rotate_left(s, n):
    pass
Example Usage:

s = "rotation"
print(rotate_left(s, 2))
Example Output: tationro'''

'''
move 0-nth number into the end of the s string

pu the stringinto a list
move the first part of the list to the end n times
combine the list and return 
'''

def rotate_left(s, n):
    # all = ""
    # all += s[n:] + s[:n]
    return s[n:] + s[:n]


s = "rotation"
print(rotate_left(s, 2))