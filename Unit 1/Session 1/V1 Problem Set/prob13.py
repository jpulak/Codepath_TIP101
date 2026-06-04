#Problem 13: Total Sum
''' Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).

def sum_positive_range(stop):
    pass
Example Usage: sum = sum_positive_range(6)
Example Result: sum = 21

'''

def sum_positive_range(stop):
    total=0
    for i in range(1,stop+1):
        total += i
    return total

n= int(input())
print(sum_positive_range(n))