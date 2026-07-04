#Problem 4: Positive Negative Pairs
'''Write a function find_largest_k() that takes in a list of 
integers nums that does not contain any zeroes as a parameter.
 The function finds the largest positive integer k such that -k
   also exists in the array and returns k. If there is no such integer, 
   return -1.

def find_largest_k(nums):
    pass
Example Usage:

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))
Example Output:

3
-1
'''
'''
have a pinter for finding the highest positiv einteger
and then scannign to find the negative equvalen tby subtracting == 0
'''

def find_largest_k(nums):
    nums.sort()
    left, right = 0,0
    largest =-1

    while left< right:
        sum = nums[left] + nums[right]

        if sum < 0: #neg nubmer is too small
            left +=1
        elif sum > 0: # positive number is too large
            right -=1
        else:
            largest = nums[right] #positive
            left +=1
            right -=1
    return largest


nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))