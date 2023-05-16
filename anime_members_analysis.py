import pandas as pd
import time
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

st = time.time()

df = pd.read_csv('animes.csv')
df = df.dropna()
df = df.reset_index(drop=True)

members = []
for i in range(len(df)):
    members.append(df.members[i])

members.sort()

members1 = []
members2 = []
members3 = []
members4 = []

# used np.array_split(members, n), where n was the amount of different arrays to find these splits
for i in range(len(members)):
    if members[i] <= 334:
        members1.append(members[i])
    elif members[i] > 334 and members[i] <= 2427:
        members2.append(members[i])
    elif members[i] > 2427 and members[i] <= 23176:
        members3.append(members[i])
    elif members[i] > 23176:
        members4.append(members[i])

genre_with_num_list = []

for i in range(4):
    genre_with_num = {
        "members_arr": i,
        "num": 0,
        "rating_avg": 0
    }
    genre_with_num_list.append(genre_with_num)

for i in range(len(df)):
    if df.members[i] <= 334:
        genre_with_num_list[0]['num'] += 1
        genre_with_num_list[0]['rating_avg'] += df.score[i]
    elif df.members[i] > 334 and df.members[i] <= 2427:
        genre_with_num_list[1]['num'] += 1
        genre_with_num_list[1]['rating_avg'] += df.score[i]
    elif df.members[i] > 2427 and df.members[i] <= 23176:
        genre_with_num_list[2]['num'] += 1
        genre_with_num_list[2]['rating_avg'] += df.score[i]
    elif df.members[i] > 23176:
        genre_with_num_list[3]['num'] += 1
        genre_with_num_list[3]['rating_avg'] += df.score[i]

for i in range(len(genre_with_num_list)):
    genre_with_num_list[i]['rating_avg'] = round(genre_with_num_list[i]['rating_avg']/genre_with_num_list[i]['num'], 2)

names = []
values = []

sorted_genres = sorted(genre_with_num_list, key=lambda i:i['rating_avg'], reverse=True)


names.append("members > 23176")
names.append("2427 < members <= 23176")
names.append("334 < members <= 2427")
names.append("members <= 334")


for i in range(len(sorted_genres)):
    values.append(sorted_genres[i]['rating_avg'])
    
fig, ax = plt.subplots()
# plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
ax.set_ylabel('Average Rating')
ax.set_title('Average Rating Based on Number of Members on MyAnimeList at May 2020')
ax.set_xlabel('Number of Members')
ax.set_ylim([5, 8])
plt.yticks(np.arange(5, 8, 0.1))

bars = plt.bar(range(len(sorted_genres)), values, tick_label=names)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 0.02, "                    " + str(yval) + ", " + str(sorted_genres[i]['num']))

plt.show()

et = time.time()
print("execution time: " + str(et- st)) 