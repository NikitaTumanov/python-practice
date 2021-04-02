import email.utils
import json
import urllib.request
import matplotlib.pyplot as plt

"""
В каких группах было отправлено больше всего сообщений?
"""


def generate_groups():
    letter = ['К', 'В', 'М', 'Н']
    maxCount = [25, 13, 2, 10]
    result = []
    for i in range(len(letter)):
        for j in range(maxCount[i]):
            result.append(letter[i] + str(j + 1))
    return result


with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

# messages[var][0].split()[0] - группа
d = dict.fromkeys(generate_groups(), 0)
for i in range(len(messages)):
    key = messages[i][0].split()[0].upper()
    d[key] += 1

x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20, 10))
plt.bar(x, y)
plt.show()
