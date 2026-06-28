#Problem 4: Move Even Integers
'''Write a function sort_list_by_parity() that takes
 in an integer list nums as a parameter and moves all 
 the even integers at the beginning of the list followed 
 by all the odd integers. The function returns any list 
 that satisfies this condition.

def sort_array_by_parity(nums):
    pass
Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
Example Output:

[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], 
# [2,4,1,3], and [4,2,1,3]
[0]
'''

'''
i need to two pointers to go theroughte hlist, 
one pointer is at the first of the list and the seocnd poitner
scans the list until it finda n even number
then it goes to the secon dpositon and then keep sscanning for the
next even number
'''

def sort_array_by_parity(nums):
    left = 0
    right= len(nums) -1

    while left < right:
        if nums[left]%2 ==0:
            left +=1
        elif nums[right]%2 != 0:
            right -=1
        else: # nums[left]%2 != 0 and nums[right] %2 ==0:
            nums[left], nums[right]= nums[right], nums[left]
            left +=1
            right -=1
    return nums



nums = [3,1,2,4]
print(sort_array_by_parity(nums))

# nums2 = [0]
# print(sort_array_by_parity(nums2))
