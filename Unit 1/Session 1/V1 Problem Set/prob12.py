#Problem 12: Sum of 1 to 10
''' Write a function sum_ten() that returns the sum of 
numbers from 1 to 10.

def sum_ten():
    pass
Example Usage: output = sum_ten()
Example Result: output = 55'''

def sum_ten():
    total =0
    for i in range(1,11):
        total += i
    
    return total

output = sum_ten()
print(sum_ten())
    