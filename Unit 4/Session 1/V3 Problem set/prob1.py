#Problem 1: Highest Exponent
'''Write a function find_highest_exponent() that takes in an 
integer base and an integer limit as parameters. The function 
returns the highest exponent for which a given base raised to 
that exponent is less than or equal to limit.

def find_highest_exponent(base, limit):
    pass
Example Usage:

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)
Example Output:

# 2^6 = 64 and 2^7 = 128
6
# 3^1 = 3 and 3^2 = 9
1'''

def find_highest_exponent(base, limit):
    expo = 0
    power =1 
    while power *base <= limit:
        power *= base
        expo +=1
    return expo
     

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)