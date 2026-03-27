
#sraddha's code (i'm gonna commit it, but still)


#imports
import pandas as pd
import numpy as np


#read in data
df = pd.read_csv("data/pokemon.csv")


#.loc (fire(
fire_pokemon = df.loc[df["type_1"] == "Fire"]

#.iloc (first 5 rows)
print("\nFirst 5 rows of the dataset:\n", df.head())
subset_iloc = df.iloc[0:5, 0:5]

#boolean (high attack)
high_attack = df[df["attack"] > 100]

print("\nFire-type Pokémon:\n", fire_pokemon[["name", "type_1", "attack"]].head())
print("\nHigh attack Pokémon:\n", high_attack[["name", "attack"]].head())



#new column: strong v weak
df["strength_category"] = np.where(df["total_points"] > 500, "Strong", "Weak")

#apply() for speed
def speed_category(speed):
    if speed > 100:
        return "Fast"
    else:
        return "Slow"

df["speed_category"] = df["speed"].apply(speed_category)

print("\nNew columns:\n", df[["name", "total_points", "strength_category", "speed", "speed_category"]].head())
