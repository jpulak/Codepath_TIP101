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

# NON TWO POINTER
# Time complexity: O(n)
# Space complexity: O(n)
def two_sum(nums, target):
    prev_map = {}  # O(n) space complexit
    
    for i in range(len(nums)): # O(n) time complexity
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
        
# TWO POINTER
# Time complexity: O(n)
# Space complexity: O(1)
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right: # O(n) time complexity
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right] 
        elif current_sum < target:
            left += 1  # Need a larger sum
        else:
            right -= 1  # Need a smaller sum  