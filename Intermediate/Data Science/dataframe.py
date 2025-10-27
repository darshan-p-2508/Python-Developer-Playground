"""
The two primary data structues of pandas, Series(1-dimensional) and DataFrame(2-dimensional),
handles the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering
"""
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))   # DataFrame
print(type(data["temp"]))   # Series

# to get the table as a dictionary
data_dict = data.to_dict()
print(data_dict)

# to get the series as a list
temp_list = data["temp"].to_list()
print(temp_list)
# to find the average temperature:
print(sum(temp_list) / len(temp_list))

print(data["temp"].mean())    # provides the same result as above
print(data["temp"].max())    # to get the max value from the Series: temp

print(data["condition"])
print(data.condition)    # does the same as above line of code

# to get data from the rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# creating a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
# to store it into a file:
data.to_csv("new_data.csv")
