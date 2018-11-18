__author__ = 'Ильиных Павел Сергеевич'

# coding UTF-8


import random


class Lotto:

    def __init__(self, name):
        kit = [x for x in range(1, 91)]  # создаем набор бочонков от 1 до 90.
        self.blank = [__class__.gen_string(kit), __class__.gen_string(kit), __class__.gen_string(kit)]
        self.name = name
        self.count_lotto_keg = 15  # определяем начальное количество чисел на карточке

    @staticmethod
    def gen_string(kit):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            position = random.randint(0, x)  # Определяем номер позиции которое заполняется
            while string[position] != '':  # Определяем что делать если на этой позиции уже есть элемент
                position += 1
            string[position] = kit.pop(random.randint(0, len(kit) - 1))
        return string

    def __str__(self):  # Рисуем карточку
        res = '{:-^26}\n'.format(self.name)
        for x in range(3):
            res += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} '\
                .format(*self.blank[x]) + '\n'
        return res + '-------------------------- \n'


computer = Lotto('Карточка компьютера')
player = Lotto('Карточка игрока')

pul = [x for x in range(1, 91)]  # определяем наш набор бочонков от 1 до 90.

while True:
    if len(pul) < 1:
        print('Игра завершена.\n'
              'Ничья... Нееет, такое лото нам не нужно')
        break

    keg = pul.pop(random.randint(0, len(pul) - 1))
    print('Достаем новый бочонок: {} (В мешке осталось {}) \n'.format(keg, len(pul)))  # Определяем новый ход
    print(computer)
    print(player)
    answer = input('Зачеркнуть число? (y/n) \n')
    answer = answer.lower()  # Переводим ответ игрока в нижний регистр, на случай если он отвечает в верхнем

    # Определяем действия если игрок вводит неверный ответ с клавиатуры или не вводит его вовсе
    while len(answer) == 0 or answer not in 'yn':
        print('Неизвестное значение, попробуйте снова, допустимые ответы  y (Зачеркнуть) или n (Не зачеркивать)')
        print('Был вытащен бочонок: {} (В мешке осталось {} штук)'.format(keg, len(pul)))
        print(computer)
        print(player)
        answer = input('Зачеркнуть цифру? (y/n)')
        answer = answer.lower()

    if answer == 'y':  # Определяем действия если игрок ответил утвердительно
        check = False  # Производим проверку на наличие значения бочонка в карточке игрока
        for x in range(3):
            if keg in player.blank[x]:
                check = True  # Если значение есть, то заменяем его на знак X
                player.blank[x][player.blank[x].index(keg)] = 'X'
                player.count_lotto_keg -= 1  # Определяем оставшееся количество незачеркнутых цифр
            if keg in computer.blank[x]:
                computer.blank[x][computer.blank[x].index(keg)] = 'X'
                computer.count_lotto_keg -= 1
        if check:
            if player.count_lotto_keg < 1:  # Определяем действия если вычеркнуты все значения
                print('Поздравляю! Вы победили! Искуственный Интелект хнычет и просит реванша!')
                break
            elif computer.count_lotto_keg < 1:
                print('Фильм Терминатор знаешь? Там все так и начиналось. Компьютер победил! Надо срочно отыграться =)')
                break
        else:  # Определяем действия если игрок ошибся
            print('Данного числа нету в карточке, невыразимо жаль, но Вы проиграли! Не отчаиваемся!')
            break

    elif answer == 'n':  # Определяем действия если игрок ответил отрицательно
        check = False  # Производим проверку на наличие значения бочонка в карточке игрока
        for x in range(3):
            if keg in player.blank[x]:  # Определяем действия если игрок ошибся
                print('Данное число было в Вашей карточке, невыразимо жаль, но Вы проиграли! Может в шахматы повезет?')
                check = True
                break
            if keg in computer.blank[x]:  # Проверяем карточку компьютера, при отрицательном ответе игрока
                computer.blank[x][computer.blank[x].index(keg)] = 'X'
                computer.count_lotto_keg -= 1
        if check:
            break

    if player.count_lotto_keg < 1:
        print('Поздравляю! Вы победили! Искуственный Интелект хнычет и просит реванша!')
        break
    elif computer.count_lotto_keg < 1:
        print('Фильм Терминатор знаешь? Там все так и начиналось. Компьютер победил!')
        break
