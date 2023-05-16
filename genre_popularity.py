import pandas as pd
import time
from ast import literal_eval
import matplotlib.pyplot as plt

st = time.time()

pd.options.display.max_rows = 10
df = pd.read_csv('animes.csv')

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
        "num": 0
    }
    genre_with_num_list.append(genre_with_num)

for i in range(len(df)):
    for a in range(len(df.genre[i])):
        for b in range(len(genre_with_num_list)):
            if df.genre[i][a] == genre_with_num_list[b]['genre']:
                genre_with_num_list[b]['num'] += 1

names = []
values = []

sorted_genres = sorted(genre_with_num_list, key=lambda i:i['num'], reverse=True)

for i in range(len(sorted_genres)):
    names.append(sorted_genres[i]['genre'])
    values.append(sorted_genres[i]['num'])
    
fig, ax = plt.subplots()
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
ax.set_ylabel('Number of Anime With Genre')
ax.set_title('Anime Genre Popularity on MyAnimeList at May 2020')
ax.set_xlabel('Genre')
plt.bar(range(len(sorted_genres)), values, tick_label=names)
plt.show()
et = time.time()
print("execution time: " + str(et- st)) 