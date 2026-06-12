#Problem 7: Make Pairs
'''Write a function divide_list() that takes in an integer list nums 
consisting of 2*n integers as parameters. The function divides nums into
 n pairs such that:

Each element belongs to exactly one pair
The elements present in a pair are equal
Return True if nums can be divided into n pairs, otherwise return False.

def divide_list(nums):
    pass
Example Input:

nums = [3,2,3,2,2,2]
print(divide_list(nums))
Example Output: True
Explanation: There are 6 elements in nums, so they should be divided 
into 6 / 2 = 3 pairs. If nums is divided into the pairs (2, 2), (3, 3),
 and (2, 2), it will satisfy all the conditions.

Example Input:

nums = [1,2,3,4]
print(divide_list(nums))
Example Output: False
Explanation: There is no way to divide nums into 4 / 2 = 2 pairs such 
that the pairs satisfy every condition.

'''

def divide_list(nums):
    freq ={}
    for i in nums:
        #freq[i] = freq.get(i, 0) + 1
        if i not in freq:
            freq[i] = 0
        freq[i]+=1

    for val in freq.values():
        if val %2!=0:
            return False
    return True

nums = [3,2,3,2,2,2]
print(divide_list(nums))
nums = [1,2,3,4]
print(divide_list(nums))

# def divide_list(nums):
#     # Frequency map to count occurrences of each number
#     frequency_map = {}
#     for num in nums:
#         frequency_map[num] = frequency_map.get(num, 0) + 1
    
#     # Check if all counts are even
#     for count in frequency_map.values():
#         if count % 2 != 0:
#             return False  # An odd count found, can't divide into pairs
    
#     return True  # All counts are even, can divide into pairs