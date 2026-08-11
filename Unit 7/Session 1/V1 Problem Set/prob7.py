#Problem 7: Find Floor
'''Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

Evaluate the time and space complexity of your function.
z
def find_floor(lst, x):
	pass
Example Usage:

# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5
Example Output:
sfd
# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.'''

def find_floor(lst, x):
	low = 0
	high = len(lst) -1
	floor = None
	while low <= high:
		mid = (low+high) //2
		if lst[mid] <=x:
			floor = lst[mid]
			low =mid+1
		else:
			high = mid-1
	return floor

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))
# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.
