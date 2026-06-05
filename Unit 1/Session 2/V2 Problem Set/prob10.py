#Problem 10: Move Zeroes
'''Write a function move_zeroes() that takes in an 
integer list nums and returns a new list with all the 0 
values moved to the end of the list. The relative non-zero 
elements in the original list should be maintained.

def move_zeroes(nums):
    pass
Example Usage:

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)
Example Output:

[1,2,3,4,0,0,0]'''

def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i] ==0:
            nums.append(nums.pop(i))
    return nums

# def move_zeroes(nums):
#     result = []
#     zero_count = 0
    
#     # Iterate through the list and append non-zero elements to result
#     for num in nums:
#         if num != 0:
#             result.append(num)
#         else:
#             zero_count += 1
    
#     # Append the zeroes to the end of the result list
#     for _ in range(zero_count):
#         result.append(0)
    
#     return result

nums = [1, 2, 3]
new_nums = move_zeroes(nums)
print(new_nums)