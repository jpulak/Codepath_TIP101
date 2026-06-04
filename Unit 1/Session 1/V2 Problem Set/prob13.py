#Problem 13: Calculate the Squares
'''Write a function squares() that takes a list of
 integers nums as a parameter and returns a new list 
 containing the square of each number in the original list.

def squares(nums):
    pass
Example Input: [1,2,3,4]
Example Output: [1,4,9,16]'''

def squares(nums):
    new=[]
    for i in nums:
        new.append(i**2)
    return new

print(squares([1,2,3,4]))