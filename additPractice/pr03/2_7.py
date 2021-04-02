import urllib.request
import re
import matplotlib.pyplot as plt


"""
Какие годы были самыми популярными с точки зрения выхода игр?
Какие жанры были популярны в различные периоды времени?
"""

url = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'
resp = urllib.request.urlopen(url)
respData = resp.read()
data_str = str(respData.decode())
data_str = re.split(';|\n', data_str)
dates = data_str[3::4]
genres = data_str[1::4]
set_dates = sorted(set(dates))
set_genres = sorted(set(genres))
dDates = dict.fromkeys(set_dates, 0)
dGenres = dict.fromkeys(set_genres, 0)
for i in range(len(dates)):
    dDates[dates[i]] += 1
for i in range(len(genres)):
    dGenres[genres[i]] += 1

fig, axs = plt.subplots(2, figsize=(25, 10))
axs[0].bar(set_dates, list(dDates.values()))
axs[1].bar(set_genres, list(dGenres.values()))
plt.show()
