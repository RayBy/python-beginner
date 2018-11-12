__author__ = 'Ильиных Павел Сергеевич'

# coding UTF-8

import os
import shutil

# Дополнительные функции для задания normal
# Переход в указанную папку
def perehod():
    p = input('Введите путь к папке и нажмите Enter... ')
    os.chdir(p)
    p_2 = os.getcwd()
    if p_2 == p:
        print('Вы успешно перешли в указанную папку')
    else:
        print('Не удалось перейти в указанную папку')

# Создание файла с указанным именем
def sozdanie():
    f = input('Введите название папки и нажмите Enter... ')
    os.mkdir(f)
    if os.path.exists(f):
        print('Папка создана успешно.')
    else:
        print('Не удалось создать папку')

# Удаление файла с указанным именем
def udalenie():
    df = input('Введите название папки которую хотите удалить и нажмите Enter... ')
    os.rmdir(df)
    if not os.path.exists(df):
        print('Папка успешно удалена')
    else:
        print('Не удалось удалить папку')

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создание папок dir_ c 1 по 9
def create_dir():
    i = 1
    while i <= 9:
        d = 'dir_' + str(i)
        os.mkdir(d)
        i += 1

create_dir()

# Удаление папок из текущей диретории имя которых начинается с dir_
def del_dir():
    file_list = os.listdir()
    i_2 = 0
    while i_2 < len(file_list):
        name = os.path.join(file_list[i_2])
        if name.startswith('dir_'):
            os.rmdir(name)
        i_2 += 1

del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def file_list():
    print(os.listdir())

file_list()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    new_file = __file__ + '.copy'
    shutil.copy(__file__, new_file)

copy_file()