#Problem 6: Merge Binary Trees
'''You are given two binary trees with roots root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

def merge_trees(self, root1, root2):
	pass
Example Usage:

Example Input Trees: 

          1                 2 
         / \               / \
        /   \             /   \
       3     2           1     3
      /                   \     \
     5                     4     7

Input: root1 = 1, root2 = 2
Expected Output: 3
Expected Output Tree

      3
     / \
    /   \
   4     5
  / \     \  
 5   4     7


'''