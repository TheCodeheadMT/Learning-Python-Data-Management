
# Lesson 7: Advanced Dataframe Operations

## Learning Objectives
1. Introduce advanced methods to select values in columns or rows from dataframes using pandas.
2. Demonstrate selecting values from rows or columns using conditions.
3. Show how to create a new dataframe by selecting certain rows or columns from an existing dataframe.
4. Demonstrate selecting rows or columns using multiple conditions.
5. Explain how to use all built-in functions to access rows or columns by index, value, or field name.
6. Provide examples of each built-in method for accessing rows or columns by index, value, or field name.

---

## Lesson Content

### 1. Importing the Pandas Package
To begin, import the pandas library:
```python
import pandas as pd
```

### 2. Selecting Values by Conditions
You can use conditional statements to filter data in a dataframe.

Example:
```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95]}
df = pd.DataFrame(data)

# Select rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(filtered_df)
```

### 3. Creating a New Dataframe by Selecting Rows/Columns
You can create a new dataframe by selecting specific rows or columns.

Example:
```python
# Select only the 'Name' and 'Score' columns
new_df = df[['Name', 'Score']]
print(new_df)
```

### 4. Selecting with Multiple Conditions
Combine conditions using `&` (and), `|` (or), and `~` (not). Here are three examples:

#### Example 1: Using `&` (AND)
```python
# Select rows where Age > 25 AND Score > 90
filtered_df = df[(df['Age'] > 25) & (df['Score'] > 90)]
print("Using AND (&):", filtered_df)
```

#### Example 2: Using `|` (OR)
```python
# Select rows where Age > 30 OR Score < 90
filtered_df = df[(df['Age'] > 30) | (df['Score'] < 90)]
print("Using OR (|):", filtered_df)
```

#### Example 3: Using `~` (NOT)
```python
# Select rows where NOT (Age > 25 AND Score > 90)
filtered_df = df[~((df['Age'] > 25) & (df['Score'] > 90))]
print("Using NOT (~):", filtered_df)
```

### 5. Built-In Functions to Access Data
Pandas provides several built-in functions to access rows and columns.

#### Examples of Built-In Methods

- **`iloc`**: Access rows or columns by index.
- **`loc`**: Access rows or columns by label.
- **`at`**: Access a single value by label.
- **`iat`**: Access a single value by index.

```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95]}
df = pd.DataFrame(data)

# iloc: Access the second row (index 1)
row_by_index = df.iloc[1]
print("Using iloc:", row_by_index)

# loc: Access the row with label 1 (same as iloc in this case)
row_by_label = df.loc[1]
print("Using loc:", row_by_label)

# at: Access a single value (row 1, column 'Name')
value_by_label = df.at[1, 'Name']
print("Using at:", value_by_label)

# iat: Access a single value (row 1, column 0 by index)
value_by_index = df.iat[1, 0]
print("Using iat:", value_by_index)
```

---

## Exercises
1. Import the pandas library and create a dataframe with your own data.
2. Select rows where a numeric column has values greater than a specified threshold.
3. Create a new dataframe by selecting specific columns from the original dataframe.
4. Combine multiple conditions to filter rows and display the resulting dataframe.
5. Use at least two built-in methods (`iloc`, `loc`, `at`, `iat`) to access specific rows or columns.

---

## Summary
This lesson introduced advanced methods for selecting rows and columns in dataframes. You learned to:
- Filter rows using conditions.
- Create new dataframes from selected rows/columns.
- Combine multiple conditions for filtering.
- Use built-in pandas functions for accessing data efficiently.
