# Lesson 6: Working with Pandas DataFrames

## Learning Objectives

1. Understand how to use Python's pandas package to create a custom dataframe using lists and dictionaries.
2. Learn how to import the pandas package.
3. Create dataframes from lists and dictionaries.
4. Modify dataframes by adding and updating fields.
5. Save dataframes to disk as CSV files.
6. Load dataframes from CSV files with or without header or index information and print them.
7. Create a method to generate dataframes from lists or dictionaries.
8. Practice through exercises to create and manipulate dataframes.

---

## Lesson Content

### 1. Importing the pandas Package
To use pandas, we must first import it into our Python script. The standard convention is:
```python
import pandas as pd
```
This imports pandas and allows us to use it with the shorthand `pd`.

---

### 2. Creating DataFrames
#### a. Using a List
To create a dataframe from a list:
```python
import pandas as pd

# Create a list of data
data = ["Apple", "Banana", "Cherry"]

# Convert the list into a dataframe
df_list = pd.DataFrame(data, columns=["Fruit"])

print(df_list)
```
Output:
```
    Fruit
0   Apple
1  Banana
2  Cherry
```

#### b. Using a Dictionary
To create a dataframe from a dictionary:
```python
# Create a dictionary of data
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}

# Convert the dictionary into a dataframe
df_dict = pd.DataFrame(data)

print(df_dict)
```
Output:
```
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
```

---

### 3. Adding and Updating Fields
#### Adding a New Field:
```python
# Add a new column to the dataframe
df_dict["City"] = ["New York", "Los Angeles", "Chicago"]

print(df_dict)
```
Output:
```
      Name  Age          City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
```

#### Updating an Existing Field:
```python
# Update a column
df_dict["Age"] = [26, 31, 36]

print(df_dict)
```
Output:
```
      Name  Age          City
0    Alice   26     New York
1      Bob   31  Los Angeles
2  Charlie   36      Chicago
```

---

### 4. Saving DataFrames to Disk
To save a dataframe to a CSV file:
```python
# Save the dataframe to a CSV file
df_dict.to_csv("output.csv", index=False)
```
This will create a file named `output.csv` without the index column.

---

### 5. Loading DataFrames from CSV Files
To load a dataframe from a CSV file:
```python
# Load the dataframe from the CSV file
loaded_df = pd.read_csv("output.csv")

print(loaded_df)
```
Output:
```
      Name  Age          City
0    Alice   26     New York
1      Bob   31  Los Angeles
2  Charlie   36      Chicago
```

You can also load the file without headers or index information:
```python
loaded_df_no_header = pd.read_csv("output.csv", header=None)
print(loaded_df_no_header)
```

---

### 6. Creating a Method for DataFrame Creation
Below is a method to create a dataframe from either a list or a dictionary:
```python
def create_dataframe(data):
    if isinstance(data, list):
        return pd.DataFrame(data, columns=["Column1"])
    elif isinstance(data, dict):
        return pd.DataFrame(data)
    else:
        raise ValueError("Input must be a list or dictionary")

# Example usage
print(create_dataframe(["A", "B", "C"]))
print(create_dataframe({"X": [1, 2], "Y": [3, 4]}))
```

---

### 7. Exercises
1. Create a dataframe using a list of integers from 1 to 10. Save it as `numbers.csv` and then load it back into a dataframe.
2. Create a dataframe using a dictionary with keys `"Product"` and `"Price"`. Fill it with 5 products and their prices. Save the dataframe and load it back without headers.
3. Write a method to add a column to any given dataframe with values passed as a list.

---

## Summary
By completing this lesson, you have learned to:
- Import the pandas package.
- Create, modify, and save dataframes.
- Load dataframes from CSV files.
- Write methods to automate dataframe creation.

### Next Steps
Continue practicing by experimenting with pandas features like filtering, grouping, and analyzing data to prepare for more advanced tasks in Python scripting.

