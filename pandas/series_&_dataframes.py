# Pandas --> Panel Data

# Using this libraries we work with series and Dataframes 
#  Series Data -- means 1D labelled array that can hold any data type, Think of it like a single column in a spreadSheet (1-D)
# Dataframes -- means 2-D labelled grids(Tables)

import pandas as pd
import random
# print(pd.__version__)

# Series = A Pandas 1D labelled array that can hold any data type, Think of it like a single column in a spreadSheet (1-D)

data = [100, 109, 104.35]
# data = [True, False]
series = pd.Series(data, index=["a", "b", "c"])    # constructor --> .Series()
# series.loc["b"] = 200   # .loc is used to locating the value by lables (access and update the value)
print(series.iloc[1])   # integer-location based indexing for selection by position
print(series)
print(series.loc["a"])  # .loc is used to access the rows and columns from the series dataset

# Now, filtering the value

print(series[series > 100])

# Now, taking the dictionary examples
calories = {"Day 1": 1758, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
print()
print(series.loc["Day 2"])
series.loc["Day 3"] += 500
print(series)

# Now, filtering the value

print(series[series > 2000])

# Exercise 1

pokDict = {1: "Bulbasaur", 2: "Ivysaur", 3: "Venasaur", 4: "Charmander", 5: "Charmeleon", 6: "Charizard"}
series = pd.Series(pokDict)
print(series)

# DataFrame = A tabular data Structure with rows and columns. (2 Dimensional) Similar to an Excel Spreadsheet

data = {
    "Name": ["Ash", "Brock", "May"],
    "Age": [12, 19, 11]
}

df = pd.DataFrame(data, index=["Pokemon Trainer", "Pokemon Breeder", "Pokemon Trainer"])
print(df)
print(df.loc["Pokemon Breeder"])
rand = random.randint(0, len(df)-1)
print(df.iloc[rand])

# Add a new column
df["Gender"] = ["Male", "Male", "Female"]
print(df)

# Add a new rows
new_row = pd.DataFrame([{"Name": "Tracy", "Age": 20, "Gender": "Male"}, 
                       {"Name": "Pikachu", "Age": 3, "Gender": "Male"}], index=["Pokemon researcher", "Pokemon"])
df = pd.concat([df, new_row])
print(df)