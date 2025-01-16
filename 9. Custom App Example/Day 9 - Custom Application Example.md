# Lesson 9: Creating a Command-Line Application with Python and Pandas

## Introduction
In this lesson, you will learn how to create a custom command-line application using Python and the Pandas library. The application will process a CSV file containing IP addresses and reformat them based on a custom function. By the end of this lesson, you will be able to:

1. Create a Python class for data manipulation.
2. Use the Pandas `apply` method for efficient data transformation.
3. Design a command-line interface for your application.
4. Handle errors gracefully to ensure a robust application.
5. Combine the code into a Python module.

---

## Step 1: Setting Up the `CleanIP` Class

The `CleanIP` class will modify IP addresses by replacing the last period (`.`) with `[.]`. Review the code below and read the comments to see how what you have learned so far is combined to create this application:

```python
import pandas as pd

# A custom class for your application.
class CleanIP:
    def __init__(self, filepath):
        self.filepath = filepath

    # A class vector transformation function to apply to modify each IP address string.
    def clean_ip(self, ip):
        # Replace the last period in the IP address with [.]
        return ip[::-1].replace('.', '[.]', 1)[::-1]
    
    # A class method to process the file provided by the command line.
    def process_file(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.filepath)

            # Check if the column 'IP' exists
            if 'IP' not in df.columns:
                raise ValueError("The CSV file is not formatted correctly. Missing 'IP' column.")

            # Apply the custom function to the 'IP' column
            df['Modified_IP'] = df['IP'].apply(self.clean_ip)

            # Save the modified DataFrame to a new file
            output_path = self.filepath.replace('.csv', '_modified.csv')
            df.to_csv(output_path, index=False)
            print(f"File processed successfully. Output saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")
```

---

## Step 2: Creating the Command-Line Interface

Next, create a script that accepts the CSV file path as an argument:

```python
import sys
from clean_ip import CleanIP

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_ip_app.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    app = CleanIP(filepath)
    app.process_file()
```

---

## Step 3: Example Input File

Create a sample CSV file named `input_ips.csv` with the following content:

```
IP
192.168.1.1
10.0.0.1
172.16.0.1
8.8.8.8
192.168.0.1
10.10.10.10
255.255.255.0
127.0.0.1
1.1.1.1
224.0.0.5
```

---

## Step 4: Running the Script

To run the script, use the following command in your terminal:

```bash
python clean_ip_app.py input_ips.csv
```

### Example Output

If the input file is `input_ips.csv`, the script will create a new file named `input_ips_modified.csv` with the following content:

```
IP,Modified_IP
192.168.1.1,192.168.1[.]1
10.0.0.1,10.0.0[.]1
172.16.0.1,172.16.0[.]1
8.8.8.8,8.8.8[.]8
192.168.0.1,192.168.0[.]1
10.10.10.10,10.10.10[.]10
255.255.255.0,255.255.255[.]0
127.0.0.1,127.0.0[.]1
1.1.1.1,1.1.1[.]1
224.0.0.5,224.0.0[.]5
```

---

## Step 5: Combining the Code into a Python Module

Here is the complete code as a single Python module:

### `clean_ip.py`

```python
import pandas as pd

class CleanIP:
    def __init__(self, filepath):
        self.filepath = filepath

    def clean_ip(self, ip):
        return ip[::-1].replace('.', '].[', 1)[::-1]

    def process_file(self):
        try:
            df = pd.read_csv(self.filepath)
            if 'IP' not in df.columns:
                raise ValueError("The CSV file is not formatted correctly. Missing 'IP' column.")

            df['Modified_IP'] = df['IP'].apply(self.clean_ip)
            output_path = self.filepath.replace('.csv', '_modified.csv')
            df.to_csv(output_path, index=False)
            print(f"File processed successfully. Output saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")
```

### `clean_ip_app.py`

```python
import sys
from clean_ip import CleanIP

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_ip_app.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    app = CleanIP(filepath)
    app.process_file()
```

---

## Step 6: Suggestions for Customization

Here are some ways to extend the application:

1. **Add Support for Other Formats**: Allow the application to process Excel or JSON files in addition to CSV files.
2. **Additional Transformations**: Implement other modifications to the IP addresses, such as anonymizing specific segments.
3. **Logging**: Add a logging mechanism to track errors and processing details.
4. **Multithreading**: Optimize processing for large files by enabling parallel execution.

---

## Conclusion
This lesson guided you through creating a Python-based command-line application using the Pandas library. By completing this task, you learned how to:

- Design and implement a class for data manipulation.
- Use the Pandas `apply` method effectively.
- Create a robust command-line interface.

Continue exploring the possibilities by customizing the application to suit your needs!

