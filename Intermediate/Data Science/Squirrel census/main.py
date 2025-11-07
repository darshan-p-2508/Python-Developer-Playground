import pandas  # Import the pandas library for data manipulation

# Read the CSV file into a pandas DataFrame, which allows you to work with the data
data = pandas.read_csv("2018_CPSquirrel_Data.csv")

# Count the number of rows in the DataFrame where the 'Primary Fur Color' is "Gray"
# This assumes that the column "Primary Fur Color" exists and contains this specific value
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels)  # Output the number of gray squirrels

# Count the number of rows in the DataFrame where the 'Primary Fur Color' is "Cinnamon"
# 'Cinnamon' is being used as the identifier for red squirrels in this dataset
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels)  # Output the number of red squirrels

# Count the number of rows in the DataFrame where the 'Primary Fur Color' is "Black"
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels)  # Output the number of black squirrels

# Create a dictionary to organize the fur color data and counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],  # List of fur colors
    "Count": [gray_squirrels, red_squirrels, black_squirrels]  # Corresponding counts for each color
}

# Convert the dictionary into a pandas DataFrame for structured representation
df = pandas.DataFrame(data_dict)

# Write the DataFrame to a new CSV file, storing the count data
df.to_csv("squirrel_count.csv", index=False)  # 'index=False' prevents pandas from writing row indices to the file
print("File 'squirrel_count.csv' created")  # Notify the user that the file has been created
