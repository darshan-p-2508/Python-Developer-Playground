# dictionaries

dict1 = {
    "Code": "Set of instructions.",
    "Function": "A piece of code that you easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(dict1["Code"])

# to add/edit key value
dict1["Loop"] = "Does the instructions until the condition fails."
print(dict1)
dict1["Indent"] = "The blank space of about 4 after loops/conditions given in python to define the scope of the parent instruction."
print(dict1["Indent"])

# printing entire dictionary
print(dict1)

# creating empty dictionary
dict2 = {}

# looping through dictionary
for d in dict1:
    print(d)    # returns only the keys in the dictionaries
    print(dict1[d])    # for getting the values
    
    
# wiping the existing dictionary
dict1 = {}
print(dict1)

# nesting list and dictionary in a dictionary
capitals = {
    "France": "Paris",
    "German": "Berlin"
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stittgart", "Berlin"]
}

# how to access "Lille"
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])    # to access "D"

# nested dict and list in a dict
travel_log1 = {
    "France": {
        "num_times_visited": 0,
        "cities_visited": ["Paris", "Lille", "Dijon"]       
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stittgart"],
        "total_visits": 5
    }
}

print(travel_log1["Germany"]["cities_visited"][2])
