#Problem 1: Sum of Strings
'''Write a function sum_of_number_strings() that takes in a 
list of strings nums. Each string is a representations of
 integers. The function should return the sum of these strings
   as an integer.

def sum_of_number_strings(nums):
    pass
Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
Example Output: 60
'''

def sum_of_number_strings(nums):
    nums =[int(i) for i in nums]
    return (sum(nums))

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

# def sum_of_number_strings(nums):
#     total_sum = 0
#     for num_str in nums:
#         total_sum += int(num_str)
#     return total_sum