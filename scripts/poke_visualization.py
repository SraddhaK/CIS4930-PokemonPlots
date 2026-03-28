import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

stats_by_gen = pd.read_csv("data/processed/pokemon_stats_by_gen.csv")
stats_by_gen["generation"] = range(1, 9) # 8 generations
poke_data = pd.read_csv("data/processed/pokemon_clean.csv")

# Line graph - Visualizing potential power creep(just using atk and speed stats since they're most relevant)
fig, ax = plt.subplots(figsize=(10, 6)) # about a couple inches larger than default figsize
stats = ["total_points", "attack", "sp_attack", "speed"]
for stat in stats:
    ax.plot(stats_by_gen["generation"], stats_by_gen[stat], marker="o", label=stat)
ax.set_title("Average Pokémon Stats by Generation")
ax.set_xlabel("Generation")
ax.set_ylabel("Mean Stat Value")
ax.legend(title="Stat")
fig.tight_layout() # auto adjust spacing inside figure: no cutoff
fig.savefig("figures/power_creep_by_generation.png", dpi=300)
plt.show()
# no obvious signs of power creep, minimal increase in total power after first few gens

# Bar plot - Greatest power type(fire, water, etc.) in terms of total points
type_data = poke_data[["type_1", "type_2", "total_points"]].copy() # doesnt affect original dataframe

# melt(pandas) merges type_1 and type_2 -> single column so both types are counted
# keeps total points, melts type_1 and type_2 and sets as type, drops variable(extra auto generated column -> type originally came from)
type_long = type_data.melt(id_vars="total_points", value_vars=["type_1", "type_2"], value_name="type").drop(columns="variable")

# clean data -> exclude second type if there is none(most pokemon have 2, but many have 1)
type_long = type_long[type_long["type"] != "None"]  # keeps only the rows where that condition is True

# take mean of total points per pokemon type
mean_power_by_type = type_long.groupby("type")["total_points"].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=mean_power_by_type, x="type", y="total_points", palette="rocket", hue="type", legend=False, ax=ax)
ax.set_title("Average Total Power by Pokémon Type")
ax.set_xlabel("Type")
ax.set_ylabel("Mean Total Points")
plt.xticks(rotation=45, ha="right")
fig.tight_layout()
fig.savefig("figures/power_by_type.png", dpi=300)
plt.show()
# Dragon is clearly strongest and bug is weakest in terms of power

# Histogram - Most common pokemon type
type_counts = type_long["type"].value_counts().reset_index() # counts number of unique types, reset index transforms back to column (pandas)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=type_counts, x="type", y="count", palette="mako", hue="type", legend=False, ax=ax)
ax.set_title("Most Frequent Pokémon Typings")
ax.set_xlabel("Type")
ax.set_ylabel("Number of Pokémon")
plt.xticks(rotation=45, ha="right")
fig.tight_layout()
fig.savefig("figures/type_frequency.png", dpi=300)
plt.show()
# Most frequent type: water
# Least frequent type: ice

# Scatter plot - Attack power comparison between most frequent type and other types
most_frequent = type_counts.iloc[0]["type"]  # grabs whichever type ranked #1 which is water (automatically sorted Descending)
poke_data["highlight"] = poke_data.apply( # new column "highlight": assignes all water types to most frequent, other to other
    lambda row: most_frequent if most_frequent in (row["type_1"], row["type_2"]) else "Other",
    axis=1
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=poke_data, x="attack", y="sp_attack", 
                hue="highlight", palette={"Other": "lightgray", most_frequent: "blue"},
                alpha=0.7, ax=ax)
ax.set_title(f"Water type Pokémon: Attack vs Sp. Attack Compared to Other Types")
ax.set_xlabel("Attack")
ax.set_ylabel("Special Attack")
ax.legend(title="Type")
fig.tight_layout()
fig.savefig("figures/type_stat_comparison.png", dpi=300)
plt.show()
# Seems to be fairly balanced, although there are many water types, they trend about average in terms of atk power
# Some are very strong but there are many other strong pokemon of other types