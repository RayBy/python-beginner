# coding UTF-8
__author__ = 'Ильиных Павел Сергеевич'


import os
import gzip
import json
import urllib.request
import sqlite3
from datetime import date


def main():
    cities_ch()
    database_ch()
    print("Приветствую Вас! Эта программа позволит Вам узнать погоду в любом точке Земли!")
    print("Доступный список команд представлен в списке ниже.")
    while True:
        print('''
        
                            Доступные команды:
                            
    [1] Погода сегодня в выбранном городе
    [2] Погода сегодня в городах выбранной Вами страны
    [3] Вывести доступный список стран
    [4] Вывести список городов по определенной стране'''
        )
        act = input('Введите номер действия или нажмите q для выхода из программы: ')
        if act == '1':
            get_weather('city')
            if ct():
                continue
            else:
                break
        elif act == '2':
            get_weather('country')
            if ct():
                continue
            else:
                break
        if act == '3':
            countries_list()
            if ct():
                continue
            else:
                break
        elif act == '4':
            county_cities()
            if ct():
                continue
            else:
                break
        elif act == 'q':
            break
        else:
            act = input('Вы ввели неизвестное значение, попробуйте снова: ')
    print('Работа программы завершена')


def ct():
    print('_ '*29)
    ct = input('Для выхода введите нажмите клавишу q, Для продолжения работы нажмите клавишу Enter: ')
    if ct == 'q':
        return False
    else:
        print()
        return True


def database_ch():  # Определяем наличие файла БД, при необходимости создаем
    db_name = 'openweather.db'
    weather_db = sqlite3.connect(db_name)
    cursor = weather_db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS weather (
        city_id INT,
        city VARCHAR(255),
        date TEXT,
        temperature INT,
        weather_id INT
        )
        '''
    )
    weather_db.commit()
    weather_db.close()


def cities_ch():  # Проверяем наличие файла списка городов, при необходимости скачиваем и распаковываем
    if not os.path.exists('./city.list.json'):
        city_url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        city_file_compressed = urllib.request.urlretrieve(city_url, './city.list.json.gz')[0]
        city_file = './city.list.json'

        with gzip.open(city_file_compressed, 'rt', encoding='UTF-8') as comp, \
                open(city_file, 'wt', encoding='UTF-8') as decomp:
            decomp.write(comp.read())


def countries_list():  # список стран
    with open('./city.list.json', 'rt', encoding='UTF-8') as f:
        cities_data = tuple(json.load(f))
    countries_list = sorted(set(city["country"] for city in cities_data))
    print(countries_list)
    return countries_list


def county_cities():  # список городов по стране
    with open('./city.list.json', 'rt', encoding='UTF-8') as f:
        cities_data = tuple(json.load(f))
    country_name_user = input('\nВведите название страны 2 символа: ').upper()
    while True:
        if country_name_user in countries_list():
            city_name = sorted(city['name'] for city in cities_data if city['country'] == country_name_user)
            for i in city_name:
                print(i)
            break
        elif country_name_user == 'q':
            break
        else:
            country_name_user = input('\nВведенная страна не найдена. Попробуйте еще раз '
                                      'Для выхода нажмите кнопку q: ').upper()


def get_weather(mode):  # получаем погоду по городу или по городам выбранной страны
    with open('./city.list.json', 'rt', encoding='UTF-8') as f:
        cities_data = tuple(json.load(f))
    if mode == 'city':
        city_name_user = input('\nВведите название города или часть названия на английском: ').lower()
        cities_tech = []
        for city in cities_data:
            if city_name_user in city['name'].lower():
                cities_tech.append(city)
        if len(cities_tech) > 1:
            for i in cities_tech:
                print(i)
            city_id_user = input("По Вашему запросу обнаружено {} результатов. Введите id нужного города из списка : ".format(len(cities_tech)))
            for i in cities_tech:
                if str(i['id']) == city_id_user:
                    city_id = (i['id'], )
                    break
        else:
            city_id = (cities_tech[0]['id'], )
    if mode == 'country':
        country_name_user = input('\nВведите название страны 2 буквы: ').upper()
        country_list = frozenset(city["country"] for city in cities_data)
        while True:
            if country_name_user in country_list:
                city_id = (city['id'] for city in cities_data if city['country'] == country_name_user)
                break
            elif country_name_user == 'q':
                break
            else:
                country_name_user = input('\nВведенное значение не найдено, проверьте правильность ввода '
                                          'или нажмите клавишу q для выхода: ').upper()
    get_weather_city(city_id)


def get_weather_city(cities_id):  # Запрашиваем погоду по запросу с сайта при помощи APIID
    api_key = './app.id'
    with open(api_key, 'rt', encoding='UTF-8') as file:
        api_key = json.load(file)[0]['api_key']
    root_url = 'http://api.openweathermap.org/data/2.5/weather?id='
    cities_id = map(str, cities_id)

    for city_id in cities_id:
        full_url = '{root}{id}&units=metric&appid={api_key}'.format(root=root_url,
                                                                    id=city_id, api_key=api_key)
        with urllib.request.urlopen(full_url) as url:
            weather_data_full = json.loads(url.read())

        weather_data = {
            'city_id': weather_data_full['id'],
            'city': weather_data_full['name'],
            'date': str(date.fromtimestamp(weather_data_full['dt']).strftime('%Y.%m.%d')),
            'temp': weather_data_full['main']['temp'],
            'weather_id': weather_data_full['weather'][0]['id']
        }
        print(weather_data)
        update_weather(weather_data)


def update_weather(weather_data):
    db_name = 'openweather.db'
    weather_db = sqlite3.connect(db_name)
    cursor = weather_db.cursor()
    cursor.execute(
        '''
        SELECT COUNT(*)
        FROM weather
        WHERE city_id = {city_id}
        AND date = '{date}'
        '''.format(city_id=weather_data['city_id'], date=weather_data['date'])
    )
    check = cursor.fetchone()

    if not check[0]:  # Проверяем наличие записи по городу в БД,  в случае необходимости обновляем либо добавляем
        cursor.execute(
            '''
            INSERT INTO weather VALUES
            ({city_id}, '{city}', '{date}', {temp},{weather_id})
            '''.format(city_id=weather_data['city_id'], city=weather_data['city'],
                       date=weather_data['date'], temp=weather_data['temp'], weather_id=weather_data['weather_id'])
        )
    else:
        cursor.execute(
            '''
            UPDATE weather  
            SET temperature = {temp},
                weather_id = {weather_id}
            WHERE city_id = {city_id}
            AND date = '{date}'
            '''.format(city_id=weather_data['city_id'], date=weather_data['date'],
                       temp=weather_data['temp'], weather_id=weather_data['weather_id'])
        )
    weather_db.commit()
    weather_db.close()


if __name__ == '__main__':
    main()
