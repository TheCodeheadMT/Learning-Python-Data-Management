# Lesson 2: Creating Methods in Python

## **Learning Objectives**
In this lesson, you will learn how to:

1. Create Python methods with and without parameters.
2. Specify types for method parameters.
3. Implement a method that returns a dictionary.

---

## **Examples**

### **Example 1: Method Without Parameters**
```python
# Define a method with no parameters
def greet():
    return "Hello, World!"

# Call the method
greeting = greet()
print(greeting)
```
**Explanation:**
- This method, `greet`, has no parameters. It simply returns a static string when called.

---

### **Example 2: Method With Two Parameters (One Typed, One Untyped)**
```python
# Define a method with two parameters

def add_numbers(a: int, b):
    """
    Adds two numbers.

    Parameters:
        a (int): The first number, with a type specified.
        b: The second number, without a type specified.

    Returns:
        int: The sum of a and b.
    """
    return a + b

# Call the method
result = add_numbers(5, 7)
print(result)  # Output: 12
```
**Explanation:**
- The `add_numbers` method takes two parameters:
  - `a` specifies an integer type (`int`).
  - `b` does not specify a type, meaning it can accept any type.
- This flexibility allows you to use both strict and dynamic typing as needed.

---

### **Example 3: Method With One Typed Parameter Returning a Dictionary**
```python
# Define a method that returns a dictionary
def create_user_profile(username: str) -> dict:
    """
    Creates a user profile with the given username.

    Parameters:
        username (str): The username for the profile.

    Returns:
        dict: A dictionary representing the user profile.
    """
    return {
        "username": username,
        "status": "active",
    }

# Call the method
user_profile = create_user_profile("Alice")
print(user_profile)  # Output: {'username': 'Alice', 'status': 'active'}
```
**Explanation:**
- The method `create_user_profile` has one parameter, `username`, which is explicitly typed as a `str`.
- The method returns a dictionary containing user details.
- The return type (`-> dict`) is explicitly declared.

---

## **Conclusion**
- **Components of a Method:**
  - **Definition:** The `def` keyword starts the method definition.
  - **Name:** The method's name, e.g., `greet`.
  - **Parameters:** Optional placeholders for input values.
  - **Return Type:** Optional declaration of the return type.
  - **Body:** The block of code executed when the method is called.

By mastering these examples, you will confidently create Python methods with varying levels of complexity.
