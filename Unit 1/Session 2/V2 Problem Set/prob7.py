#Problem 7: Get Odd Numbers
'''Write a function get_odds() that takes 
in a list of integers nums and returns a list of 
all odd numbers in nums.

def get_odds(nums):
    pass
Example Usage:

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)
Example Output:

[5, 1, 5]'''

def get_odds(nums):
    all=[]
    for i in nums:
        if i %2 !=0 :
            all.append(i)
    return all

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)