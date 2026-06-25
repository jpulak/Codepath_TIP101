#Problem 2: Missing Integer
'''Write a function find_missing_positive() that takes
 in a sorted list of integers nums that always starts at
   1, and returns the smallest missing positive integer.

def find_missing_positive(nums):
    pass
Example Usage:

nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))
Example Output:

4
6
'''
def find_missing_positive(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            return i + 1
    return i + 1
        
nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))