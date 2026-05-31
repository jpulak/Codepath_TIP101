#Problem 3: Evaluate Two Sum
'''The two_sum() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:

def two_sum(nums, target):
    prev_map = {}  # Value to index mapping
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
Which has better time complexity?
Which has better space complexity?
'''