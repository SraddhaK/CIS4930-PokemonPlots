"""
File name: poke_clean.py
Description: File used to clean pokemon.csv file so it can be utilized in future analysis.
Outputs cleaned_pokemon.csv
Author: Aiden Duncan
"""

# (Know i'm going to commit it but still felt like adding little doc string)

# Import necessary packages
import pandas as pd
import numpy as np

# Load data
poke_data = pd.read_csv("data/raw/pokemon.csv", index_col = 0)

# Handle missing values
poke_data.drop(columns=["base_experience", 
    "base_friendship", "egg_type_1", "egg_type_number", "egg_type_2", "egg_cycles", 
    "growth_rate", "percentage_male", "status", "against_normal", "against_fire",
    "against_fight", "against_dragon", "against_dark", "against_fairy", "against_ice", 
    "against_rock", "against_flying", "against_ground", "against_electric", "against_psychic",
    "against_ghost", "against_poison", "against_steel", "against_water", "against_grass", "against_bug", 
    "german_name", "japanese_name"], inplace = True) # Drop irrelevant information for study

# Fill in relevant missing values with constants
poke_data["type_2"].fillna("None", inplace = True)
poke_data["ability_2"].fillna("None", inplace = True)
poke_data["ability_hidden"].fillna("None", inplace = True)

# Fill in missing numeric values with mean
poke_data["hp"].fillna(poke_data["hp"].mean(), inplace = True)
poke_data["attack"].fillna(poke_data["attack"].mean(), inplace = True)
poke_data["defense"].fillna(poke_data["defense"].mean(), inplace = True)
poke_data["sp_attack"].fillna(poke_data["sp_attack"].mean(), inplace = True)
poke_data["sp_defense"].fillna(poke_data["sp_defense"].mean(), inplace = True)
poke_data["speed"].fillna(poke_data["speed"].mean(), inplace = True)
poke_data["weight_kg"].fillna(poke_data["weight_kg"].mean(), inplace = True)

# Convert to numeric to ensure numeric values for columns
poke_data["hp"] = pd.to_numeric(poke_data["hp"], errors= "coerce")
poke_data["attack"] = pd.to_numeric(poke_data["attack"], errors= "coerce")
poke_data["defense"] = pd.to_numeric(poke_data["defense"], errors= "coerce")
poke_data["sp_attack"] = pd.to_numeric(poke_data["sp_attack"], errors= "coerce")
poke_data["sp_defense"] = pd.to_numeric(poke_data["sp_defense"], errors= "coerce")
poke_data["speed"] = pd.to_numeric(poke_data["speed"], errors= "coerce")
poke_data["weight_kg"] = pd.to_numeric(poke_data["weight_kg"], errors= "coerce")
poke_data["catch_rate"] = pd.to_numeric(poke_data["catch_rate"], errors= "coerce")

# No date column in this dataset — create a synthetic one to satisfy the requirement
gen_year_map = {1: "1996", 2: "1999", 3: "2002", 4: "2006",
                5: "2010", 6: "2013", 7: "2016", 8: "2019"}
poke_data["release_date"] = poke_data["generation"].map(gen_year_map)
poke_data["release_date"] = pd.to_datetime(poke_data["release_date"], format="%Y")

# Create some additional columns using np.where and np.apply
poke_data["speed_class"] = np.where(poke_data["speed"] >= poke_data["speed"].mean(), "Fast", "Slow")

avg_total_stats = poke_data["total_points"].mean()

def strength_class(row, avg_stats):
    if row["total_points"] >= avg_stats:
        return "Strong"
    else: return "weak"

poke_data["strength_category"] = poke_data.apply(strength_class, axis = 1, avg_stats = avg_total_stats)

# Aggregations
# Multi-column aggregation (mean AND count)
grouped = poke_data.groupby(["pokedex_number", "generation"])["total_points"].agg(["mean", "count"])
# print(grouped.head(10))

# Single grouped stat for EDA use
stats_by_gen = poke_data.groupby("generation")[["total_points", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]].mean()
# print(stats_by_gen.head(10))

# Pivot table
pivot = poke_data.pivot_table(
    index="pokedex_number",
    columns="generation",
    values="total_points",
    aggfunc="mean"
)
# print(pivot)

# Export cleaned data and reorganized data as helpful point sof reference for analysis
poke_data.to_csv("data/processed/pokemon_clean.csv", index=False)
stats_by_gen.to_csv("data/processed/pokemon_stats_by_gen.csv", index=False)