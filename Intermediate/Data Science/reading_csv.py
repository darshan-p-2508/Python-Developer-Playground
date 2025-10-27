# one way to read the csv files:
with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)

print("-" * 75)

# using the csv library:
import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    # print(data) # prints the memory where the object is created (not readable)
    for row in data:
        print(row)  # now we get eash row as a list making it more readable

print("-" * 75)

# to read only the first column of the data table
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for r in data:
        if r[1] != "temp":
            temperatures.append(int(r[1]))
    print(temperatures)

"""
This is easy to use for simple files and smaller files
for larger files we need another powerful library to handle huge data; Pandas
To install Pandas: head over to cmd, type "pip install pandas", hit enter
"""

print("-" * 75)

import pandas as p

data = p.read_csv("weather_data.csv")
print(data)
# to print specific column, give the column name:
print(data["temp"])
