#Problem 6: Backwards Binary Search
'''Generally binary search returns the index of the first occurrence of the target in the list. Write an updated version of binary search find_last() that, given a list that may contain duplicates, returns the index of the last occurrence of target.

Evaluate the time and space complexity of your function.
z
def find_last(lst, target):
	passaqa
Example Usage:
e
# Example Input: lst = [1, 3, 5, 7, sa9, 11, 11, 13, 15], target = 11
Example Output:
sfds2
# Expected Output: 6
# Explanation: The second (lasdt) occurrence of 11 has index 6 in the list'''

def find_last(lst, target):
    left, right = 0, len(lst) - 1
    last_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            last_occurrence = mid
            left = mid + 1  # Continue searching in the right half
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_occurrence