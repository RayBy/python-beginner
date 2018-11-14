__author__ = 'Ильиных Павел Сергеевич'

# coding UTF-8

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Подключаем необходимые модули

import math


class Triangle:  # Объявляем класс треугольник

    def __init__(self, x1, y1, x2, y2, x3, y3):  # Определяем координаты для построения треугольника
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def area(self):  # Определям площадь треугольника
        sq = abs(((self.x2-self.x1)*(self.y3-self.y1) - (self.x3-self.x1)*(self.y2-self.y1))/2)
        return print("Площадь треугольника равна", sq)

    def height(self):  # Определяем высоту треугольника
        sl1 = (math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        sl2 = (math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2))
        sl3 = (math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2))
        p = (1/2)*(sl1 + sl2 + sl3)
        h = abs((2*(math.sqrt(p*(p-sl1)*(p-sl2)*(p-sl3))))/sl1)
        return print("Высота треугольника опущенная на сторону AB равна ", h)

    def perimeter(self):  # Вычисляем периметр треугольника
        sl1 = (math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        sl2 = (math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2))
        sl3 = (math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2))
        per = (sl1+sl2+sl3)
        return print("Периметр треугольника равен ", per)


triangle_check = Triangle(1, 1, 2, 5, 5, 3)
triangle_check.area()
triangle_check.height()
triangle_check.perimeter()
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Подключаем модули необходимые для работы
import math
import sys


class Trapezium:  # Объявляем класс трапеция

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):  # Определяем координаты для построения трапеции
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def check(self):  # Проверка является ли трапеция равнобокой, если нет, то прекратить выполнение программы
        ab = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        cd = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))

        if ab == cd:
            print("Трапеция является равнобокой", "\n", "Продолжаем выполнение вычислений")
        else:
            print("Трапеция с такими координатами не равнобокая")
            print("Программа завершена")
            sys.exit()

    def side_lenght(self):  # Определяем длину сторон трапеции
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        c = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        d = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print("Длина сторон травпеции: ", "\n", "AB=", a, "\n", "BC=", b, "\n", "CD=", c, "\n", "DC=", d, "\n")

    def perimeter(self):  # Вычисляем периметр трапеции
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        c = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        d = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))

        per = a + b + c + d
        print("Периметр трапеции = ", per)

    def area(self):  # Вычисляем площадь трапеции
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        c = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        d = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))

        h = math.sqrt((a**2) - ((((d-b)**2) + (a**2) - (c**2)) / (2 * (d - b)))**2)
        S = ((b+d)/2)*h
        print("Площадь трапеции равна ", S)

# Проводим первую проверку (Трапеция равнобокая)
first_check = Trapezium(0, 0, 2, 2, 4, 2, 6, 0)
first_check.check()
first_check.side_lenght()
first_check.perimeter()
first_check.area()

print()

# Проводим вторую проверку (Неравнобокая трапеция)
second_check = Trapezium(0, 0, 6, 3, 6, 3, 9, 0)
second_check.check()
second_check.side_lenght()
second_check.perimeter()
second_check.area()