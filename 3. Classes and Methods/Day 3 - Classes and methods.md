
# Lesson 3: Understanding Python Classes and the `__main__` Method

## Objectives
1. Learn how to create a Python class with variables and methods.
2. Understand the difference between class variables and global variables.
3. Learn how the `__main__` method works and its purpose.
4. Learn how to call methods within a class and reference variables using the `self` keyword.
5. Execute a Python script containing a class from the command line.

---

## Creating a Python Class
A class in Python is defined using the `class` keyword. Here is a simple example:

```python
class Example:
    # This is a class variable
    class_variable = "I am a class variable"

    def __init__(self, value):
        # This is an instance variable
        self.instance_variable = value

    def show_variables(self):
        print("Class variable:", Example.class_variable)
        print("Instance variable:", self.instance_variable)
```

---

## Class Variables vs. Global Variables
- **Class Variables** are shared across all instances of a class.
- **Instance Variables** are unique to each instance of a class.
- **Global Variables** are defined outside any function or class and can be accessed anywhere in the module.

---

## The `__main__` Method
The `__main__` method is the entry point for Python programs. When a Python file is run directly, the code inside `if __name__ == "__main__":` is executed.

Example:
```python
if __name__ == "__main__":
    obj = Example("I am an instance variable")
    obj.show_variables()
```

---

## Using the `self` Keyword
The `self` keyword is used within class methods to reference instance variables and other methods.

Example:
```python
class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")
```

---

## Complete Example
Below is a complete example of a Python script that demonstrates these concepts:

```python
class Calculator:
    # Class variable
    operations = ["add", "subtract", "multiply", "divide"]

    def __init__(self, a, b):
        self.a = a  # Instance variable
        self.b = b  # Instance variable

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

if __name__ == "__main__":
    calc = Calculator(10, 5)
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
```

To execute this script:
1. Save it as `calculator.py`.
2. Open the terminal and run `python calculator.py`.

---

### Exercises
1. Create a class `Person` with attributes `name` and `age`. Add a method `greet` that prints a greeting message.
2. Modify the `Calculator` class to include `multiply` and `divide` methods.
3. Experiment with global variables inside and outside a class.
