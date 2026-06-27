#Problem 1: Prime Number
'''Write a function is_prime() that takes in a
 positive integer n and returns True if it is a prime 
 number and False otherwise. A prime number is a number 
 greater than 1 that has no positive divisors other than
   1 and itself.

def is_prime(n):
    pass
Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
Example Output:

True
False
False'''

'''
understand is the integer is given if it is prime, return true 
if not return false

plan to figure out if it is a prime number

'''
def is_prime(n):
    if n < 1:
        return False
    i = 2
    while i*i <=n:
        if n %i ==0:
            return False
        i +=1
    return True


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))