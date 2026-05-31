# Unit 7 Cheatsheet

A quick reference sheet for Unit 7. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

---

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Understand the difference between iterative and recursive problem-solving approaches
* Implement solutions using recursion
* Describe and apply divide-and-conquer algorithms
* Solve problems using binary search

---

# General Concepts ✅ In-Scope

# Python Syntax

## Floor Division

The `//` operator performs **floor division**.

It divides two numbers and rounds the result **down** to the nearest whole integer.

### Syntax

```python
x // y
```

### Example Usage

```python
print(5 // 2)
```

Output:

```text
2
```

Explanation:

```text
5 / 2 = 2.5
Floor division rounds down to 2
```

---

```python
print(10 // 2)
```

Output:

```text
5
```

Explanation:

```text
10 / 2 = 5
Already a whole number
```

---

# Recursion

Recursion is the process of a function calling itself.

### Example

```python
def recursive_crash():
    print("I will run forever")
    recursive_crash()
```

If called:

```python
recursive_crash()
```

Output:

```text
I will run forever
I will run forever
I will run forever
...
```

Eventually the program crashes because the recursion never stops.

---

# Iteration vs Recursion

Both iteration and recursion are methods of repeating work.

## Iteration

Uses loops.

Examples:

* `for`
* `while`

Works using a **bottom-up** approach.

Solve small steps repeatedly until the full problem is solved.

---

## Recursion

Uses function calls.

Works using a **top-down** approach.

Breaks a problem into smaller versions of itself until reaching a simple case.

---

## Example Comparison

### Iterative Solution

```python
def count_iterative(num):

    i = 1

    while i <= num:
        print(f"Count {i}!")
        i += 1
```

Input:

```python
count_iterative(5)
```

Output:

```text
Count 1!
Count 2!
Count 3!
Count 4!
Count 5!
```

---

### Recursive Solution

```python
def count_recursive(num):

    print(f"Count {num}!")

    if num == 1:
        return
    else:
        count_recursive(num - 1)
```

Input:

```python
count_recursive(5)
```

Output:

```text
Count 5!
Count 4!
Count 3!
Count 2!
Count 1!
```

---

# Building a Recursive Function

Every recursive function requires two components:

## 1. Base Case

The stopping condition.

Without a base case, recursion never ends.

---

## 2. Recursive Case

The function calls itself with a smaller or simpler problem.

---

## Example

```python
def count_recursive(num):

    print(f"Count {num}!")

    # Base Case
    if num == 1:
        return

    # Recursive Case
    else:
        count_recursive(num - 1)
```

---

# Multiple Base Cases

A recursive function can have more than one stopping condition.

### Example: Determine if a Number is Odd

```python
def is_odd(n):

    # Base Case 1
    if n == 0:
        return False

    # Base Case 2
    if n == 1:
        return True

    # Recursive Case
    return is_odd(n - 2)
```

### Example Usage

```python
print(is_odd(5))
print(is_odd(6))
```

Output:

```text
True
False
```

---

# Multiple Recursive Cases

A recursive function may also contain multiple recursive branches.

### Example: Count Even Numbers

```python
def count_evens(lst):

    # Base Case
    if not lst:
        return 0

    # Recursive Case 1
    if lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:])

    # Recursive Case 2
    else:
        return count_evens(lst[1:])
```

### Example Usage

```python
output = count_evens([1, 2, 3, 4])

print(output)
```

Output:

```text
2
```

---

# Recursive Returns as Accumulators

In iterative solutions we often use accumulator variables.

### Iterative Version

```python
def count_evens_iterative(lst):

    count = 0

    for num in lst:
        if num % 2 == 0:
            count += 1

    return count
```

---

### Recursive Version

```python
return 1 + count_evens(lst[1:])
```

The return value acts like the accumulator.

Each recursive call contributes part of the final answer.

---

# Recursive Driver and Helper Functions

Sometimes recursive functions need additional parameters.

A common solution is:

1. Driver Function
2. Helper Function

---

## Driver Function

The function users call.

```python
def partition_evens_odds(lst):
    return recurse_partition(lst, [], [])
```

---

## Helper Function

Contains the recursive logic.

```python
def recurse_partition(lst, evens, odds):

    if not lst:
        return evens, odds

    if lst[0] % 2 == 0:
        evens.append(lst[0])
    else:
        odds.append(lst[0])

    return recurse_partition(lst[1:], evens, odds)
```

---

## Example Usage

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens, odds = partition_evens_odds(lst)

print(evens)
print(odds)
```

Output:

```text
[2, 4, 6, 8]
[1, 3, 5, 7, 9]
```

---

# Why Use a Helper Function?

Without a helper function:

```python
partition_evens_odds(lst, [], [])
```

The user must manually provide empty lists.

This creates a poor user experience.

The helper function hides implementation details.

---

# Divide and Conquer Algorithms

Divide and Conquer solves problems by:

1. Dividing
2. Solving
3. Combining

---

## Step 1: Divide

Break the problem into smaller subproblems.

Goal:

```text
Large Problem
↓
Smaller Problems
↓
Smallest Problems
```

---

## Step 2: Conquer

Solve each smaller problem.

Often accomplished using recursion.

---

## Step 3: Combine

Merge subproblem solutions together.

Goal:

```text
Small Solutions
↓
Larger Solutions
↓
Final Answer
```

---

# Binary Search

Binary Search is a classic Divide-and-Conquer algorithm.

Used to find a target value in a **sorted list**.

---

## Time Complexity

```text
O(log n)
```

Very efficient because each step cuts the search space in half.

---

## Binary Search Process

### Step 1

Check the middle element.

---

### Step 2

If the middle element equals the target:

```python
return middle_index
```

---

### Step 3

If target is smaller:

Search left half.

---

### Step 4

If target is larger:

Search right half.

---

### Step 5

Continue until:

* Target found
* Search area empty

---

## Example

Find:

```text
5
```

In:

```text
[1,2,3,4,5,6,7,8,9]
```

Check middle:

```text
5
```

Target found immediately.

---

# Merge Sort

Another Divide-and-Conquer algorithm.

Used for sorting.

---

## Time Complexity

```text
O(n log n)
```

---

## Merge Sort Process

### Step 1: Divide

Split list repeatedly.

Example:

```text
[8,4,2,6]
```

↓

```text
[8,4] [2,6]
```

↓

```text
[8] [4] [2] [6]
```

---

### Step 2: Conquer

Lists of size 1 are already sorted.

---

### Step 3: Combine

Merge sorted lists together.

```text
[8] [4]
```

↓

```text
[4,8]
```

and

```text
[2] [6]
```

↓

```text
[2,6]
```

Then:

```text
[4,8] + [2,6]
```

↓

```text
[2,4,6,8]
```

---

# Bonus Concepts 💡 Not In-Scope

The following topics are useful but are not required for Unit 7 assessments.

## Inner Functions

Functions defined inside other functions.

Often used to create helper functions.

---

## List Comprehensions

Compact syntax for building lists.

Example:

```python
squares = [x * x for x in range(5)]
```

---

# The Call Stack

Whenever functions call other functions, Python uses a data structure called the **Call Stack**.

---

## Example

```python
def function_c():
    print("I'm Function C!")
    print("Function C is done executing!")

def function_b():
    print("I'm Function B!")
    function_c()
    print("Function B is done executing!")

def function_a():
    print("I'm Function A!")
    function_b()
    print("Function A is done executing!")

function_a()
```

Output:

```text
I'm Function A!
I'm Function B!
I'm Function C!
Function C is done executing!
Function B is done executing!
Function A is done executing!
```

---

## How the Call Stack Works

Think of function calls as books stacked on top of one another.

When a function is called:

```text
Push onto stack
```

When a function finishes:

```text
Pop off stack
```

The function on top executes first.

---

# Recursion and the Call Stack

Recursive functions repeatedly add new copies of themselves to the stack.

Example:

```python
sum_to_n(5)
```

Creates stack frames for:

```text
sum_to_n(5)
sum_to_n(4)
sum_to_n(3)
sum_to_n(2)
sum_to_n(1)
```

Then they return in reverse order.

---

# Recursion and Space Complexity

Every recursive call consumes memory.

### Example

```python
def sum_to_n(n):

    if n == 0:
        return 0

    return n + sum_to_n(n - 1)
```

For input:

```text
n
```

Approximately:

```text
n function calls
```

exist simultaneously.

---

## Space Complexity

```text
O(n)
```

because the call stack stores approximately `n` stack frames.

---

## Non-Recursive Functions

Most iterative solutions only require:

```text
O(1)
```

additional stack space.

---

# Quick Study Checklist

Before taking the Unit 7 Assessment, make sure you can:

* [ ] Explain floor division (`//`)
* [ ] Define recursion
* [ ] Explain recursion vs iteration
* [ ] Identify base cases
* [ ] Identify recursive cases
* [ ] Write recursive functions
* [ ] Use multiple base cases
* [ ] Use multiple recursive cases
* [ ] Explain recursive return values
* [ ] Create driver/helper recursive functions
* [ ] Explain divide-and-conquer
* [ ] Describe binary search
* [ ] Know why binary search is `O(log n)`
* [ ] Describe merge sort
* [ ] Know why merge sort is `O(n log n)`
* [ ] Explain the call stack
* [ ] Explain recursion's space complexity

---

# Key Takeaway

Unit 7 introduces recursion and divide-and-conquer algorithms.

The most important concepts are:

1. **Base Cases** → Stop recursion.
2. **Recursive Cases** → Break problems into smaller versions.
3. **Driver & Helper Functions** → Manage additional recursive parameters.
4. **Binary Search** → Efficient searching in sorted lists (`O(log n)`).
5. **Merge Sort** → Efficient sorting (`O(n log n)`).
6. **Call Stack** → Explains how recursive function calls are stored and executed.

Mastering these concepts provides the foundation for many advanced technical interview problems.
