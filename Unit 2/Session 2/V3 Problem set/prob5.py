#Problem 5: No Duplicates Allowed
'''Write a function that takes in a list of integers nums 
as a parameter and removes all duplicates. The function should
 return a list containing the unique elements in the order of 
 their last occurrence in the original list.

def remove_duplicates_from_front(nums):
    pass
Example Input:

nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))
Example Output: [6,5,2,8,3]'''

def remove_duplicates_from_front(nums):
    unique_nums = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] not in unique_nums:
            unique_nums.insert(0, nums[i])
    return unique_nums


nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))

# def remove_duplicates_from_front(nums):
#     frequency_map = {}
#     for num in nums:
#         frequency_map[num] = True
#     last_occurrences = []
#     for num in nums[::-1]:  # Reverse iterate
#         if frequency_map[num]:
#             last_occurrences.append(num)
#             frequency_map[num] = False
#     return last_occurrences[::-1]  # Reverse again to original order