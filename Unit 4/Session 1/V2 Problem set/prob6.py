#Problem 6: Two-Pointer Remove Element
'''The two-pointer approach can also be used
 with two pointers that iterate forward through
   a list or string at different rates. Use two
    
      pointers to solve the following problem:
Write a function remove_element() that takes in a
 list nums and a value val as parameters and removes 
 all instances of that value in-place. The function 
 returns the new length of nums.

def remove_element(nums, val):
    pass
Example Usage:

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)
Example Output:

[5, 3, 1]
3
'''
#fast slow
def remove_element(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write +=1
    del nums[write:]#all the good numbers moved to the left and del rest
    return write

    
        
    

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)

