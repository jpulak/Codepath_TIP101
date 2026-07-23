#Problem 1: Build a Binary Tree I
'''Given the following TreeNode class, create the binary tree depicted in the image below.

Binary Tree Example
(image provided in course webstie)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right'''

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
         

def is_univalued_help(node, value):
    if not node:
        return True

    if node.val != value:
        return False
    
    return is_univalued_help(node.left, value) and is_univalued_help(node.right, value)

def if_univalued(root):
    if not root:
        return True

    return is_univalued_help(root,root.val)


root1 = TreeNode(1,
    TreeNode(1,
        TreeNode(1),
        TreeNode(1)
    ),
    TreeNode(1,
        None,
        TreeNode(1)
    )
)

print(if_univalued(root1))