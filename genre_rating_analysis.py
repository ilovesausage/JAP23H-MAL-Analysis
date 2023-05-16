import pandas as pd
import time
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

st = time.time()

pd.options.display.max_rows = 10
df = pd.read_csv('animes.csv')

df = df.dropna()
df = df.reset_index(drop=True)
unique_genres = []

df.genre = df.genre.apply(literal_eval)
for i in range(len(df)):
    for a in range(len(df.genre[i])):
        if df.genre[i][a] not in unique_genres:
            unique_genres.append(df.genre[i][a])
            
unique_genres = unique_genres[:-5]

genre_with_num_list = []

for i in range(len(unique_genres)):
    genre_with_num = {
        "genre": unique_genres[i],
        "num": 0,
        "rating_avg": 0
    }
    genre_with_num_list.append(genre_with_num)

for i in range(len(df)):
    for a in range(len(df.genre[i])):
        for b in range(len(genre_with_num_list)):
            if df.genre[i][a] == genre_with_num_list[b]['genre']:
                genre_with_num_list[b]['num'] += 1
                genre_with_num_list[b]['rating_avg'] += df['score'][i].item()

for i in range(len(genre_with_num_list)):
    genre_with_num_list[i]['rating_avg'] = round(genre_with_num_list[i]['rating_avg']/genre_with_num_list[i]['num'], 2)

names = []
values = []

sorted_genres = sorted(genre_with_num_list, key=lambda i:i['rating_avg'], reverse=True)

for i in range(len(sorted_genres)):
    names.append(sorted_genres[i]['genre'])
    values.append(sorted_genres[i]['rating_avg'])

fig, ax = plt.subplots()
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
bars = plt.bar(range(len(sorted_genres)), values, tick_label=names)
ax.set_ylabel('Average Rating')
ax.set_xlabel('Genre')
ax.set_ylim([5.7, 7.5])
plt.yticks(np.arange(5.7, 7.5, 0.1))
ax.set_title('Average Genre Rating on MyAnimeList at May 2020')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 0.05, yval)
    
plt.show()
et = time.time()
print("execution time: " + str(et- st)) 
print(genre_with_num_list)