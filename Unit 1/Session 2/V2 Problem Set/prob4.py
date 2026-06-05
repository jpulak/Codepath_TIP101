#Problem 4: Check for Number
'''Write a function check_num() that takes in a list of
 integers lst and an integer num as parameters and returns
   True if num is a value in lst and False otherwise.

def check_num(lst, num):
    pass
Example Usage:

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)
Example Output:

True
False'''

def check_num(lst, num):
    for i in lst:
        if i == num:
            return True
    return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)