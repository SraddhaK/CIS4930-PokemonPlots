import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def print_column_description(data, column, message):
    print(f"{message}\n{data[column].describe()}\n")

poke_data = pd.read_csv("data/processed/pokemon_clean.csv")
most_common_generation = poke_data["generation"].mode()

print_column_description(poke_data, "total_points", "Description for total points:")
print("Each Pokemon has a specific amount of total stat points and a type that determines its strength in battle. How does each pokemon type compare to the average total points? Looking at the power_by_type plot, we can see that water, poison, grass, and bug types are under the average. On the other side, dragon is significantly higher than the average.")
print_column_description(poke_data, "height_m", "Description for height in meters:")
print_column_description(poke_data, "weight_kg", "Description for weight in kg:")

print(f"The most generations that introduced the most Pokemon:\n{most_common_generation}\n")

print_column_description(poke_data, "type_1", "Description for type 1:")
print_column_description(poke_data, "type_2", "Description for type 2:")
print("Each Pokemon can have two types, type 1 being the main type and type 2 being a subtype most of the time.\nWater is the most common type as seen in the type_frequency plot and is also the most common type in the first type slot. However, the most common type being flying for the second type slot is not the least common type (ice)")

print("The main question we were asking withh this analysis is: Is there power creep (i.e. an increase in Pokemon power as time progresses) in Pokemon?\nBased on our current plots about power creep, there seems to be no indication that power creep is occurring based off of new Pokemon's stats. This does not rule out power creep in modern day Pokemon, however, as different factors such as: what moves a Pokemon can learn, what the Pokemon's ability does, or what combination of types does the Pokemon have can determine its power in battle.")

poke_data_subset = poke_data[["total_points", "height_m", "weight_kg", "hp", "speed", "attack", "defense", "sp_attack", "sp_defense"]]
corr_matrix = poke_data_subset.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation heatmap for various stats")
plt.tight_layout()
plt.xticks(rotation=45, ha="right")
plt.show()