#Problem 2: Delete Minimum
'''Write a function delete_minimum_elements(nums)
 that takes in a list of integers nums as a parameter
   and continuously removes the minimum element until 
   the list is empty. The function returns a new list of 
   all the elements in nums in the order in which they 
   were removed.

def delete_minimum_elements(nums):
    pass
Example Usage:

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)
Example Output: [1,2,3,3,5,8]'''

'''
takes in a list of integers
and then remove the minimum element
until list is mepty
the fucnitonr eturn new list
int he ordre it iwas removed

so basically sort the list, but it has to be
removing in ordre of the least
'''

def delete_minimum_elements(nums):
    new=[]
    while nums:
        min_val = min(nums)
        nums.remove(min_val)
        new.append(min_val)
    return new




nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)