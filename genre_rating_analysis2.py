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
unique_num = []

df.genre = df.genre.apply(literal_eval)
for i in range(len(df)):
    if len(df.genre[i]) not in unique_num:
        unique_num.append(len(df.genre[i]))

genre_with_num_list = []

for i in range(len(unique_num)):
    genre_with_num = {
        "number of genres": unique_num[i],
        "num": 0,
        "rating_avg": 0
    }
    genre_with_num_list.append(genre_with_num)

for i in range(len(df)):
    for a in range(len(genre_with_num_list)):
        if len(df.genre[i]) == genre_with_num_list[a]['number of genres']:
            genre_with_num_list[a]['num'] += 1
            genre_with_num_list[a]['rating_avg'] += df['score'][i].item()

for i in range(len(genre_with_num_list)):
    genre_with_num_list[i]['rating_avg'] = round(genre_with_num_list[i]['rating_avg']/genre_with_num_list[i]['num'], 2)

names = []
values = []

sorted_genres = sorted(genre_with_num_list, key=lambda i:i['rating_avg'], reverse=True)

for i in range(len(sorted_genres)):
    names.append(sorted_genres[i]['number of genres'])
    values.append(sorted_genres[i]['rating_avg'])

fig, ax = plt.subplots()
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
bars = plt.bar(range(len(sorted_genres)), values, tick_label=names)
ax.set_ylabel('Average Rating')
ax.set_xlabel('Number of Genres')
ax.set_ylim([5.5, 8.0])
plt.yticks(np.arange(5.5, 8.0, 0.1)) 
ax.set_title('Average Genre Rating Based on Number of Genres on MyAnimeList at May 2020')
i = 0
for bar in bars:
    yval = bar.get_height()
    text = "  " + str(yval)
    text += ", " + str(sorted_genres[i]['num'])
    plt.text(bar.get_x(), yval + 0.05, text)
    i += 1
    
plt.show()
et = time.time()
print("execution time: " + str(et- st)) 
