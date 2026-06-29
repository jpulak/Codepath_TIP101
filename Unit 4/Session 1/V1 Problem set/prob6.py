#Problem 6: Remove Duplicates with O(1)

'''Write a function remove_duplicates() that takes
 in a sorted list of integers nums as a parameter 
 and removes the duplicates in-place such that each
   element appears only once. Do not allocate extra
     space for another array; you must do this by 
     modifying the input list with O(1) extra memory.
       The function returns the new length of the list.

def remove_duplicates(nums):
    pass
Example Usage:

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
Example Output:

[1,1,2,3,4,4,4,5]
5
[1,2,3,4,5]
'''

def remove_duplicates(nums):

    if not nums:
        return 0
    # Pointer slow for the position of the next unique element
    slow = 1
    # Iterate through the array with fast
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow-1]:
            nums[slow] = nums[fast]
            slow +=1
            
    nums[:] = nums[:j]
    del nums[slow:]
    return slow


    

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
