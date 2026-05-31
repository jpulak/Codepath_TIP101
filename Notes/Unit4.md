# Unit 4 Cheatsheet

A quick reference sheet for Unit 4. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

---

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Use the Two-Pointer approach to solve problems
* Understand opposite-direction pointers
* Understand same-direction pointers
* Apply the sliding window technique
* Use unpacking for cleaner code

---

# General Concepts ✅ In-Scope

# The Two-Pointer Approach

The **two-pointer approach** is a common algorithmic technique where two variables track different positions within a list or string.

Instead of repeatedly scanning the same data, pointers move through the structure based on conditions, often reducing runtime complexity from **O(n²)** to **O(n)**.

Common uses include:

* Reversing arrays or strings
* Finding pairs that meet a condition
* Merging sorted arrays
* Sliding window problems
* Palindrome checking

---

# Opposite Direction Pointers

One pointer starts at the beginning and another starts at the end.

The pointers move toward each other until they meet or cross.

## Visual Example

```text
[1, 2, 3, 4, 5, 6]
 ↑             ↑
left         right
```

After swapping:

```text
[6, 2, 3, 4, 5, 1]
    ↑       ↑
   left   right
```

Continue until:

```python
left >= right
```

---

## Template

```python
left = 0
right = len(nums) - 1

while left < right:
    # Process values

    left += 1
    right -= 1
```

---

## Example: Reverse a List

```python
nums = [1, 2, 3, 4, 5]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1

print(nums)
```

Output:

```python
[5, 4, 3, 2, 1]
```

---

## When Do We Stop?

Stop when:

### Odd Length

```python
left == right
```

Pointers meet in the middle.

---

### Even Length

```python
left > right
```

Pointers cross each other.

---

# Same Direction Pointers

Instead of moving toward each other, both pointers move forward.

This is commonly used when working with:

* Two sorted arrays
* Two strings
* Subsequence problems

---

## Example: Merge Two Sorted Lists

```python
nums1 = [1, 4, 6]
nums2 = [2, 3, 5]

p1 = 0
p2 = 0

merged = []
```

Compare:

```text
1 vs 2
```

Take the smaller value:

```python
merged = [1]
p1 = 1
```

Continue until both lists are exhausted.

---

## Template

```python
p1 = 0
p2 = 0

while p1 < len(nums1) and p2 < len(nums2):

    if nums1[p1] < nums2[p2]:
        p1 += 1
    else:
        p2 += 1
```

---

## Example

```python
nums1 = [1, 4, 6]
nums2 = [2, 3, 5]

p1 = 0
p2 = 0

merged = []

while p1 < len(nums1) and p2 < len(nums2):

    if nums1[p1] < nums2[p2]:
        merged.append(nums1[p1])
        p1 += 1
    else:
        merged.append(nums2[p2])
        p2 += 1

print(merged)
```

Output:

```python
[1, 2, 3, 4, 5]
```

---

# Sliding Window

The **sliding window** technique is an extension of the two-pointer approach.

Instead of examining every possible subarray repeatedly, we maintain a moving "window" over part of the list or string.

---

## Example Window Size = 3

```python
nums = [1, 2, 3, 4, 5]
```

Window 1:

```python
[1, 2, 3]
```

Window 2:

```python
[2, 3, 4]
```

Window 3:

```python
[3, 4, 5]
```

---

## Template

```python
for i in range(len(nums) - 2):

    window = nums[i:i+3]

    # Process window
```

---

## Example: Sum Each Window

```python
nums = [1, 2, 3, 4, 5]

for i in range(len(nums) - 2):

    window = nums[i:i+3]

    print(sum(window))
```

Output:

```text
6
9
12
```

---

## Why Use Sliding Window?

Without sliding window:

```python
O(n²)
```

With sliding window:

```python
O(n)
```

Useful for:

* Maximum subarray
* Longest substring
* Fixed-size windows
* Frequency problems

---

# Unpacking

Unpacking allows multiple variables to be assigned at once.

---

## Basic Example

```python
a, b = 1, 2

print(a)
print(b)
```

Output:

```text
1
2
```

---

## Swapping Variables

Without unpacking:

```python
temp = a
a = b
b = temp
```

With unpacking:

```python
a, b = b, a
```

Much cleaner.

---

# Swapping List Elements

```python
nums = [1, 2, 3, 4]

nums[0], nums[3] = nums[3], nums[0]

print(nums)
```

Output:

```python
[4, 2, 3, 1]
```

This is commonly used in opposite-direction pointer problems.

---

# Nested Unpacking

Unpacking also works on nested structures.

```python
inventory = [
    ["apples", 3],
    ["carrots", 5]
]
```

Unpack:

```python
[[item1, quantity1],
 [item2, quantity2]] = inventory
```

Result:

```python
item1 = "apples"
quantity1 = 3

item2 = "carrots"
quantity2 = 5
```

---

# Common Two-Pointer Patterns

## Reverse String

```python
s = list("hello")

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]

    left += 1
    right -= 1

print("".join(s))
```

Output:

```text
olleh
```

---

## Palindrome Check

```python
s = "racecar"

left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)
```

Output:

```text
True
```

---

## Find Pair Sum

```python
nums = [1, 2, 3, 4, 6]
target = 7

left = 0
right = len(nums) - 1

while left < right:

    current = nums[left] + nums[right]

    if current == target:
        print(left, right)
        break

    elif current < target:
        left += 1

    else:
        right -= 1
```

Output:

```text
0 4
```

---

# Quick Study Checklist

Before taking the Unit 4 Assessment, make sure you can:

* [ ] Explain what the two-pointer approach is
* [ ] Use opposite-direction pointers
* [ ] Use same-direction pointers
* [ ] Know when pointers should stop
* [ ] Reverse a list using two pointers
* [ ] Check whether a string is a palindrome
* [ ] Merge sorted lists
* [ ] Understand sliding windows
* [ ] Extract windows using slicing
* [ ] Use unpacking
* [ ] Swap variables using unpacking
* [ ] Swap list elements using unpacking
* [ ] Identify when a problem can be solved with two pointers

---

# Key Takeaway

Unit 4 is primarily about recognizing when two positions in a data structure should be tracked simultaneously.

The three major patterns to master are:

1. **Opposite Direction Pointers** → Reverse arrays, palindromes, pair sums
2. **Same Direction Pointers** → Merge sorted structures, subsequences
3. **Sliding Window** → Subarray and substring problems

Most Unit 4 assessment problems can be solved using one of these patterns.
