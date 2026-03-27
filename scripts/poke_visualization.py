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