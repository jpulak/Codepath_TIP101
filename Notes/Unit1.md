# Unit 1 Cheatsheet

A quick reference sheet for Unit 1. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Write, use, and modify variables, functions, and print statements
* Use conditional logic (`if` statements)
* Work with lists (accessing, iterating, etc.)

---

# General Concepts ✅ In-Scope

## Built-In Functions

### Print

```python
print(s)
```

Prints the message `s` to the console.

**Parameters**

* `s` — The message you would like to print

### Examples

```python
# Example 1: Printing a string
print("Welcome to TIP101!")
```

```python
# Example 2: Printing an integer
print(100)
```

```python
# Example 3: Printing variables
s = "Welcome to CodePath!"
num = 7

print(s)
print(num)
```

```python
# Example 4: Printing a list
lst = ["TIP101", "TIP102", "TIP103"]
print(lst)
```

```python
# Example 5: Printing an expression
x = 5
y = 3

print(x + y)
```

```python
# Example 6: Printing a function return value

def my_func():
    return 6

result = my_func()

print(result)
print(my_func())
```

---

## Length

```python
len(s)
```

Returns the length of a list or string.

### Parameters

* `s` — The list or string

### Examples

```python
# Example 1: Length of a list
lst = ['a', 'b', 'c']
print(len(lst))
```

**Output**

```text
3
```

```python
# Example 2: Length of a string
s = "abcd"
print(len(s))
```

**Output**

```text
4
```

---

## Range

```python
range(start, stop, step)
```

Returns a sequence of numbers.

### Parameters

| Parameter | Description                                       |
| --------- | ------------------------------------------------- |
| start     | First value in sequence (optional, defaults to 0) |
| stop      | Ending value (exclusive)                          |
| step      | Increment amount (optional, defaults to 1)        |

### Examples

```python
range(10)
```

Produces:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

```python
range(1, 11)
```

Produces:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

```python
range(0, 30, 5)
```

Produces:

```text
0, 5, 10, 15, 20, 25
```

---

# Conditionals

Python conditionals use:

```python
if
elif
else
```

The code block executes when the condition evaluates to `True`.

### Example 1: Simple If Statement

```python
x = 3

if x > 1:
    print("This line will execute!")

if x > 5:
    print("This line will not execute!")
```

**Output**

```text
This line will execute!
```

---

### Example 2: If-Elif

```python
x = 10
y = 20

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
```

**Output**

```text
y is greater than x
```

---

### Example 3: If-Elif-Else

```python
x = 20
y = 20

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
else:
    print("x and y are equal")
```

**Output**

```text
x and y are equal
```

---

# For Loops

```python
for item in sequence:
```

Allows you to iterate through a sequence such as a list, string, or range.

### Example 1: Iterating Through a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output**

```text
apple
banana
cherry
```

---

### Example 2: Using Range

```python
for i in range(5):
    print(i)
```

**Output**

```text
0
1
2
3
4
```

---

# List Methods & Syntax

## Append Method

```python
lst.append(item)
```

Adds an item to the end of a list.

### Parameters

* `item` — Item to add

### Example

```python
lst = [1, 2, 3, 4]

lst.append(5)

print(lst)
```

**Output**

```text
[1, 2, 3, 4, 5]
```

---

## Sort Method

```python
lst.sort()
```

Sorts a list in ascending order.

### Example 1: Integers

```python
lst = [4, 2, 1, 3]

lst.sort()

print(lst)
```

**Output**

```text
[1, 2, 3, 4]
```

---

### Example 2: Strings

```python
lst = ["b", "a", "d", "c"]

lst.sort()

print(lst)
```

**Output**

```text
['a', 'b', 'c', 'd']
```

---

# List Indexing

```python
lst[index]
```

Accesses an element at a specific position.

## Rules

* Indexing starts at `0`
* Positive indices count from the beginning
* Negative indices count from the end
* Invalid indices raise an `IndexError`

### Example 1: Positive Indexing

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[2])
```

**Output**

```text
apple
cherry
```

---

### Example 2: Negative Indexing

```python
print(fruits[-1])
print(fruits[-2])
```

**Output**

```text
cherry
banana
```

---

### Example 3: Index Error

```python
print(fruits[3])
```

**Output**

```text
IndexError: list index out of range
```

---

# List Slicing

```python
lst[start:end]
```

Returns a new list containing elements from `start` up to but **not including** `end`.

## Rules

* `start` is optional
* `end` is optional
* Negative indices count from the end
* Original list remains unchanged

### Example 1

```python
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])
```

**Output**

```text
[1, 2, 3]
```

---

### Example 2

```python
print(nums[:3])
```

**Output**

```text
[0, 1, 2]
```

---

### Example 3

```python
print(nums[3:])
```

**Output**

```text
[3, 4, 5]
```

---

### Example 4

```python
print(nums[-3:])
```

**Output**

```text
[3, 4, 5]
```

---

# Bonus Concepts 💡 Not In-Scope

The following concepts are useful but **not required** for the Unit 1 assessment.

| Function              | Description                               |
| --------------------- | ----------------------------------------- |
| `lst.insert(x, item)` | Inserts `item` at index `x`               |
| `lst.remove(item)`    | Removes first occurrence of `item`        |
| `lst.pop(x)`          | Removes and returns item at index `x`     |
| `lst.copy()`          | Creates a shallow copy of a list          |
| `abs(x)`              | Returns absolute value of `x`             |
| `enumerate()`         | Returns index-value pairs while iterating |

### Example: Enumerate

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output**

```text
0 apple
1 banana
2 cherry
```

---

# Quick Study Checklist

Before taking the Unit 1 Assessment, make sure you can:

* [ ] Use `print()`
* [ ] Use `len()`
* [ ] Use `range()`
* [ ] Write `if`, `elif`, and `else` statements
* [ ] Write `for` loops
* [ ] Access list elements using indexing
* [ ] Use list slicing
* [ ] Use `append()`
* [ ] Use `sort()`
* [ ] Trace code involving lists and loops
* [ ] Explain what a piece of code will output
