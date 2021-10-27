import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
csv.field_size_limit(sys.maxsize)

with open('hw_02/spotify_data1.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    genre_counter = Counter()
    pop = 0
    rock = 0
    funk = 0
    disco = 0
    rap = 0
    soul = 0
    classical = 0
    brass = 0
    indie = 0
    for row in csv_reader:
        if 'pop' in row['genre']:
            pop += 1
        if 'funk' in row['genre']:
            funk += 1
        if 'disco' in row['genre']:
            disco += 1
        if 'rap' in row['genre']:
            rap += 1
        if 'soul' in row['genre']:
            soul += 1
        if 'classical' in row['genre']:
            classical += 1
        if 'brass' in row['genre']:
            brass += 1
        if 'indie' in row['genre']:
            indie += 1
        if 'rock' in row['genre']:
            rock += 1
        # if 'rock' in row['genre']:
           # rock += 1

counts = {
    'pop': pop, 'funk': funk, 'disco': disco, 'rap': rap, 'soul': soul, 'classical': classical, 'brass': brass, 'indie': indie, 'rock': rock
}

print('counts=', counts)

xs = sorted(counts.keys())
ys = [counts[key] for key in xs]

fig, ax = plt.subplots()
ax.bar(xs, ys)
ax.set_xlabel('Genre')
ax.set_ylabel('Frequency')
ax.set_title(
    'How many times does a specific genre appear in my Spotify library')
plt.show()
