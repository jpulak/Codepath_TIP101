#Problem 2: Count Pairs
'''Write a function count_pairs() that takes in a
 0-indexed list of integers nums of length n and 
 an integer target as parameters. The function
   returns the number of index pairs (i, j) 
   where 0 <= i < j < n and nums[i] + nums[j] < target.

def count_pairs(nums, target):
	pass
Example Usage:

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))
Example Output:

# nums[0] + nums[1] = 0
# nums[0] + nums[2] = 1
# nums[0] + nums[4] = 0
3

# nums[0] + nums[1] = -4
# nums[0] + nums[3] = -8
# nums[0] + nums[4] = -13
# nums[0] + nums[5] = -7
# nums[0] + nums[6] = -3
# nums[1] + nums[4] = -5
# nums[3] + nums[4] = -9
# nums[3] + nums[5] = -3
# nums[4] + nums[5] = -8
# nums[4] + nums[6] = -4
10'''

def count_pairs(nums, target):
	nums.sort() #sort array using two pointer

	count = 0
	n = len(nums)

	for left in range(n):
		right = left +1
		while right < n and nums[left] + nums[right] < target:
			right +=1
		count += right -left -1 #add number of valid paris with nums[left]
	return count

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))