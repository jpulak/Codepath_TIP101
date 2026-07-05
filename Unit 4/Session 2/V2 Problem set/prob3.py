#Problem 3: Sort List by Parity
'''Write a function sort_array_by_parity() that takes in a
 list of integers nums where half of the integers are odd, 
 and the other half are even. The function sorts the list so
   that whenever nums[i] is odd, i is odd and whenever nums[i] is 
   even, i is even. The function returns the list in any order 
   that satisfies the condition.

def sort_array_by_parity(nums):
	pass
Example Usage:

nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
Example Output:

[4,5,2,7]
# [2,7,4,5], [2,7,4,5], [4,7,2,5] also works
[2,3]

'''

def sort_array_by_parity(nums):
	n = len(nums)
	evenPointer, oddPointer = 0, 1  # Starting indices for even and odd

	while evenPointer < n and oddPointer < n:
		# Find the next even number that is out of place
		while evenPointer < n and nums[evenPointer] % 2 == 0:
			evenPointer += 2
		# Find the next odd number that is out of place
		while oddPointer < n and nums[oddPointer] % 2 == 1:
			oddPointer += 2
		
		# If neither pointer has reached the end, swap their elements
		if evenPointer < n and oddPointer < n:
			nums[evenPointer],nums[oddPointer]=nums[oddPointer],nums[evenPointer]
	return nums

# def sort_array_by_parity(nums):
# 	check = 0
# 	new = 0
# 	while check < len(nums):
# 		if check%2 == 0:
# 			new = 0
# 			while new < len(nums):
# 				if nums[new] %2 ==0:
# 					nums[check],nums[new] = nums[new], nums[check]
# 				new +=1
# 		else:
# 			new = 0
# 			while new < len(nums):
# 				if nums[new] %2 !=0:
# 					nums[check],nums[new] = nums[new], nums[check]
# 				new +=1
# 		check +=1

# 	return nums
nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

