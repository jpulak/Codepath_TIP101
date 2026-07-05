#Problem 4: Merge to Palindrome
'''Write a function min_merge_operations() that takes in a list
 of non-negative integers nums and returns the minimum number
   of merge operations to make it a palindrome. A merge operation
     is adding two of the integers.

def min_merge_operations(nums):
	pass
Example Usage:

nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))
Example Output:

# merge 6 and 1 to get [7,3,7]
1
# nums2 already a palindrome
0
# need to merge all numbers to [13]
3
'''
def min_merge_operations(nums):
	left, right = 0, len(nums)-1
	counter = 0

	while left< right:
		#if equal, move towards center
		if nums[left] == nums[right]:
			left +=1
			right -=1
		#left ele is maller, merge to the next element
		elif nums[left] < nums[right]:
			nums[left +1] += nums[left] #merge
			left +=1
			counter +=1 #increament merge counter
		#right smaller, merge with prev element
		else:
			nums[right-1] += nums[right] #merge
			right -=1
			counter+=1
	return counter


nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))