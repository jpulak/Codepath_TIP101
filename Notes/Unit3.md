# Unit 3 Cheatsheet

A quick reference sheet for Unit 3. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Insert variables and Python expressions into strings
* Index and access subsections of a string
* Loop over strings
* Solve problems involving strings, lists, dictionaries, or combinations of all three

---

# General Concepts ✅ In-Scope

# String Methods & Syntax

## Lower Method

```python
s.lower()
```

Returns a lowercase version of the string.

### Parameters

* None

### Examples

```python
# Example 1: Mixed Case
s = "Hello World!"
lowered = s.lower()

print(lowered)
```

Output:

```text
hello world!
```

---

```python
# Example 2: Uppercase
s = "HELLO WORLD"
lowered = s.lower()

print(lowered)
```

Output:

```text
hello world
```

---

# Split Method

```python
s.split(separator)
```

Splits a string into a list.

### Parameters

| Parameter | Description                                      |
| --------- | ------------------------------------------------ |
| separator | Character(s) used to split the string (optional) |

### Notes

* Default separator is whitespace
* Returns a list of substrings

### Examples

```python
# Example 1: Split by whitespace
s = "Never gonna give you up"

parts = s.split()

print(parts)
```

Output:

```python
['Never', 'gonna', 'give', 'you', 'up']
```

---

```python
# Example 2: Split by dash
s = "Never-gonna-let-you-down"

parts = s.split("-")

print(parts)
```

Output:

```python
['Never', 'gonna', 'let', 'you', 'down']
```

---

# Join Method

```python
separator.join(iterable)
```

Combines elements into a string using the separator.

### Parameters

| Parameter | Description                         |
| --------- | ----------------------------------- |
| iterable  | List or iterable containing strings |

### Examples

```python
lst = ["Never", "gonna", "run", "around", "and", "desert", "you"]

result = " ".join(lst)

print(result)
```

Output:

```text
Never gonna run around and desert you
```

---

```python
lst = ["Never", "gonna", "make", "you", "cry"]

result = "-".join(lst)

print(result)
```

Output:

```text
Never-gonna-make-you-cry
```

---

# Strip Method

```python
s.strip(characters)
```

Removes whitespace or specified characters from both ends of a string.

### Parameters

| Parameter  | Description                     |
| ---------- | ------------------------------- |
| characters | Characters to remove (optional) |

### Examples

```python
s = "       Never gonna say goodbye       "

result = s.strip()

print(result)
```

Output:

```text
Never gonna say goodbye
```

---

```python
s = "????Never gonna tell a lie and hurt you????"

result = s.strip("?")

print(result)
```

Output:

```text
Never gonna tell a lie and hurt you
```

---

# String Indexing

Strings use zero-based indexing.

```python
word = "python"

print(word[0])
print(word[2])
print(word[-1])
```

Output:

```text
p
t
n
```

---

# String Slicing

```python
string[start:end]
```

Returns part of a string.

### Examples

```python
word = "python"

print(word[1:4])
```

Output:

```text
yth
```

---

```python
print(word[:3])
```

Output:

```text
pyt
```

---

```python
print(word[3:])
```

Output:

```text
hon
```

---

# Looping Through Strings

## Loop Through Characters

```python
word = "code"

for char in word:
    print(char)
```

Output:

```text
c
o
d
e
```

---

## Loop Through Indices

```python
word = "code"

for i in range(len(word)):
    print(i, word[i])
```

Output:

```text
0 c
1 o
2 d
3 e
```

---

# Tuples

A tuple stores multiple values together.

Tuples use parentheses:

```python
my_tuple = ("Mario", "Luigi")
```

### Example

```python
my_tuple = ("Mario", "Luigi")

print(my_tuple)
```

Output:

```text
('Mario', 'Luigi')
```

---

## Accessing Tuple Elements

```python
my_tuple = ("Mario", "Luigi")

mario = my_tuple[0]
luigi = my_tuple[1]

print(mario)
print(luigi)
```

Output:

```text
Mario
Luigi
```

---

## Tuple Immutability

Tuples cannot be modified.

```python
my_tuple = (10, 20)

my_tuple[0] = 30
```

Results in:

```text
TypeError: 'tuple' object does not support item assignment
```

---

# Built-In Functions

# Round Function

```python
round(number, decimals)
```

Rounds a number.

### Parameters

| Parameter | Description                         |
| --------- | ----------------------------------- |
| number    | Number to round                     |
| decimals  | Number of decimal places (optional) |

### Examples

```python
x = 3.14159

print(round(x, 2))
```

Output:

```text
3.14
```

---

```python
x = 3.14159

print(round(x))
```

Output:

```text
3
```

---

# Enumerate

```python
enumerate(iterable, start=0)
```

Returns index-value pairs.

### Example 1: String

```python
my_string = "code"

for index, char in enumerate(my_string):
    print(index, char)
```

Output:

```text
0 c
1 o
2 d
3 e
```

---

### Example 2: Custom Start Value

```python
cereals = ["cheerios", "fruity pebbles", "cocoa puffs"]

for count, cereal in enumerate(cereals, start=1):
    print(count, cereal)
```

Output:

```text
1 cheerios
2 fruity pebbles
3 cocoa puffs
```

---

# Zip

```python
zip(x, y)
```

Combines multiple iterables together.

### Example 1

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)

print(list(zipped))
```

Output:

```python
[('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

---

### Example 2: Different Lengths

```python
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]

zipped = zip(names, ages)

print(list(zipped))
```

Output:

```python
[('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

> Zip stops at the shortest iterable.

---

# Comparing Strings and Lists

## Similarities

| Feature          | Strings | Lists |
| ---------------- | ------- | ----- |
| Ordered Sequence | ✅       | ✅     |
| Indexed          | ✅       | ✅     |
| Sliceable        | ✅       | ✅     |
| Iterable         | ✅       | ✅     |
| Works with len() | ✅       | ✅     |

---

## Differences

### Content Type

**Strings**

```python
"hello"
```

Contain only characters.

**Lists**

```python
[1, "hello", [1, 2]]
```

Can contain any data type.

---

### Mutability

#### Strings are Immutable

```python
s = "Try"

s[0] = "C"
```

Results in:

```text
TypeError
```

---

#### Lists are Mutable

```python
lst = ["T", "r", "y"]

lst[0] = "C"

print(lst)
```

Output:

```python
['C', 'r', 'y']
```

---

# Common String Problem Patterns

## Count Characters

```python
s = "banana"

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)
```

Output:

```python
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

---

## Reverse a String

```python
s = "hello"

reversed_s = s[::-1]

print(reversed_s)
```

Output:

```text
olleh
```

---

## Check for Palindrome

```python
s = "racecar"

print(s == s[::-1])
```

Output:

```text
True
```

---

# Bonus Concepts 💡 Not In-Scope

These concepts are useful but not required for Unit 3 assessments.

| Function      | Description                                           |
| ------------- | ----------------------------------------------------- |
| `s.isalpha()` | Returns True if all characters are letters            |
| `s.isalnum()` | Returns True if all characters are letters or numbers |
| `s.find(x)`   | Returns first index of substring, or -1               |
| `s.count(x)`  | Counts occurrences of substring                       |
| `set()`       | Creates a set of unique values                        |

---

## isalpha()

```python
"hello".isalpha()
```

Returns:

```text
True
```

---

## isalnum()

```python
"abc123".isalnum()
```

Returns:

```text
True
```

---

## find()

```python
"banana".find("na")
```

Returns:

```text
2
```

---

## count()

```python
"banana".count("a")
```

Returns:

```text
3
```

---

## Sets

Sets store unique values.

```python
nums = {1, 2, 3, 3, 2}

print(nums)
```

Output:

```python
{1, 2, 3}
```

Properties:

* No duplicates
* Unordered
* Fast lookup

---

# Quick Study Checklist

Before taking the Unit 3 Assessment, make sure you can:

* [ ] Use `lower()`
* [ ] Use `split()`
* [ ] Use `join()`
* [ ] Use `strip()`
* [ ] Access string characters using indexing
* [ ] Slice strings
* [ ] Loop through strings
* [ ] Understand tuples
* [ ] Use `round()`
* [ ] Use `enumerate()`
* [ ] Use `zip()`
* [ ] Explain differences between strings and lists
* [ ] Solve frequency-counting problems
* [ ] Manipulate and analyze strings
* [ ] Combine strings, lists, and dictionaries in solutions
