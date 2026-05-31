#Problem 2: Sharing Cookies
'''Imagine you're an awesome babysitter and want to give the kids you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the cookie size list s as parameters and maximizes the number of content children you are babysitting! The function returns

Example 1:

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

find_content_children(s, g) 
# Output: 2 
Example 2:

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

find_content_children(s, g) 
# Output: 2 '''