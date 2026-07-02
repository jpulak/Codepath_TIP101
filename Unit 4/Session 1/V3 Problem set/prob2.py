#Problem 2: Two-Pointer Target Sum
'''Write a function two_sum() that takes in a sorted list of integers
 nums and an integer target as parameters and returns the indices of
   the two numbers that add up to target. You may assume that each input
     would have exactly one solution, and you may not use the same element
       twice. You can return the indices in any order.

The function must use the two-pointer approach, which is a common technique 
in which we initialize two variables (also called a pointer in this context) 
to track different indices or places in a list or string, then moves the
 pointers to point at new indices based on certain conditions. In the most 
 common variation of the two-pointer approach, we initialize one variable 
 to point at the beginning of a list and a second variable/pointer to point
   at the end of list. We then shift the pointers to move inwards through 
   the list towards each other, until our problem is solved or the pointers
     reach the opposite ends of the list.

def two_sum(nums, target):
    pass
Example Usage:

nums = [2,7,11,15,17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)
Example Output

[0,1]
[1,2]

first pointer in the first
second pointer go throught ehwhole thing
fast and slwo poitner
fast sum with slow and compare to targer
if it is nto equal, move fast to the next pointer
if it is not after looping, increment slow
'''

def two_sum(nums, target):
    left = 0
    right = len(nums) -1

    while left< right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left +=1 #need bigger sum so get bigger number to ht eleft
        else:
            right -=1 #need smaller sum get smaller to the right

nums = [2,7,11,15,17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)