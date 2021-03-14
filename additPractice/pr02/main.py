import random
import pyfiglet

def string_to_int(s):
    print("Task 1:")
    return [int(x) for x in s]

def count_of_dif_el(s):
    print("Task 2:")
    return len(set(s))

def reverse(s):
    print("Task 3:")
    return s[::-1]

def index_list(s, x):
    print("Task 4:")
    return [i for i in range(0,len(s)) if s[i]==x]

def sum_chet_index(s):
    print("Task 5:")
    return sum([s[i] for i in range(0,len(s)) if i%2==0 ])

def max_len_str(s):
    print("Task 6:")
    return max(j for j in s if len(j)==max(len(i) for i in s))

def doklad():
    print("Генерация доклада:")
    chast_1=['Коллеги,','В то же время,','Однако,','Тем не менее,','Следовательно,','Соответственно,','Вместе с тем,',
    'С другой стороны,']
    chast_2 = ['парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов',
    'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий', 'программа прорывных исслeдований',
    'ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data']
    chast_3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
    "расширяет горизонты", "заставляет искать варианты",
    "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
    chast_4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
    "компрометации конфиденциальных", "универсальной коммодитизации",
    "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
    chast_5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
    "опасных экспериментов.", "государственно-частных партнёрств.",
    "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    return random.choice(chast_1)+" "+random.choice(chast_2)+" "+random.choice(chast_3)+" "+random.choice(chast_4)+" "+random.choice(chast_5)

def ascii_banner(s):
    return pyfiglet.figlet_format(s)

print("Часть 1:")
print(string_to_int(['1', '2', '3', '4', '5']))
print(count_of_dif_el(['1', '2', '3', '1', '4', '5', '3']))
print(reverse(['1', '2', '3', '4', '5']))
print(index_list(['1', '2', '3', '1', '4', '5', '3'], '1'))
print(sum_chet_index([1, 2, 3, 4, 5]))
print(max_len_str(["short", "very long", "really long", "the longest"]))
print(doklad())
print("Часть 2:")
print(ascii_banner('KisPython'))