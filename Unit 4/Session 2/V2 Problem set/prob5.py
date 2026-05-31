#Problem 5: Averages of Subarray
'''The sliding window technique is an algorithmic technique often used to find a subarray or substring that meets certain criteria. It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. The pointers are then incremented to slide the window and examine a different subarray or substring.

Use the sliding window technique to solve the following problem:

Write a function find_averages_of_subarrays() that takes in a list of integers nums and an integer k as parameters. The function returns a list where each element in the average of each contiguous subarray of size k in nums where 1 ≤k ≤ len(nums)

def find_averages_of_subarrays(k, nums):
	pass
Example Usage:

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
Example Output:

[2.2, 2.8, 2.4, 3.6, 2.8]
# (1 + 3 + 2 + 6 - 1)/5 = 2.2
# (3 + 2 + 6 -1 + 4)/5 = 2.8
# ... and so forth
'''