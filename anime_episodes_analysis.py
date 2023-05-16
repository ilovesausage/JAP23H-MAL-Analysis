import pandas as pd
import time
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

st = time.time()

df = pd.read_csv('animes.csv')
df = df.dropna()
df = df[df['episodes'] != 1]
df = df.reset_index(drop=True)

episodes = []
for i in range(len(df)):
    episodes.append(df.episodes[i])


# used np.array_split(episodes, n), where n was the amount of different arrays to find these splits
episodes1 = []
episodes2 = []
episodes3 = []
episodes4 = []

for i in range(len(episodes)):
    if(episodes[i] <= 6):
        episodes1.append(episodes[i])
    elif(episodes[i] <= 12 and episodes[i] > 6):
        episodes2.append(episodes[i])
    elif(episodes[i] > 12 and episodes[i] < 26):
        episodes3.append(episodes[i])
    elif(episodes[i] >= 26):
        episodes4.append(episodes[i])

genre_with_num_list = []

for i in range(4):
    genre_with_num = {
        "episodes_arr": i,
        "num": 0,
        "rating_avg": 0
    }
    genre_with_num_list.append(genre_with_num)

for i in range(len(df)):
    if df.episodes[i] <= 6:
        genre_with_num_list[0]['num'] += 1
        genre_with_num_list[0]['rating_avg'] += df.score[i]
    elif df.episodes[i] <= 12 and df.episodes[i] > 6:
        genre_with_num_list[1]['num'] += 1
        genre_with_num_list[1]['rating_avg'] += df.score[i]
    elif df.episodes[i] > 12 and df.episodes[i] < 26:
        genre_with_num_list[2]['num'] += 1
        genre_with_num_list[2]['rating_avg'] += df.score[i]
    elif df.episodes[i] >= 26:
        genre_with_num_list[3]['num'] += 1
        genre_with_num_list[3]['rating_avg'] += df.score[i]
print(len(episodes1))
print(len(episodes2))

print(len(episodes3))


print(len(episodes4))


for i in range(len(genre_with_num_list)):
    genre_with_num_list[i]['rating_avg'] = round(genre_with_num_list[i]['rating_avg']/genre_with_num_list[i]['num'], 2)

names = []
values = []

sorted_genres = sorted(genre_with_num_list, key=lambda i:i['rating_avg'], reverse=True)

names.append("12 < episodes < 26")
names.append("6 < episodes <= 12")
names.append("episodes <= 26")
names.append("episodes <=6")

for i in range(len(sorted_genres)):
    values.append(sorted_genres[i]['rating_avg'])
    
fig, ax = plt.subplots()
# plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
ax.set_ylabel('Average Rating')
ax.set_title('Average Rating Based on Number of Episodes on MyAnimeList at May 2020')
ax.set_xlabel('Number of Episodes')
ax.set_ylim([6, 7.15])
plt.yticks(np.arange(6, 7.15, 0.1))

i = 0
bars = plt.bar(range(len(sorted_genres)), values, tick_label=names)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 0.02, "                        " + str(yval) + ", " + str(sorted_genres[i]['num']))
    i += 1

plt.show()

print(genre_with_num_list)
et = time.time() 
# print("execution time: " + str(et- st))  