import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from matplotlib.lines import lineStyles

sns.set_theme(style="whitegrid")

stats_by_gen = pd.read_csv("data/processed/pokemon_stats_by_gen.csv")
stats_by_gen["generation"] = range(1, 9) # 8 generations
poke_data = pd.read_csv("data/processed/pokemon_clean.csv")

# For visualizing potential power creep(just using atk and speed stats since they're most relevant)
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

# Greatest power type(fire, water, etc.) in terms of total points (bar plot)
type_data = poke_data[["type_1", "type_2", "total_points"]].copy() # doesnt affect original dataframe

# melt(pandas) merges type_1 and type_2 -> single column so both types are counted
# keeps total points, melts type_1 and type_2 and sets as type, drops variable(extra auto generated column -> type originally came from)
type_long = type_data.melt(id_vars="total_points", value_vars=["type_1", "type_2"], value_name="type").drop(columns="variable")

# clean data -> exclude second type if there is none(most pokemon have 2, but many have 1)
type_long = type_long[type_long["type"] != "None"]  # keeps only the rows where that condition is True

# take mean of total points per pokemon type
mean_power_by_type = type_long.groupby("type")["total_points"].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=mean_power_by_type, x="type", y="total_points", palette="rocket", ax=ax)

ax.set_title("Average Total Power by Pokémon Type")
ax.set_xlabel("Type")
ax.set_ylabel("Mean Total Points")
plt.xticks(rotation=45, ha="right")
fig.tight_layout()
fig.savefig("figures/power_by_type.png", dpi=300)
plt.show()