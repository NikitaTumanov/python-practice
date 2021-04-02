import email.utils
import json
import urllib.request
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


"""
Как по времени суток распределяется активность студентов?
"""
with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

time = [datetime.datetime(1, 1, 1, messages[i][1][3], messages[i][1][4], messages[i][1][5]) for i in
        range(len(messages))]
count = list(range(24))
for i in range(len(time)):
    count[time[i].time().hour] += 1


x = [datetime.datetime(2021, 3, 21) + datetime.timedelta(hours=i) for i in range(24)]
y = count


plt.plot(x, y)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
