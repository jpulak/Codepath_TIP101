#Problem 9: Create Number
'''Write a function list_to_number() that takes 
in a list digits where each item is a digit between
 0-9. The function returns the number they represent
   when combined.

def list_to_number(digits):
    pass
Example Usage:

digits = [1,0,3]
number = list_to_number(digits)
print(number)
Example Output: 103'''

def list_to_number(digits):
    return("".join(map(str,digits)))

    # int("".join([str(i) for i in digits]))

# def list_to_number(digits):
#     number = 0
#     for digit in digits:
#         number = number * 10 + digit
#     return number

digits = [1,0,3]
number = list_to_number(digits)
print(number)