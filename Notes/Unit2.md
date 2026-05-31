# Unit 2 Cheatsheet

A quick reference sheet for Unit 2. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Create and modify dictionaries
* Access and loop through keys, values, and key-value pairs
* Solve problems using frequency maps
* Solve problems involving lists, dictionaries, or combinations of both

---

# General Concepts ✅ In-Scope

# Built-In Functions

## Type Casting

Type casting is the process of converting data from one type into another.

---

### int(x)

```python
int(x)
```

Converts a float or string into an integer.

### Parameters

* `x` — Float or string to convert

### Notes

* Floats are rounded **down** (truncated)
* Returns an integer

### Examples

```python
x = int(2.5)      # 2
y = int("5")      # 5
```

---

### float(x)

```python
float(x)
```

Converts an integer or string into a floating-point number.

### Parameters

* `x` — Integer or string to convert

### Examples

```python
x = float(2)      # 2.0
y = float("5")    # 5.0
z = float("5.3")  # 5.3
```

---

### str(x)

```python
str(x)
```

Converts a value into a string.

### Parameters

* `x` — Any data type

### Examples

```python
x = str(2)                # "2"
y = str(2.0)              # "2.0"
z = str([1, 2, 3, 4])     # "[1, 2, 3, 4]"
```

---

# Remainder Division (Modulo)

The `%` operator returns the remainder after division.

```python
x % y
```

### Examples

```python
print(5 % 2)
```

Output:

```text
1
```

Because:

```text
5 ÷ 2 = 2 remainder 1
```

---

```python
print(10 % 2)
```

Output:

```text
0
```

Because:

```text
10 ÷ 2 = 5 remainder 0
```

---

# Sum

```python
sum(x)
```

Returns the sum of all values in a list.

### Example

```python
sum([1, 2, 3, 4])
```

Returns:

```text
10
```

---

# Min

```python
min(x)
```

Returns the smallest item.

### Example 1: List

```python
min([2, 3, 4, 1, 5])
```

Returns:

```text
1
```

---

### Example 2: Multiple Values

```python
min(5, 2, 3)
```

Returns:

```text
2
```

---

### Example 3: Strings

```python
min(['a', 'b', 'c', 'aa'])
```

Returns:

```text
'a'
```

---

### Example 4: Dictionary Keys

```python
min({'a': 1, 'b': 2, 'c': 3, 'd': 4})
```

Returns:

```text
'a'
```

---

# Max

```python
max(x)
```

Returns the largest item.

### Example 1: List

```python
max([2, 3, 5, 1, 4])
```

Returns:

```text
5
```

---

### Example 2: Multiple Values

```python
max(5, 2, 3)
```

Returns:

```text
5
```

---

### Example 3: Strings

```python
max(['a', 'b', 'c', 'aa'])
```

Returns:

```text
'c'
```

---

### Example 4: Dictionary Keys

```python
max({'a': 1, 'b': 2, 'c': 3, 'd': 4})
```

Returns:

```text
'd'
```

---

# Dictionary Methods & Syntax

## Creating a Dictionary

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

---

## Setting and Updating Values

Add new key-value pairs or update existing ones using `=`.

### Add New Key

```python
d["d"] = 4

print(d)
```

Output:

```text
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

### Update Existing Key

```python
d["a"] = 100

print(d)
```

Output:

```text
{'a': 100, 'b': 2, 'c': 3, 'd': 4}
```

---

# Accessing Elements

## Method 1: Direct Access

```python
d[key]
```

Returns the value associated with a key.

⚠️ Raises a `KeyError` if the key does not exist.

### Example

```python
d = {'a': 1, 'b': 2, 'c': 3}

print(d['a'])
print(d['b'])
```

Output:

```text
1
2
```

---

## Method 2: get()

```python
d.get(key, default_value)
```

Safely accesses a key.

### Parameters

| Parameter     | Description                          |
| ------------- | ------------------------------------ |
| key           | Key to search for                    |
| default_value | Value returned if key does not exist |

### Examples

```python
d = {'a': 1, 'b': 2, 'c': 3}

print(d.get('a'))
```

Output:

```text
1
```

---

```python
print(d.get('z'))
```

Output:

```text
None
```

---

```python
print(d.get('z', 'Not Found'))
```

Output:

```text
Not Found
```

---

# Pop Method

```python
d.pop(key, default_value)
```

Removes a key-value pair and returns the value.

### Example 1: Without Default Value

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d.pop('a')
```

Returns:

```text
1
```

Dictionary becomes:

```python
{'b': 2, 'c': 3, 'd': 4}
```

---

```python
d.pop('e')
```

Raises:

```text
KeyError
```

---

### Example 2: With Default Value

```python
d.pop('a', None)
```

Returns:

```text
1
```

---

```python
d.pop('e', None)
```

Returns:

```text
None
```

No error occurs.

---

# Keys Method

```python
d.keys()
```

Returns all dictionary keys.

### Example

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(d.keys())
```

Output:

```text
dict_keys(['a', 'b', 'c', 'd'])
```

---

# Values Method

```python
d.values()
```

Returns all dictionary values.

### Example

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(d.values())
```

Output:

```text
dict_values([1, 2, 3, 4])
```

---

# Items Method

```python
d.items()
```

Returns key-value pairs as tuples.

### Example

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(d.items())
```

Output:

```text
dict_items([
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4)
])
```

---

# Looping Through Dictionaries

## Loop Through Keys

```python
for key in d:
    print(key)
```

---

## Loop Through Values

```python
for value in d.values():
    print(value)
```

---

## Loop Through Key-Value Pairs

```python
for key, value in d.items():
    print(key, value)
```

Output:

```text
a 1
b 2
c 3
d 4
```

---

# Frequency Map Pattern

One of the most important Unit 2 concepts.

### Counting Occurrences

```python
nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

Output:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

This pattern appears frequently in interview questions.

---

# Bonus Concepts 💡 Not In-Scope

These concepts are useful but not required for Unit 2 assessments.

| Function        | Description                                           |
| --------------- | ----------------------------------------------------- |
| `remove(x)`     | Removes first occurrence of value `x` from a list     |
| `zip()`         | Iterates through multiple lists simultaneously        |
| `defaultdict()` | Automatically creates default values for missing keys |
| `d.copy()`      | Returns a copy of a dictionary                        |
| `sorted(x)`     | Returns a sorted copy                                 |

---

## sorted() vs sort()

### sort()

```python
nums = [3, 1, 2]

nums.sort()

print(nums)
```

Output:

```text
[1, 2, 3]
```

* Changes the original list
* Works only on lists

---

### sorted()

```python
nums = [3, 1, 2]

new_nums = sorted(nums)

print(new_nums)
```

Output:

```text
[1, 2, 3]
```

* Does **not** modify original data
* Works on lists, tuples, dictionaries, strings, and more

---

# Quick Study Checklist

Before taking the Unit 2 Assessment, make sure you can:

* [ ] Use `int()`, `float()`, and `str()`
* [ ] Use the `%` operator
* [ ] Use `sum()`
* [ ] Use `min()`
* [ ] Use `max()`
* [ ] Create dictionaries
* [ ] Add and update key-value pairs
* [ ] Access values using `[]`
* [ ] Access values using `get()`
* [ ] Remove values using `pop()`
* [ ] Use `keys()`
* [ ] Use `values()`
* [ ] Use `items()`
* [ ] Loop through dictionaries
* [ ] Build frequency maps
* [ ] Solve problems involving lists and dictionaries together
