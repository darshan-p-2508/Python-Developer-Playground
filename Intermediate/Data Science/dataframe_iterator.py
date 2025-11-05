"""
This script demonstrates different ways to iterate through a Pandas DataFrame.

It covers:
1. Creating a DataFrame from a dictionary.
2. Iterating through columns using the `.items()` method.
3. Iterating through rows using the `.iterrows()` method.
4. Accessing specific row data based on a condition.

Author: Darshan P
"""

# Importing the pandas library
import pandas as pd  # Using the standard alias 'pd' instead of 'pandas'

# Creating a dictionary that holds student names and their corresponding scores
student_dict = {
    "student": ["Alex", "Bob", "John"],
    "score": [56, 76, 98]
}

# Converting the dictionary into a Pandas DataFrame
student_data_frame = pd.DataFrame(student_dict)

# Displaying the DataFrame
print(student_data_frame)

# -------------------------------------------------------------------------
# Iterating through a DataFrame by columns
# The .items() method returns key-value pairs, where:
# - 'key' is the column name
# - 'value' is the column data as a Pandas Series
# -------------------------------------------------------------------------
for key, value in student_data_frame.items():
    print(f"Column Name: {key}")
    print(value)
    
# Note:
# This type of iteration is usually less useful for row-wise operations,
# as it loops over columns (first 'student', then 'score') rather than rows.

# -------------------------------------------------------------------------
# Iterating through a DataFrame by rows
# The .iterrows() method returns:
# - 'index': the row index
# - 'row': a Pandas Series representing each row
# -------------------------------------------------------------------------
for index, row in student_data_frame.iterrows():
    print(f"Row Index: {index}")
    print(row)

# -------------------------------------------------------------------------
# Accessing specific values from each row
# Since each 'row' is a Pandas Series, we can access values using dot notation.
# -------------------------------------------------------------------------
for index, row in student_data_frame.iterrows():
    # Print each student's name
    print(f"Student Name: {row.student}")
    
    # Example: Accessing the score of a specific student
    if row.student == "Alex":
        print(f"{row.student}'s Score: {row.score}")
