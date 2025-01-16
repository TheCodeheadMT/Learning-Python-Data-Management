# Lesson 1: Introduction to Python

## Learning Objectives
1. Understand Python as a scripting language.
2. Learn how to create a basic Python script (Hello World).
3. Execute a Python script from the command line on Windows or MacOS.

---

## Part 1: What is Python?
Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. It is widely used for:

- Web development (e.g., Django, Flask)
- Data analysis and visualization (e.g., Pandas, Matplotlib)
- Artificial intelligence and machine learning (e.g., TensorFlow, PyTorch)
- Automation and scripting

### Strengths of Python:
- Easy to learn and use for beginners.
- Extensive library support for various tasks.
- Cross-platform compatibility (works on Windows, MacOS, Linux).
- Large, active community.

### Weaknesses of Python:
- Slower execution speed compared to compiled languages (e.g., C, C++).
- Not ideal for memory-intensive tasks.

### What are Variables in Python?
Variables are containers for storing data values. In Python, variables are created when you assign a value to them. Python is dynamically typed, meaning you don’t need to declare a variable’s type explicitly; Python determines it based on the value assigned.

#### Types of Variables:
1. **String (`str`)**: Used to store text values.
   ```python
   name = "Alice"
   ```

2. **Integer (`int`)**: Used to store whole numbers.
   ```python
   age = 25
   ```

3. **Float (`float`)**: Used to store decimal numbers.
   ```python
   height = 5.9
   ```

4. **Boolean (`bool`)**: Used to store `True` or `False` values.
   ```python
   is_student = True
   ```

5. **List (`list`)**: Used to store multiple items in a single variable.
   ```python
   colors = ["red", "blue", "green"]
   ```

6. **Dictionary (`dict`)**: Used to store data in key-value pairs.
   ```python
   person = {"name": "Alice", "age": 25}
   ```

7. **NoneType**: Represents the absence of a value.
   ```python
   x = None
   ```

#### Dynamic Typing in Python:
- Python variables can change type during execution because Python is dynamically typed.
   ```python
   x = 10       # x is an integer
   x = "hello" # now x is a string
   ```

#### Typing Variables Explicitly:
- Though Python is dynamically typed, you can use type hints for better code readability and maintainability.
   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```
---

## Part 2: Writing Your First Python Script
A Python script is a text file containing Python code. You will create a simple "Hello World" script to print a message to the screen.

### Steps:
1. **Open a Text Editor:**
   - On Windows: Use Notepad, VS Code, or any text editor.
   - On MacOS: Use TextEdit (in plain text mode), VS Code, or similar.

2. **Write the Code:**
   ```python
   # This is a simple Python script
   print("Hello, World!")
   ```
   Save the file with a `.py` extension (e.g., `hello.py`).

3. **Save the File:**
   - On Windows: Save to a folder like `C:\Users\YourName\Documents\`.
   - On MacOS: Save to a folder like `/Users/YourName/Documents/`.

---

## Part 3: Running a Python Script

### Step 1: Install Python
Before running Python scripts, ensure Python is installed on your system.
- Download and install Python from [https://www.python.org/](https://www.python.org/).
- Verify installation by running `python --version` or `python3 --version` in the command line.

### Step 2: Run the Script

#### On Windows:
1. Open the Command Prompt.
2. Navigate to the directory where you saved the script using the `cd` command:
   ```
   cd C:\Users\YourName\Documents
   ```
3. Run the script:
   ```
   python hello.py
   ```

#### On MacOS:
1. Open the Terminal.
2. Navigate to the directory where you saved the script using the `cd` command:
   ```
   cd /Users/YourName/Documents
   ```
3. Run the script:
   ```
   python3 hello.py
   ```

---

## Summary
By completing this lesson, you have:
- Learned what Python is and its strengths and weaknesses.
- Written and saved your first Python script.
- Executed a Python script using the command line on Windows or MacOS.
- Understood what variables are, their types, and how Python’s dynamic typing works.

Now you are ready to explore more advanced concepts in Python scripting!

