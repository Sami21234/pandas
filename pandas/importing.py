import pandas as pd

# importing the csv and json file
df = pd.read_csv("pokemon.csv", index_col="Name")
# print(df.to_string())

# selction

df = pd.read_csv("pokemon.csv", index_col="Name")
# print(df)

# Selction by Columns

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df[["Name", "Height", "Type1", "Legendary"]].to_string())

# Selection by Rows
# print(df)
# print(df.loc["Pikachu":"Mewtwo", ["Height", "Weight"]])
# print(df.iloc[0:120:2, 0:5]) #(rows, columns)

# pokemon = input("Enter the pokemon name: ")

# try:
#     print(df.loc[pokemon])

# except KeyError:
#     print(f"{pokemon} not found")

# Filtering
# It is the process to keep the rows that matches the condition

df = pd.read_csv("pokemon.csv")

# Now filtering those pokemons which have the weight in kgs above the 20
weighted_Pokemon = df[df["Weight"] > 80]
# print(weighted_Pokemon.to_string())

# Now filtering the pokemon which are legendary pokemon
legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)

# Now filtering those pokemons which are water type
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# print(water_pokemon)

# Now filtering those which are of type fire and fly
fire_fly_type = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# print(fire_fly_type)

# Aggregate Function
# Reduces a set of values into a single summary values used to summarize and analyze data, Often used with the groupBy() function

df = pd.read_csv("pokemon.csv")

# whole Dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].max())
# print(df["Height"].count())

# groupBy() function
groupBy = df.groupby("Type1")
# print(groupBy["Height"].mean())
# print(groupBy["Height"].sum())
# print(groupBy["Height"].min())
# print(groupBy["Height"].max())
# print(groupBy["Height"].count())

# Data Cleaning = The process of fixing/removing: incomplete, incorrect, or irrelevant data. 
# 75% of work done with pandas is data cleaning

df = pd.read_csv("pokemon.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])
# print(df)

# 2. Handle missing data

# df = df.dropna(subset=["Type2"])  # dropna() = If any row has a value NaN (than) it will remove that row (dropna) --> not available

# df = df.fillna({"Type2": "None"})   # fillna() = It is used to change the value of (NaN) to any default value like not available 
# print(df.to_string())

# 3. Fix inconsistent values

df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
# print(df.to_string())

# 4. standardize the text
df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. Fix the data types
df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string())

# 6. Remove duplicate values
df = df.drop_duplicates()
print(df.to_string())