# Lesson 4: Working with Lists and Dictionaries in Python

## Introduction

In this lesson, you will learn how to use Python to create and work with lists and dictionaries. Lists and dictionaries are fundamental data structures in Python that help you store and manage collections of data. By the end of this lesson, you will be able to:

1. Create and manipulate lists and dictionaries.
2. Understand the differences between them.
3. Perform common operations and avoid common mistakes.
4. Combine lists and dictionaries.
5. Use these data structures in real-world scenarios.

---

## What Are Lists and Dictionaries?

### Lists

A list is an ordered collection of items. You can think of it as a numbered container where each item has a specific position.

```python
# Example of a list
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

### Dictionaries

A dictionary is a collection of key-value pairs. Each key is unique and is used to retrieve the associated value.

```python
# Example of a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
```

---

## Basic Operations

### Lists

- **Add an element:**

```python
fruits.append("orange")  # Adds "orange" to the list
```

- **Remove an element:**

```python
fruits.remove("banana")  # Removes "banana" from the list
```

- **Access an element:**

```python
print(fruits[1])  # Prints the second item in the list
```

- **Iterate over a list:**

```python
for fruit in fruits:
    print(fruit)
```

### Dictionaries

- **Add or update a key-value pair:**

```python
person["job"] = "Engineer"  # Adds a new key-value pair
```

- **Remove a key-value pair:**

```python
del person["age"]  # Removes the key "age" and its value
```

- **Access a value by key:**

```python
print(person["name"])  # Prints "Alice"
```

- **Iterate over keys and values:**

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Differences Between Lists and Dictionaries

| Feature          | List    | Dictionary            |
| ---------------- | ------- | --------------------- |
| Ordered          | Yes     | No (Python 3.7+: Yes) |
| Access by        | Index   | Key                   |
| Duplicate values | Allowed | Keys must be unique   |

---

## Common Mistakes

1. **Index out of range (lists):**

   ```python
   fruits = ["apple"]
   print(fruits[1])  # Error: IndexError
   ```

2. **KeyError (dictionaries):**

   ```python
   print(person["height"])  # Error: KeyError
   ```

3. **Modifying a list while iterating:**

   ```python
   for fruit in fruits:
       fruits.remove(fruit)  # Unintended behavior
   ```

---

## Combining Lists and Dictionaries

### Concatenating Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)
```

### Combining Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
```

---

## Exercises

1. **Create and manipulate a list:**

   - Create a list of your favorite movies.
   - Add a new movie to the list.
   - Remove a movie from the list.
   - Print all movies using a loop.

2. **Create and manipulate a dictionary:**

   - Create a dictionary representing a book with keys like `title`, `author`, and `year`.
   - Add a new key-value pair for `genre`.
   - Update the `year`.
   - Print all key-value pairs.

3. **Real-world example:**

   - Create a dictionary where the keys are product names and the values are their prices.
   - Add a new product.
   - Print all products with prices greater than \$10.

---

By completing this lesson, you will have a solid understanding of how to work with lists and dictionaries in Python, enabling you to use them effectively in your own scripts.

