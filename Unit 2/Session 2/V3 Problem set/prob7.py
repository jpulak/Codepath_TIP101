#Problem 7: Target Sum
'''Write a function two_sum() that takes in a list of 
integers nums and an integer target as parameters.
 The function should return the indices of the two numbers 
 that add up to target. You may assume that each input would
   have exactly one solution and you may not use the same element
     twice. The function can return the indices in any order.

def two_sum(nums, target):
    pass
Example Input:

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)
Example Output:

[0,1]
[1,2]
[0,1]'''

def two_sum(nums, target):
    prev_map = {}  # Value to index mapping
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i


nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)