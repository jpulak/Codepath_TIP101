#Problem 6: Has Duplicates
'''Write a function has_duplicates() that takes in a list of integers nums and a positive number k as parameters. The function returns True if the list contains any duplicate elements within k (inclusive) indices of each other. In other words, return True if nums[i] has the same value as any of the k neighboring elements to its left or right. If k is greater than the list's length, the solution should check for duplicates in the complete list. The function should return False otherwise.

def has_duplicates(nums, k):
	pass
Example Usage:

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)
Example Output:

False
True
True'''