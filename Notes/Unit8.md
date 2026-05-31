# Unit 8 Cheatsheet

Here’s a quick reference sheet for Unit 8. While not an exhaustive list, it highlights the key syntax and concepts you’ll use in this unit, plus a few optional ideas that may help with problem-solving. You’re still expected to know required material from earlier units.

**Sections are labeled for clarity:**

- ✅ In-Scope: May appear on the assessment
- 💡 Not In-Scope: Useful, but not required

---

# 🎯 Unit Goals

- Define key terms related to binary trees
- Perform a preorder, postorder, and inorder traversal of a tree
- Solve problems that require traversing and manipulating nodes in a tree
- Differentiate between a general binary tree and a binary search tree
- Perform key operations such as insertion, deletion, and searching for a node in a binary tree

---

# General Concepts ✅ In-Scope

# Binary Trees

Binary trees are a **non-linear data structure**. Similar to a linked list, trees are made up of nodes that store a piece of data as well as references to other nodes.

---

## Binary Tree Structure

Each node in a binary tree can point to **up to two other nodes** in the tree.

Each of these pointers is known as a **child** of the original **parent** node.

The two children are referred to as:

- Left child
- Right child

### TreeNode Class

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right
```

### Example Usage

```python
# Creates the following tree:
#   1
#  / \
# 2   3

node_one = TreeNode(1)
node_two = TreeNode(2)
node_three = TreeNode(3)

node_one.left = node_two
node_one.right = node_three
```

- `node_two` is the left child of `node_one`
- `node_three` is the right child of `node_one`

---

# Tree Terminology

Understanding tree vocabulary is important.

## Root

The **top-most node** in a tree.

---

## Leaf

A node with **no children**.

---

## Edge

The reference or pointer connecting a parent node to a child node.

---

## Height

The maximum number of edges required to travel from a leaf node to the root node.

---

## Level

All nodes at the same height in the tree.

---

## Subtree

The tree formed by any node and all of its descendants.

---

## Ancestor

A node closer to the root on the path from the current node to the root.

---

## Descendant

Any node contained within the current node's subtree.

---

## Siblings

Two nodes that share the same parent.

---

# Balanced Trees

A tree is **balanced** if:

1. The height difference between the left and right subtree is at most 1.
2. Both subtrees are themselves balanced.

### Balanced Tree

Nodes are distributed fairly evenly.

Benefits:

- Faster searching
- Faster insertion
- Faster traversal

### Unbalanced Tree

Nodes become concentrated on one side.

Consequences:

- Slower searching
- Slower traversal
- Performance can approach linked-list behavior

Whether a tree is balanced significantly affects algorithm efficiency.

---

# Tree Traversal

Tree traversals usually begin at the **root node**.

Because trees are non-linear structures, there are multiple valid ways to visit every node.

The most common traversals are **Depth First Search (DFS)** traversals.

DFS fully explores one subtree before moving to another.

There are three standard DFS traversals:

1. Preorder
2. Inorder
3. Postorder

---

# Preorder Traversal

## Order

```text
Current → Left → Right
```

### Steps

1. Visit the current node
2. Traverse the left subtree
3. Traverse the right subtree

### Why Use Preorder?

Preorder visits nodes in the order they were added.

Common uses:

- Saving tree structure
- Serializing trees
- Copying trees

### Example

Given:

```text
      7
    /   \
   4     9
  / \   / \
 2   5 8  10
/ \
1  3
```

Preorder result:

```text
7 4 2 1 3 5 9 8 10
```

### How It Works

Start at root:

```text
Visit 7
```

Go left:

```text
Visit 4
```

Go left:

```text
Visit 2
```

Go left:

```text
Visit 1
```

Node 1 has no children.

Return to 2.

Visit right child:

```text
Visit 3
```

Continue until all left and right subtrees have been explored.

---

# Inorder Traversal

## Order

```text
Left → Current → Right
```

### Steps

1. Traverse left subtree
2. Visit current node
3. Traverse right subtree

### Why Use Inorder?

For a **Binary Search Tree (BST)**, inorder traversal visits nodes from:

```text
Smallest → Largest
```

Useful for:

- Printing sorted data
- Retrieving ordered values

### Example

Using the same tree:

```text
      7
    /   \
   4     9
  / \   / \
 2   5 8  10
/ \
1  3
```

Inorder result:

```text
1 2 3 4 5 7 8 9 10
```

### How It Works

Start at root:

```text
Go left
```

Continue left until reaching node 1.

Visit:

```text
1
```

Return to parent:

```text
2
```

Visit:

```text
2
```

Move right:

```text
3
```

Continue until entire tree is traversed.

---

# Postorder Traversal

## Order

```text
Left → Right → Current
```

### Steps

1. Traverse left subtree
2. Traverse right subtree
3. Visit current node

### Why Use Postorder?

Postorder processes all descendants before their parent.

Useful for:

- Deleting trees
- Freeing memory
- Evaluating expression trees

### Example

Using the same tree:

```text
      7
    /   \
   4     9
  / \   / \
 2   5 8  10
/ \
1  3
```

Postorder result:

```text
1 3 2 5 4 8 10 9 7
```

### How It Works

Start at root:

```text
Go left
```

Continue left until node 1.

Node 1:

- No left child
- No right child

Visit:

```text
1
```

Return to node 2.

Visit node 3.

After both children are processed:

```text
Visit 2
```

Continue until root is visited last.

---

# Traversal Summary

| Traversal | Order | Common Use |
|------------|--------|------------|
| Preorder | Current → Left → Right | Save/copy tree |
| Inorder | Left → Current → Right | Sorted output in BST |
| Postorder | Left → Right → Current | Delete/free tree |

---

# Binary Search Trees (BST)

A **Binary Search Tree** is a special type of binary tree.

For every node:

```text
Left subtree values < Current node value
Right subtree values > Current node value
```

Example:

```text
      8
     / \
    3  10
   / \   \
  1   6   14
```

Valid BST because:

- Everything left of 8 is smaller than 8.
- Everything right of 8 is larger than 8.

---

# Searching in a BST

Because the tree is ordered:

### If target < current node

Move left.

### If target > current node

Move right.

### If target == current node

Found it.

### Example

Search for 6:

```text
8 → left
3 → right
6 → found
```

Efficient because large portions of the tree are skipped.

---

# Inserting into a BST

Steps:

1. Start at root.
2. Compare value.
3. Move left or right.
4. Continue until an empty position is found.
5. Insert new node.

Example:

Insert 5 into:

```text
    8
   /
  3
```

Process:

```text
5 < 8 → left
5 > 3 → right
insert
```

Result:

```text
    8
   /
  3
   \
    5
```

---

# Deleting from a BST

Three common cases:

### Case 1: Leaf Node

Simply remove it.

```text
  5
 /
2
```

Delete 2.

Result:

```text
5
```

---

### Case 2: One Child

Replace node with its child.

```text
  5
 /
2
 \
  3
```

Delete 2.

Result:

```text
  5
 /
3
```

---

### Case 3: Two Children

Replace node with:

- Inorder successor (smallest node in right subtree)

or

- Inorder predecessor (largest node in left subtree)

Then delete that replacement node.

---

# Complexity Overview

Assuming a balanced BST:

| Operation | Time Complexity |
|------------|----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

Worst-case unbalanced BST:

| Operation | Time Complexity |
|------------|----------------|
| Search | O(n) |
| Insert | O(n) |
| Delete | O(n) |

---

# 💡 Why Do We Traverse Left to Right?

Computer science originated primarily in cultures where reading occurs from left to right.

This influenced the convention used for tree traversal algorithms.

There is no technical reason we cannot traverse:

```text
Right → Left
```

instead.

Traversal direction is simply a convention.

---

# Bonus Concepts 💡 Not In-Scope

The following concepts are useful but are **not required** for the Unit 8 assessment.

## Binary Search Tree Balancing

Techniques used to keep trees balanced automatically.

Examples:

- AVL Trees
- Red-Black Trees

---

## Breadth First Search (BFS)

Visits nodes level-by-level instead of subtree-by-subtree.

Typically uses a queue.

---

## Heap Trees

Specialized binary trees used for:

- Priority queues
- Scheduling
- Efficient minimum/maximum retrieval

---

## Tree Rotations

Operations used to rebalance BSTs after insertion or deletion.

---

## Recursive Traversal Implementations

Common recursive traversal templates:

```python
def preorder(root):
    if not root:
        return

    print(root.value)
    preorder(root.left)
    preorder(root.right)
```

```python
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)
```

```python
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value)
```

These traversal implementations are useful to understand, but detailed recursion mechanics may extend beyond Unit 8 assessment expectations.