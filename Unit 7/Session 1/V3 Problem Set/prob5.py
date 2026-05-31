#Problem 5: Binary Search III
'''Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search that returns True if the given target is in the list and False otherwise. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the middle value is the target value, return True
		# If the middle value is smaller than the target value, search the right half of the list
		# If the middle value is greater than the target value, search the left half of the list
	
	# Return False if the target element has not been found

def binary_search(lst, target):
    pass
Example Usage:

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
Example Output:

# Expected Output: True'''