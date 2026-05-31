# Unit 9 Cheatsheet

Here’s a quick reference sheet for Unit 9. While not an exhaustive list, it highlights the key syntax and concepts you’ll use in this unit, plus a few optional ideas that may help with problem-solving. You’re still expected to know required material from earlier units.

## Sections

- ✅ In-Scope: May appear on the assessment
- 💡 Not In-Scope: Useful, but not required

---

# General Concepts ✅ In-Scope

## Python Syntax

### Absolute Value

`abs(x)` returns the absolute value of a given number.

The absolute value of a number is the distance of that number from 0.

#### Parameters

- `x`: the number you would like the absolute value of

#### Example Usage

```python
# Example #1: Absolute value of a number
abs(-10)  # Returns 10

# Example #2: Absolute value of an expression
abs(10 - 20)  # Returns 10
```

---

### Infinity

We can represent positive and negative infinity with the following syntax:

```python
positive_infinity = float('inf')

negative_infinity = float('-inf')
```

Infinity is often used as an initial value when finding some unknown value, especially a minimum or maximum value.

#### Example Usage

```python
lst = [5, 4, 3, 2, 1]

def get_min(lst):
    minimum = float('inf')

    for num in lst:
        if num < minimum:
            minimum = num

    return minimum
```

In the example above, infinity is used to find the minimum value in a list of numbers.

We assume the minimum is the largest number possible (infinity), then update our assumption as we iterate through the list and find values lower than infinity.

Infinity is also commonly used as a return value to handle edge cases.

#### Example Usage

```python
def safe_divide(a, b):
    if b == 0:
        if a > 0:
            return float('inf')
        else:
            return float('-inf')

    return a / b
```

In the example above, infinity is used to gracefully handle cases where a user tries to divide a number by zero.

Normally, dividing a number by zero would result in Python raising a `ZeroDivisionError`.

---

# Queues

Queues are a special type of list where elements are always added and removed in a certain order.

Queues follow the **First In, First Out (FIFO)** principle, which means that the first element added to the queue will be the first element to be removed.

The term **queue** comes from the British meaning of the word queue: a line of waiting people.

Queue data structures follow the same logic as queues of real people.

Imagine that each element in the queue is a person:

- New people add themselves to the end of the line.
- They must wait until all people ahead of them leave.
- The person who has been waiting the longest exits first.

Practically speaking:

- New elements are appended to the **end** of a queue.
- Elements are removed from the **beginning** of a queue.

---

## Creating a Queue with `deque`

In Python, we use the `deque` class to create a queue.

### Example Usage

```python
# 1. Import the deque module
from collections import deque

# 2. Initialize a new deque object
queue = deque()

# 3. Add a new element, 1, to the end (right side) of the queue
queue.append(1)

# 4. Remove an element from the beginning (left side) of the queue
removed_elt = queue.popleft()

print(removed_elt)  # Prints 1
```

### Breakdown

1. Import the `deque` class from the `collections` library.
2. Create a new queue.
3. Use `append()` to add elements to the end.
4. Use `popleft()` to remove elements from the beginning.

---

## Alternative Queue Operations

It is equally valid to:

- Add elements to the beginning.
- Remove elements from the end.

### Example Usage

```python
# Import the deque module
from collections import deque

# Initialize a new deque object
queue = deque()

# Add a new element, 1, to the left side of the queue
queue.appendleft(1)

# Remove an element from the right side of the queue
removed_elt = queue.pop()

print(removed_elt)  # Prints 1
```

### Important Rule

The important thing is that:

- Elements are added to one side.
- Elements are removed from the opposite side.

This preserves FIFO behavior.

---

## Why Use `deque` Instead of a List?

A queue can be implemented using a normal Python list.

However, `deque` is preferred because:

- Adding to the end is **O(1)**
- Removing from the beginning is **O(1)**

Under the hood, `deque` is implemented using a linked list, making these operations efficient.

---

# Breadth First Search (BFS)

Breadth First Search (BFS), also known as **Level Order Traversal**, is a method for visiting all nodes in a tree.

With BFS:

1. Visit the root.
2. Visit all children of the root.
3. Visit all grandchildren.
4. Continue level by level.

### Example Traversal Order

```text
Level 1: 19

Level 2: 7, 25

Level 3: 5, 22, 71

Level 4: 6, 30, 96
```

Traversal Order:

```text
[19, 7, 25, 5, 22, 71, 6, 30, 96]
```

---

## BFS Algorithm

BFS is typically implemented iteratively using a queue.

### Pseudocode

```text
If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue

    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue
```

---

## Recursive BFS

BFS can also be implemented recursively.

However, an iterative queue-based implementation is generally preferred because:

- BFS naturally follows FIFO ordering.
- Queues naturally provide FIFO ordering.

The queue directly models the order BFS visits nodes.

---

# How to Pick a Traversal Method

There are four standard traversal algorithms for binary trees:

### Depth First Search (DFS)

- Preorder
- Inorder
- Postorder

### Breadth First Search (BFS)

- Level Order Traversal

For many problems, any traversal method can work.

However, some traversals are better suited for specific tasks.

---

# Depth First Search

In general, DFS is preferred when:

- The solution is expected to be deeper in the tree.
- You want to explore a branch completely before moving elsewhere.

DFS follows one path as far as possible before backtracking.

A BFS solution may still work, but it may visit many unnecessary nodes first.

DFS traversals are commonly used for:

- Finding leaves
- Finding tree height
- Finding tree diameter

---

# Inorder Traversal

For a Binary Search Tree (BST):

```text
Left → Current → Right
```

Inorder traversal visits nodes in sorted ascending order.

### Common Uses

- Binary Search Tree operations
- Converting a BST into a sorted list
- Producing sorted output

---

# Preorder Traversal

For a binary tree:

```text
Current → Left → Right
```

Preorder processes the root before either subtree.

It also processes nodes in the order they were inserted.

### Common Uses

- Tree copying
- Expression tree evaluation
- Tree serialization
- Saving tree structure

---

# Postorder Traversal

For a binary tree:

```text
Left → Right → Current
```

Postorder processes children before the root.

### Common Uses

- Deleting a tree
- Expression tree evaluation
- Cleaning up subtrees before parents

---

# Breadth First Search (Level Order)

BFS processes nodes:

- Closest to the root first
- Level by level
- Left to right within each level

### Preferred When

- The solution is expected near the root.
- The problem requires level-by-level processing.

### Common Uses

- Level order traversal
- Shortest path in unweighted trees
- Tree level analysis

---

# Bonus Concepts 💡 Not In-Scope

The following concepts are useful and may improve your code readability or deepen your understanding, but they are **not required** for the Unit 9 assessment.

## Throwaway Variable

Used to intentionally ignore values.

Common uses:

- Ignoring one value from a function that returns multiple values.
- Ignoring loop variables that are not needed.

Example:

```python
x, _ = (10, 20)

print(x)  # Prints 10
```

---

## Inner Functions

Specialized Python syntax often used to create helper functions.

Example:

```python
def outer():
    def helper():
        print("Helper function")

    helper()

outer()
```

Inner functions are commonly used to:

- Hide implementation details.
- Support recursion helper functions.
- Improve code organization.