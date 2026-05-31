# Unit 10 Cheatsheet

Here’s a quick reference sheet for Unit 10. While not an exhaustive list, it highlights the key syntax and concepts you’ll use in this unit, plus a few optional ideas that may help with problem-solving. You’re still expected to know required material from earlier units.

## Sections

- ✅ In-Scope: May appear on the assessment
- 💡 Not In-Scope: Useful, but not required

---

# General Concepts ✅ In-Scope

## Python Syntax

### Inner/Nested Functions

An **Inner Function**, also called a **nested function**, is a function defined inside another function.

### Example Usage

```python
# Outer function
def print_sum(x, y):

    # Inner function
    def get_sum():
        return x + y

    total = get_sum()
    print(f"{x} + {y} is {total}")

print_sum(1, 2)  # Prints: 1 + 2 is 3
```

The inner function has access to any variables and parameters defined by the outer function.

In the example above, the inner function `get_sum()` has access to `print_sum()`'s parameters even though they are not passed into `get_sum()`.

### Key Characteristics

- Inner functions can access variables from the outer function.
- Inner functions only exist within the scope of the outer function.
- They are commonly used as helper functions.
- They help keep code organized and modular.

### Example Usage

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):

    def inorder(node, result):
        if node:
            inorder(node.left, result)   # Traverse left subtree
            result.append(node.val)      # Visit root
            inorder(node.right, result)  # Traverse right subtree

    result = []
    inorder(root, result)
    return result
```

The function `inorder_traversal()` returns the inorder traversal of a tree as a list.

The helper function `inorder()` is specific to this task and is unlikely to be reused elsewhere, making it a good candidate for an inner function.

---

## Ternary Operators

A **ternary operator** is shorthand syntax that allows us to write a simple if-else statement on a single line.

### General Syntax

```python
value_if_true if condition else value_if_false
```

### Example Usage

```python
a = 10
b = 20

# Ternary operator
max_value = a if a > b else b
```

Equivalent normal conditional:

```python
if a > b:
    max_value = a
else:
    max_value = b
```

### Benefits

- More concise than a full if-else block.
- Useful for simple conditional assignments.
- Improves readability when used appropriately.

---

## List Comprehensions

A **List Comprehension** is shorthand syntax for creating a new list from an existing iterable.

### General Syntax

```python
[new_list_value for item in existing_list]
```

### Example Usage

```python
numbers = [1, 2, 3, 4, 5]

# List comprehension
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)
# Prints: [1, 4, 9, 16, 25]
```

Equivalent for-loop:

```python
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)
# Prints: [1, 4, 9, 16, 25]
```

---

### List Comprehensions with Conditions

The syntax can be expanded to filter elements.

### General Syntax

```python
[new_list_value for item in existing_list if condition]
```

### Example Usage

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only square numbers less than 5
squared_numbers = [num ** 2 for num in numbers if num < 5]

print(squared_numbers)
# Prints: [1, 4, 9, 16]
```

Equivalent for-loop:

```python
squared_numbers = []

for num in numbers:
    if num < 5:
        squared_numbers.append(num ** 2)

print(squared_numbers)
# Prints: [1, 4, 9, 16]
```

---

## Dictionary Comprehensions

Dictionary comprehensions apply the same idea to dictionaries.

### General Syntax

```python
{
    key_expression: value_expression
    for item in iterable
    if condition
}
```

### Example Usage

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Dictionary comprehension
squared_dict = {
    num: num ** 2
    for num in numbers
    if num < 5
}

print(squared_dict)
# Prints: {1: 1, 2: 4, 3: 9, 4: 16}
```

Equivalent for-loop:

```python
squared_dict = {}

for num in numbers:
    if num < 5:
        squared_dict[num] = num ** 2

print(squared_dict)
# Prints: {1: 1, 2: 4, 3: 9, 4: 16}
```

### Purpose

Dictionary comprehensions are useful for:

- Creating dictionaries quickly.
- Transforming existing data.
- Filtering values while constructing dictionaries.

---

# Bonus Concepts 💡 Not In-Scope

The following topics are useful and may deepen your understanding, but they are **not required** for the Unit 10 assessment.

---

# Stacks

A **Stack** is a special type of list that follows the **Last In, First Out (LIFO)** principle.

This means:

- The last element added is the first element removed.

Think of a stack like a stack of plates:

- New plates are placed on top.
- Plates are removed from the top.

### Stack Terminology

| Operation | Description |
|------------|------------|
| Push | Add an element to the top of the stack |
| Pop | Remove an element from the top of the stack |

---

## Stack Implementation

Stacks can be easily implemented using Python lists.

### Example Usage

```python
stack = []

# Push items
stack.append(1)
stack.append(2)

# Pop item
popped_item = stack.pop()

print(popped_item)  # Prints: 2
print(stack)        # Prints: [1]
```

### Time Complexity

| Operation | Complexity |
|------------|------------|
| append() | O(1) |
| pop() | O(1) |

Because both operations are O(1), Python lists already provide an efficient stack implementation.

Unlike queues, no additional library is necessary.

---

# Stacks vs Queues

Both stacks and queues maintain a specific insertion/removal order.

## Stack (LIFO)

```text
Last In → First Out
```

Example:

```text
Push: 1, 2, 3

Pop Order:
3
2
1
```

---

## Queue (FIFO)

```text
First In → First Out
```

Example:

```text
Enqueue: 1, 2, 3

Dequeue Order:
1
2
3
```

---

## Stacks and Recursion

Many recursive solutions naturally use a stack.

Computers internally use a stack called the **Call Stack**.

Every recursive call:

1. Gets pushed onto the call stack.
2. Waits until deeper calls finish.
3. Gets popped off the stack.

---

## Example: Reverse a String Using a Stack (Iterative)

```python
def reverse_string_iterative(s):
    stack = []

    # Push characters onto stack
    for char in s:
        stack.append(char)

    reversed_string = ""

    # Pop characters off stack
    while stack:
        reversed_string += stack.pop()

    return reversed_string
```

---

## Example: Reverse a String Recursively

```python
def reverse_string_recursive(s):

    # Base case
    if len(s) <= 1:
        return s

    # Recursive case
    return reverse_string_recursive(s[1:]) + s[0]
```

The recursive solution uses the call stack to reverse the string.

---

# Sets

A **Set** is a built-in Python data structure representing an unordered collection of unique elements.

Sets are commonly used for:

- Tracking seen values
- Eliminating duplicates
- Finding overlap between collections

---

## Set Characteristics

### Unordered

Sets do not maintain element order.

```python
my_set = {1, 2, 3}
```

You cannot access elements using indices.

---

### Unique Elements

Duplicate values are automatically removed.

```python
my_set = {1, 1, 2, 2, 3}

print(my_set)
# {1, 2, 3}
```

---

### Mutable

Elements can be added or removed.

---

### Iterable

Sets can be traversed using loops.

```python
for item in my_set:
    print(item)
```

---

## Creating Sets

### Using Curly Braces

```python
my_set = {1, 2, 3, 4}
```

### Using `set()`

```python
another_set = set([1, 2, 3, 4])
```

### Creating an Empty Set

```python
empty_set = set()
```

⚠️ Important:

```python
{}
```

creates an empty dictionary, **not** an empty set.

---

## Common Set Methods

### add()

Adds an element.

```python
my_set.add(4)
```

---

### remove()

Removes an element.

Raises `KeyError` if not found.

```python
my_set.remove(2)
```

---

### discard()

Removes an element if it exists.

Does not raise an error.

```python
my_set.discard(5)
```

---

### clear()

Removes all elements.

```python
my_set.clear()
```

---

### Example Usage

```python
my_set = {1, 2, 3}

my_set.add(4)        # {1, 2, 3, 4}
my_set.remove(2)     # {1, 3, 4}

# Raises KeyError
my_set.remove(5)

# No error
my_set.discard(5)

my_set.clear()       # {}
```

---

# Set Operations

Sets support mathematical operations.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
```

---

## Union

Elements in either set.

```python
union_set = set1 | set2
```

Result:

```python
{1, 2, 3, 4, 5}
```

---

## Intersection

Elements in both sets.

```python
intersection_set = set1 & set2
```

Result:

```python
{3}
```

---

## Difference

Elements in the first set but not the second.

```python
difference_set = set1 - set2
```

Result:

```python
{1, 2}
```

---

## Symmetric Difference

Elements in either set but not both.

```python
symmetric_difference_set = set1 ^ set2
```

Result:

```python
{1, 2, 4, 5}
```

---

## Summary of Set Operations

| Operation | Symbol | Description |
|------------|---------|-------------|
| Union | `a \| b` | Elements in either set |
| Intersection | `a & b` | Elements in both sets |
| Difference | `a - b` | Elements in first set only |
| Symmetric Difference | `a ^ b` | Elements in one set but not both |
