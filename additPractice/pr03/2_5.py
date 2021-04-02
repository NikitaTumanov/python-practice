import email.utils
import json
import urllib.request
import matplotlib.pyplot as plt

"""
Какие задачи оказались самыми легкими, самыми сложными?
"""


def generate_tasks():
    letter = 'f'
    maxCount = [4, 3, 2]
    result = []
    for i in range(len(maxCount)):
        for j in range(maxCount[i]):
            result.append(letter + str(i + 1) + str(j + 1))
    return result


def diff(ones, zeros):
    result = []
    for i in range(len(ones)):
        result.append(ones[i] - zeros[i])
    return result


with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/table.json') as url:
    table = json.loads(url.read().decode())
with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

dZero = dict.fromkeys(generate_tasks(), 0)
dOne = dict.fromkeys(generate_tasks(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    key = table['data'][i][2]
    if score == 0:
        dZero[key] += 1
    else:
        dOne[key] += 1
x = generate_tasks()
y = diff(list(dOne.values()), list(dZero.values()))
plt.subplots()
plt.title('Разность между кол-вом 1 и 0')
plt.bar(x, y)
plt.show()
