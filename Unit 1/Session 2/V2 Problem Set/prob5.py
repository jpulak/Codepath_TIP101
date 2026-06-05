#Problem 5: Missing Number
'''Write a function find_missing() that takes in a list 
nums containing n unique numbers in the range [0,n]. 
The function returns the only number in the range that is 
missing from the list.

def find_missing(nums):
    pass
Example Usage:

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)
Example Output: 3'''

def find_missing(nums):
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    
    # nums.sort()
    # counter = 0
    # for num in nums:
    #     if num == counter:
    #         counter += 1 
    #     else:
    #         break # Do not need to keep looping
    # return counter
    
nums =[3,0,1]
missing_num = find_missing(nums)
print(missing_num)