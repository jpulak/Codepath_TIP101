#Problem 7: Good Pairs
'''Write a function num_identical_pairs() that takes in a list of integers nums and returns the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def num_identical_pairs(nums):
    pass
Example 1:

nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))

nums = [1,2,3]
print(num_identical_pairs(nums))

nums = [1,1,1,1]
print(num_identical_pairs(nums))
Example Output:

4
0
6
Example 1 Explanation:

nums[0] == 1
- nums[0] == nums[3]
- nums[0] == nums[4]
Good Pairs: (0,3) and (0,4) --> count = 2

nums[1] == 2
No identical pairs found

nums[2] == 3
- nums[2] == nums[5]
Good Pairs: (2,5) --> count = 3

nums[3] == 1
*will not check any any indices less than current index*
- nums[3] == nums[4]
Good Pairs: (3,4) --> count = 4

nums[4] == 1
*will not check any any indices less than current index*
No identical pairs found

nums[5] == 3
*will not check any any indices less than current index*
No identical pairs found
'''