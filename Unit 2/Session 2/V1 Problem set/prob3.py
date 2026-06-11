#Problem 3: Frequency Count
'''Write a function that takes in a list of integers 
nums and counts the number of occurrences of each integer.
 The function returns the result as a dictionary with integers
   as keys and their counts as values.

def count_occurrences(nums):
    pass
Example Input: nums = [1, 2, 2, 3, 3, 3, 4]
Example Output: {1: 1, 2: 2, 3: 3, 4: 1}'''

def count_occurrences(nums):
    dictt={}
    for i in nums:
        if i in dictt:
            dictt[i] += 1 #add on to current 
        else:
            dictt[i] = 1 #create new 
    return dictt


nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

# def count_occurrences(nums):
#     frequency_map = {}
#     for num in nums:
#         if num not in frequency_map:
#             frequency_map[num] = 0
#         frequency_map[num] += 1
#     return frequency_map