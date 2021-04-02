import json
import urllib.request
import matplotlib.pyplot as plt

"""
В каких группах было получено больше всего правильных решений?
"""


def generate_groups():
    letter = ['К', 'В', 'М', 'Н']
    maxCount = [25, 13, 2, 10]
    result = []
    for i in range(len(letter)):
        for j in range(maxCount[i]):
            result.append(letter[i] + str(j + 1))
    return result


with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/table.json') as url:
    table = json.loads(url.read().decode())

print(table['data'][0][3])
# table['data'][var][0] - группа
# table['data'][var][3] - оценка


d = dict.fromkeys(generate_groups(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    if score == 1:
        key = table['data'][i][0]
        d[key] += 1
x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20, 10))
plt.bar(x, y)
plt.show()
