import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def print_column_description(data, column, message):
    print(f"{message}\n{data[column].describe()}\n")

poke_data = pd.read_csv("data/processed/pokemon_clean.csv")

print_column_description(poke_data, "total_stat", "Description for total stats:")
print_column_description(poke_data, "height_m", "Description for height in meters:")
print_column_description(poke_data, "weight_kg", "Description for weight in kg")
print_column_description(poke_data, "generation", "Description for generation, able to determine which generation released the most amount of pokemon:")
print_column_description(poke_data, "type_1", "Description for type 1, able to determine most common type in the first type slot")
print_column_description(poke_data, "type_2", "Description for type 2, able to determine most common type in the first type slot")


poke_data_subset = poke_data[["total_stat", "height_m", "weight_kg", "hp", "speed", "attack", "defense", "sp_attack", "sp_defense"]]
corr_matrix = poke_data_subset.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation heatmap for various stats")
plt.show()