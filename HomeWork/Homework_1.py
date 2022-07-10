# Задача №1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите день недели (от 1 до 7)--> '))
if (day == 6 or day == 7):
    print(f'{day} - да, это выходной')
else:
    print(f'{day} - нет, это не выходной')



# Задача №2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f'{x = } {y = } {z = } result: {not (x or y or z) == (not x and not y and not z)}')



# Задача №3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату x = '))
y = int(input('Введите координату y = '))
if (x == 0 or y == 0):
    print(f'({x}, {y}) - это точка на оси координат')
elif (x > 0 and y > 0):
    print(f'({x}, {y}) - I плоскость')
elif (x < 0 and y > 0):
    print(f'({x}, {y}) - II плоскость')
elif (x < 0 and y < 0):
    print(f'({x}, {y}) - III плоскость')
else:
    print(f'({x}, {y}) - IV плоскость')



# Задача №4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти (от 1 до 4): '))
if number == 1:
    print('Диапазон координат точки: х > 0, у > 0')
elif number == 2:
    print('Диапазон координат точки: х < 0, у > 0')
elif number == 3:
    print('Диапазон координат точки: х < 0, у < 0')
elif number == 4:
    print('Диапазон координат точки: х > 0, у < 0')
else:
    print('Заданное значение не является номером четверти')



# Задача №5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Введите координату x1 = '))
y1 = float(input('Введите координату y1 = '))
x2 = float(input('Введите координату x2 = '))
y2 = float(input('Введите координату y2 = '))
distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
print(distance)
