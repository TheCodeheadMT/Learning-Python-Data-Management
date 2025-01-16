# Lesson 4: Introduciton and Basic Operations with Pandas

## What is pandas?

Pandas is a powerful and flexible Python library for data manipulation and analysis. It provides data structures like Series and DataFrame that make it easy to work with structured data. It is widely used in data science, analytics, and machine learning.

## Installing pandas

To use pandas, you need to install it. Below are instructions for Windows and macOS.

### Windows
1. Open the Command Prompt.
2. Run the following command:
    ```bash
    pip install pandas
    ```

### macOS
1. Open the Terminal.
2. Run the following command:
    ```bash
    pip install pandas
    ```

To verify the installation, you can import pandas in a Python shell:
```python
import pandas as pd
print(pd.__version__)
```

## Data Types in pandas

Pandas primarily works with two main data structures:

1. **Series**: A one-dimensional array-like object containing elements of the same type.
    Example:
    ```python
    import pandas as pd

    data = [10, 20, 30]
    series = pd.Series(data)
    print(series)
    ```

2. **DataFrame**: A two-dimensional labeled data structure, similar to a table.
    Example:
    ```python
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
    df = pd.DataFrame(data)
    print(df)
    ```

## Previewing Data

You can preview data in a DataFrame using the following methods:

1. **Top 10 rows**:
    ```python
    print(df.head(10))
    ```

2. **Bottom 10 rows**:
    ```python
    print(df.tail(10))
    ```

3. **Specific range of rows**:
    ```python
    print(df[2:5])
    ```

## Operations on Rows and Columns

Pandas provides various operations for working with rows and columns.

### Selecting Columns
You can select a single column or multiple columns:
```python
# Single column
print(df['Name'])

# Multiple columns
print(df[['Name', 'Age']])
```

### Adding a Column
```python
df['City'] = ['New York', 'Los Angeles', 'Chicago']
print(df)
```

### Removing a Column
```python
df = df.drop(columns=['City'])
print(df)
```

### Filtering Rows
```python
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```

By following this guide, you can get started with pandas and perform basic operations with dataframes. With practice, you will discover more advanced features that make pandas an essential tool for data manipulation.
