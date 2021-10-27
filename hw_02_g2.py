import pandas as pd
import numpy as np

from matplotlib import colors, pyplot as plt


data = pd.read_csv('hw_02/valence_dance_energy.csv')
energy = data['energy']
dance = data['danceability']
valence = data['valence']

ax = plt.gca()

ax.scatter(energy, dance, color='b')
ax.scatter(energy, valence, color='r')


# plt.scatter(energy, bpm, cmap='Greens',
# edgecolors='black', linewidths=1, alpha=0.75)

plt.title('Energy of a song in relation to its Danceability and Valence')
ax.set_xlabel('Energy')
ax.set_ylabel('Valence and Danceability')
plt.legend(["Danceability", "Valence"], loc="upper left")

plt.tight_layout()

plt.show()
