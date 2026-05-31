#Problem 5: Merge Sort I
'''Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

Given the pseudo-code and helper function merge() below, implement the merge_sort() function.

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
	result = [] # List to store the merged result
	i = j = 0 # Pointers to iterate over left and right input arrays
	
	# Compare elements from left and right halves of the list and add them to the
	# result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1
  
  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1
  
  return result

def merge_sort(lst):
	pass
Example Usage:

# Example Input: [5,3,4,2,1]
Example Output:

# Expected Output: [1,2,3,4,5]'''