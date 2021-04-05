import random


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
    return [i for i in range(0, len(s)) if s[i] == x]


def sum_chet_index(s):
    print("Task 5:")
    return sum([s[i] for i in range(0, len(s)) if i % 2 == 0])


def max_len_str(s):
    print("Task 6:")
    return max(j for j in s if len(j) == max(len(i) for i in s))


def groups():
    print("Генерация групп:")
    letters = ['K', 'В', 'Н']
    maxCount = [25, 13, 10]
    return [letters[i] + str(j + 1) for i in range(len(letters)) for j in range(maxCount[i])]


def report():
    part_1 = ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,',
               'Вместе с тем,',
               'С другой стороны,']
    part_2 = ['парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов',
               'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий',
               'программа прорывных исслeдований',
               'ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data']
    part_3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
               "расширяет горизонты", "заставляет искать варианты",
               "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
    part_4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
               "компрометации конфиденциальных", "универсальной коммодитизации",
               "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
    part_5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
               "опасных экспериментов.", "государственно-частных партнёрств.",
               "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    return print(random.choice(part_1) + " " + random.choice(part_2) + " " + random.choice(part_3) + " " + random.choice(
        part_4) + " " + random.choice(part_5))


names = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Илья', 'Кирилл', 'Михаил', 'Никита',
         'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Тимофей', 'Владислав', 'Игорь',
         'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур', 'Олег', 'Ярослав', 'Антон', 'Николай']
ignore = ['Ю', 'Ь', 'Ъ', 'Й', 'Ё', 'Ы']
alphabet = [chr(x) for x in range(ord('А'), ord('Я') + 1) if chr(x) not in ignore]
end_of_lastname = ['ов', 'ев', 'ин', 'ын', 'ский', 'цкий', 'ской', 'цкой', 'ой', 'ий', 'енков', 'их', 'ых', 'ко']
consonant_letters = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
vowel_letters = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'е']


def surname():
    s = random.choice(names) + " " + random.choice(alphabet) + ". "
    for i in range(random.randint(1, 3)):
        if i == 0:
            s += random.choice(consonant_letters).upper()
        else:
            s += random.choice(consonant_letters)
        s += random.choice(vowel_letters)
    s = s + random.choice(consonant_letters) + random.choice(end_of_lastname)
    return print(s)


print("Часть 1:")
print(string_to_int(['1', '2', '3', '4', '5']))
print(count_of_dif_el(['1', '2', '3', '1', '4', '5', '3']))
print(reverse(['1', '2', '3', '4', '5']))
print(index_list(['1', '2', '3', '1', '4', '5', '3'], '1'))
print(sum_chet_index([1, 2, 3, 4, 5]))
print(max_len_str(["short", "very long", "really long", "the longest"]))
print(groups())
print("Генерация доклада:")
[report() for i in range(3)]
print("Генерация фамилий:")
[surname() for i in range(5)]
