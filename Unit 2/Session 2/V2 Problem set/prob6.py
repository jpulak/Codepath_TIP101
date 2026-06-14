#Problem 6: How Many Smaller
'''Write a function smaller_numbers_than_current() that takes in a list of 
numbers nums as a parameter. For each nums[i], the function should find out 
how many numbers in the list are smaller than it. (For each nums[i], count the
 number of valid j's such that j!=i and nums[j] < nums[i])

Return the answers in a list.

def smaller_numbers_than_current(nums):
    pass
Example Input:

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
Example Output: [4,0,1,1,3]

Explanation:

nums[0] == 6
There exists four smaller numbers than it (1, 2, 2 and 3) --> ans[0]=4

nums[1] == 1 
There does not exist any smaller number than it --> ans[1]=0

nums[2] == 2 
There exists one smaller number than it (1) --> ans[2]=1

nums[3] == 2 
There exists one smaller number than it (1) --> ans[3]=1

nums[4] == 3 
There exists three smaller numbers than it (1, 2 and 2) --> ans[4]=3
'''
'''
understand
function taking in a list of integers
for each integer, figure out how many numbers within the list is smaller than the integer
output the number into a list

plan
define function with parameter(list of integer)
define new list
define new var to keep track??
iterate through the list
current = i
    for i in range
    if i < i:
        var +=1
nested list?

implement

def smaller_numbers_than_current(nums):
    all=[]
    for num in nums:
        new = num
        track =0
        for j in nums:
            if new > j:
                track +=1
        all.append(track)
    return all
'''

def smaller_numbersT_than_current(nums):
    # Sort the nums list
    sorted_nums = sorted(nums)
    
    # Dictionary to store the smallest index at which each number appears
    smaller_count_map = {}
    for i in range(len(sorted_nums)):
        num = sorted_nums[i]
        # Only set the index for the first occurrence of each number
        if num not in smaller_count_map:
            smaller_count_map[num] = i
    
    # Manually generate the result based on the original list values
    result = []
    for num in nums:
        result.append(smaller_count_map[num])
    
    return result

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))