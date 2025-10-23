import pandas

data = pandas.read_csv("2018_CPSquirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels)
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels)
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print("File 'squirrel_count.csv' created")
