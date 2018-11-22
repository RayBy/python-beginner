# coding UTF-8
__author__ = 'Ильиных Павел Сергеевич'

import sys
import sqlite3
import os
import csv
import json
import copy


def export():
    try:
        exp_format = sys.argv[1]
    except IndexError:
        print('Ошибка! Необходимо запустить скрипт с одним из параметров: --csv, --html, --json')
        exit()
    exp_formats_lst = ['--csv', '--json', '--html']
    if exp_format not in exp_formats_lst:
        print('Ошибка! Необходимо запустить скрипт с одним из параметров: --csv, --html, --json')
        exit()

    if len(sys.argv) > 2:
        city_name = sys.argv[2]
        file_name = '{}.txt'.format(city_name)
        sql_condition = 'WHERE city = "{}"'.format(city_name)
    else:
        file_name = 'weather.{}'.format(exp_format[2:])
        sql_condition = ''
    db_name = 'openweather.db'  # Определяем имя файла БД

    if os.path.exists(db_name):  # Делаем запрос в БД
        weather_db = sqlite3.connect(db_name)
        cursor = weather_db.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM weather
            {}
            '''.format(sql_condition)
        )
        weather_data = cursor.fetchall()

        if not weather_data:  # Проверяем наличие города в БД по введенным данным
            print('Вы ввели "{}" данных по этому городу в базе нет! Проверьте правильность ввода или загрузите данные с сервера.'
                  .format(city_name))
            exit()
        col_names = [col[0] for col in cursor.description]

        if exp_format == '--csv':  # экспортируем файл в нужный нам формат
            with open(file_name, 'w', encoding='UTF-8') as file:
                file.write(', '.join(col_names))
                file.write('\n')
                for row in weather_data:
                    file.write(str(row)[1:-1])
                    file.write('\n')
        elif exp_format == '--html':
            pass
        elif exp_format == '--json':
            pass
    else:
        print('Файл БД не найден, пожалуйста запустите сначала скрипт openweather.py')
        exit()


if __name__ == '__main__':
    export()
