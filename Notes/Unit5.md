# Unit 5 Cheatsheet

A quick reference sheet for Unit 5. While not an exhaustive list, it highlights the key syntax and concepts you'll use in this unit, plus a few optional ideas that may help with problem-solving.

> **Note:** You are still expected to know required material from earlier units.

---

## Legend

* ✅ **In-Scope:** May appear on the assessment
* 💡 **Not In-Scope:** Useful, but not required

---

# 🎯 Unit Goals

* Define and use classes and objects
* Use class attributes and methods to manage object data
* Create and manipulate a singly linked list
* Solve problems requiring traversal of a singly linked list

---

# General Concepts ✅ In-Scope

# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that uses **objects** and their interactions to build software.

Python already provides built-in object types such as:

* Integers (`int`)
* Floating-point numbers (`float`)
* Strings (`str`)
* Lists (`list`)
* Dictionaries (`dict`)

The power of OOP is that it allows us to create our own custom data types using **classes**.

---

# Classes

A **class** is a blueprint for creating objects.

Classes define:

## Properties (Attributes)

Variables that describe an object.

Examples:

* Name
* Age
* Breed
* Owner

---

## Methods

Functions that define behavior.

Examples:

* Walk
* Bark
* Drive
* Print information

---

# Defining a Class

Example: Creating a `Dog` class

```python
class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
```

---

# Understanding the Constructor

The constructor is the special method:

```python
__init__()
```

Its purpose is to initialize a new object.

### Syntax

```python
class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
```

### Parameters

| Parameter | Description                  |
| --------- | ---------------------------- |
| self      | Refers to the current object |
| name      | Dog's name                   |
| breed     | Dog's breed                  |
| owner     | Dog's owner                  |

---

# What is `self`?

`self` refers to the current instance of the class.

Python automatically supplies it when methods are called.

You do **not** pass it manually.

Example:

```python
my_dog = Dog("Fido", "Cocker Spaniel", "Ada")
```

Python automatically handles:

```python
self
```

behind the scenes.

---

# Instantiating a Class

Creating an object from a class is called **instantiation**.

```python
my_dog = Dog(
    "Fido",
    "Cocker Spaniel",
    "Ada Lovelace"
)
```

This creates a new `Dog` object.

---

# Class Properties

Properties are accessed using **dot notation**.

## Syntax

```python
object.property
```

### Example

```python
print(my_dog.name)
```

Output:

```text
Fido
```

---

# Class Methods

Methods are functions that belong to a class.

## Example

```python
class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def call_dog(self):
        print(f"Here {self.name}!")
```

---

# Calling a Method

Use dot notation.

```python
my_dog.call_dog()
```

Output:

```text
Here Fido!
```

---

# Methods with Parameters

Methods can take additional parameters.

```python
class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")
```

Calling the method:

```python
my_dog.command_trick("roll over")
```

Output:

```text
Fido, roll over!
```

---

# Complete Example

```python
class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def call_dog(self):
        print(f"Here {self.name}!")

    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")


my_dog = Dog(
    "Fido",
    "Cocker Spaniel",
    "Ada Lovelace"
)

print(my_dog.name)

my_dog.call_dog()
my_dog.command_trick("roll over")
```

Output:

```text
Fido
Here Fido!
Fido, roll over!
```

---

# Linked Lists

A linked list is a data structure used to store ordered data.

Like Python lists:

* Stores multiple values
* Maintains order

Unlike Python lists:

* Nodes are not stored consecutively in memory
* Each node stores a pointer to the next node

---

# Linked Lists vs Arrays

## Python List (Array)

```text
[U][B][F][D][A][E]
```

Memory:

```text
200 201 202 203 204 205
```

Stored consecutively.

---

## Linked List

```text
U -> B -> F -> D -> A -> E -> None
```

Memory might look like:

```text
200 -> 512 -> 98 -> 301 -> 700 -> 12
```

Nodes can be anywhere in memory.

---

# Nodes

Each element in a linked list is called a **Node**.

A node contains:

1. A value
2. A reference to the next node

---

## Node Structure

```text
+-------+-------+
| value | next  |
+-------+-------+
```

Example:

```text
+----+------+
| 42 | None |
+----+------+
```

---

# Defining a Node Class

```python
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

---

# Creating Nodes

```python
node1 = Node(10)
node2 = Node(20)

node1.next = node2
```

Structure:

```text
10 -> 20 -> None
```

---

# Linked List Class

Sometimes interview questions provide a LinkedList class.

Example skeleton:

```python
class LinkedList:

    def __init__(self):
        self.head = None

    def add_first(self, value):
        pass

    def append(self, value):
        pass

    def length(self):
        pass

    def get_at_index(self, index):
        pass
```

---

# The Head Node

The first node in a linked list is called the **head**.

Example:

```text
head
 ↓
10 -> 20 -> 30 -> None
```

The head allows access to the entire list.

---

# Linked List Traversal

Traversal means visiting every node in the list.

---

## Traversal Steps

### Step 1

Create a pointer.

```python
current = head
```

---

### Step 2

Continue while a node exists.

```python
while current:
```

---

### Step 3

Perform work.

```python
print(current.value)
```

---

### Step 4

Move to the next node.

```python
current = current.next
```

---

# Traversal Template

```python
current = head

while current:

    # Process node

    current = current.next
```

---

# Complete Traversal Example

```python
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node3 = Node(30)
node2 = Node(20, node3)
node1 = Node(10, node2)

head = node1

current = head

while current:
    print(current.value)

    current = current.next
```

Output:

```text
10
20
30
```

---

# Common Interview Pattern

Many linked list interview questions follow this exact structure:

```python
current = head

while current:

    # Perform operation

    current = current.next
```

Examples:

* Count nodes
* Find maximum value
* Find minimum value
* Search for a value
* Reverse a linked list
* Detect cycles

---

# Visual Example

```text
head
 ↓
[10] → [20] → [30] → None
```

Traversal:

```text
current = 10
current = 20
current = 30
current = None
```

Loop ends when:

```python
current == None
```

---

# Common Mistakes

## Forgetting `.next`

Incorrect:

```python
current = current
```

Infinite loop.

Correct:

```python
current = current.next
```

---

## Forgetting the Head

Incorrect:

```python
while head:
```

Modifies your head pointer.

Preferred:

```python
current = head

while current:
```

---

## Accessing None

Incorrect:

```python
print(current.next.value)
```

May cause:

```text
AttributeError
```

Always verify the next node exists.

---

# Bonus Concepts 💡 Not In-Scope

These are useful but are **not required** for Unit 5 assessments.

| Method          | Description                            |
| --------------- | -------------------------------------- |
| `lst.extend(x)` | Appends all elements from iterable `x` |
| `lst.reverse()` | Reverses a list in place               |

---

## extend()

```python
nums = [1, 2]

nums.extend([3, 4])

print(nums)
```

Output:

```python
[1, 2, 3, 4]
```

---

## reverse()

```python
nums = [1, 2, 3]

nums.reverse()

print(nums)
```

Output:

```python
[3, 2, 1]
```

---

# Quick Study Checklist

Before taking the Unit 5 Assessment, make sure you can:

* [ ] Explain Object-Oriented Programming
* [ ] Define a class
* [ ] Write a constructor (`__init__`)
* [ ] Understand the purpose of `self`
* [ ] Instantiate objects
* [ ] Access object properties
* [ ] Create class methods
* [ ] Call methods using dot notation
* [ ] Explain what a linked list is
* [ ] Explain the difference between arrays and linked lists
* [ ] Define a Node class
* [ ] Understand the head node
* [ ] Traverse a linked list
* [ ] Use a `current` pointer
* [ ] Know when traversal stops (`current == None`)

---

# Key Takeaway

Unit 5 introduces two major concepts:

1. **Object-Oriented Programming (OOP)** — creating custom classes, objects, properties, and methods.
2. **Linked Lists** — node-based data structures that are traversed using pointers.

The most important coding pattern for this unit is:

```python
current = head

while current:
    # Process node

    current = current.next
```

Mastering this traversal pattern will help solve most linked list interview questions in Unit 5.
