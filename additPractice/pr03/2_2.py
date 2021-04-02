import json
import urllib.request
import matplotlib.pyplot as plt


"""
Как по дням недели распределяется активность студентов?
"""
with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())

count = list(range(7))
for i in range(len(messages)):
    day = messages[i]['date'][:3]
    if day == 'Mon':
        count[0] += 1
    elif day == 'Tue':
        count[1] += 1
    elif day == 'Wed':
        count[2] += 1
    elif day == 'Thu':
        count[3] += 1
    elif day == 'Fri':
        count[4] += 1
    elif day == 'Sat':
        count[5] += 1
    elif day == 'Sun':
        count[6] += 1

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

x = days
y = count
plt.subplots()
plt.bar(x, y)
plt.show()
