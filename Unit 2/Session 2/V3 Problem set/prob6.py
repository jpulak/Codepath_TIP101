#Problem 6: First Repeating Element
'''Write a function find_min_index_of_repeating() that 
takes in an integer list nums as a parameter and returns 
the minimum index of an element that has a duplicate value.
 The function should only do a single traversal of the list. 
 If there are no repeating elements, return None.

def find_min_index_of_repeating(nums):
    pass
Example Usage:

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))
Example Output:

1
None
3
'''

def find_min_index_of_repeating(nums):
    # Dictionary to store the first occurrence index of elements
    first_occurrence = {}
    min_index = None  # Initialize min_index to impossible value
    
    for i in range(len(nums)):
        if nums[i] not in first_occurrence:
            first_occurrence[nums[i]] = i
        elif min_index is None or first_occurrence[nums[i]] < min_index:
            min_index = first_occurrence[nums[i]]
            
    return min_index

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))

# def find_min_index_of_repeating(nums):
#     # Dictionary to store the first occurrence index of elements
#     first_occurrence = {}
#     min_index = None  # Initialize min_index to None
    
#     # Traverse the list from right to left to ensure the minimum index of the first repeating element is found
#     for i in range(len(nums)-1, -1, -1):
#         if nums[i] in first_occurrence:
#             # If the element is found in the dictionary, update min_index if necessary
#             min_index = i
#         else:
#             # Store the index of the first occurrence
#             first_occurrence[nums[i]] = i
    
#     return min_index