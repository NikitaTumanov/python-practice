import os


# Написать утилиту командной строки, формирующую дерево каталогов и файлов с учетом вложенности и начиная с заданного
# пути. Результат должен быть выдан в виде текста в формате graphviz.

def result(s):
    if s == 'start':
        print('digraph G {')
    elif s == 'end':
        print('}')
    return s


def recursive_descent():
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for dirname in dirnames:
            print('  ' + os.path.basename(dirpath) + " -> " + dirname)
        for filename in filenames:
            print('  ' + os.path.basename(dirpath) + " -> " + f'"{filename}"')


def transformation():
    result('start')
    recursive_descent()
    result('end')


transformation()