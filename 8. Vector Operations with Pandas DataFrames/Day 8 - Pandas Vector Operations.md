
# Lesson 8: Vector Operations with Pandas DataFrames
 

## Introduction
This lesson introduces vector operations using the Pandas Python package. You'll learn how to use the `apply` method and lambda functions to perform operations on DataFrame columns. Vector operations are faster and more efficient than nested loops because they leverage optimized, low-level code and parallel processing, reducing computational overhead. They are simpler and more readable, minimizing bugs associated with manual indexing and loop management. Additionally, vectorized operations take advantage of modern hardware, such as CPUs and GPUs, for significant performance gains, making them ideal for large-scale data processing.

---

## What are Vector Operations?
Vector operations allow you to apply a function across all elements of a Pandas Series or DataFrame column without using a loop. For example:
```python
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5])
squared = data ** 2  # Vectorized operation
print(squared)
```
Output:
```
0     1
1     4
2     9
3    16
4    25
dtype: int64
```

---

## Using `apply` and Lambda Functions
### Example 1: String Operation
```python
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']})
df['Name_Length'] = df['Name'].apply(lambda x: len(x))
print(df)
```
Output:
```
      Name  Name_Length
0    Alice            5
1      Bob            3
2  Charlie            7
```

### Example 2: Numeric Operation
```python
df = pd.DataFrame({'Value': [10, 20, 30]})
df['Double'] = df['Value'].apply(lambda x: x * 2)
print(df)
```
Output:
```
   Value  Double
0     10      20
1     20      40
2     30      60
```

### Example 3: Custom Function
You can also use `apply` with a custom function for more complex operations.
```python
def categorize_value(value):
    if value > 20:
        return 'High'
    elif value > 10:
        return 'Medium'
    else:
        return 'Low'

df = pd.DataFrame({'Value': [10, 20, 30]})
df['Category'] = df['Value'].apply(categorize_value)
print(df)
```
Output:
```
   Value  Category
0     10      Low
1     20   Medium
2     30     High
```

---

## Python Script Example
Below is a Python script that performs these operations and saves the results to a CSV file.

```python
import pandas as pd

# Create from dict or load data from CSV 
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Value': [10, 20, 30]})

# Create new columns using lambda functions
df['Name_Length'] = df['Name'].apply(lambda x: len(x))
df['Double'] = df['Value'].apply(lambda x: x * 2)

# Categorize values using a custom function
def categorize_value(value):
    if value > 20:
        return 'High'
    elif value > 10:
        return 'Medium'
    else:
        return 'Low'

df['Category'] = df['Value'].apply(categorize_value)

# Save to CSV
df.to_csv('output.csv', index=False)
```

---

## Exercises
1. Create a DataFrame with columns `Product` and `Price`. Use a lambda function to calculate a 10% discount for each product.
2. Write a script to load a CSV file, categorize a column of numeric values using a custom function, and save the result.
3. Practice creating custom functions and applying them to DataFrame columns using `apply`.
