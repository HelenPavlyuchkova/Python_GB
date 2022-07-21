# Задача №1. Вычислить число c заданной точностью d
# при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

import math

d = float(input('Задайте точность d (вида: 0.001): '))
count = 0
while d % 1 != 0:
    d *= 10
    count += 1
print(round(math.pi, count))


# Задача №2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def f(x):
    list_res = []
    n = 2
    while x > 1:
        if x % n == 0:
            list_res.append(n)
            x /= n
        else:
            n += 1
    return list_res

x = int(input('Введите натуральное число x: '))
print(f'Список простых множителей числа {x} ->', f(x))

# Задача №3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# пример: [0, 4, 2, 5, 4, 5, 3, 5, 2] -> [0, 4, 2, 5, 3]

spisok = input('Задайте последовательность чисел через пробел: ').split(' ')
spisok = [int(x) for x in spisok]
spisok_new = [0]
for i in range(1,len(spisok)):
    for j in range(0, i):
        val = True
        if spisok[j] == spisok[i]:
            val = False
            break
    if val == True:
        spisok_new.append(spisok[i])
print(spisok, '->', spisok_new)

# Задача №4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите натуральную степень k = '))
spKoff = []
for i in range(0, k+1):
    spKoff.append(random.randint(0, 10))

line = ''
for i in range(0, k+1):
    if i == 0:
        if spKoff[i] > 0:
            line = line+'+'+str(spKoff[i])+'=0'
        else:
            line = line+'=0'
    elif i == 1:
        if spKoff[i] > 1:
            line = str(spKoff[i])+'*x'+line
        elif spKoff[i] == 1:
            line = 'x'+line
    else:
        if spKoff[i] > 1:
            line = str(spKoff[i])+'*x^'+str(i)+'+'+line
        if spKoff[i] == 1:
            line = 'x^'+str(i)+'+'+line
spKoff.reverse()
print(spKoff)
print(f'{k=}->', line)


# Задача №5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def funcwrite(text, spKoff):  # записываем набор коэффициентов в файл
    with open(text, 'w', encoding='utf-8') as file:
        for i in spKoff:
            file.write(f'{i} ')
    return


def funcread(text):  # считываем набор коэффициентов из файла и преобразуем в список int
    spKoff = []
    with open(text, 'r', encoding='utf-8') as file:
        a = file.readline().split(' ')
        for i in range(0, len(a)-1):
            spKoff.append(int(a[i]))
    return spKoff


k = int(input('Введите натуральную степень k = '))  # размер многочлена
spKoff1 = []
spKoff2 = []
for i in range(0, k+1):
    spKoff1.append(random.randint(-10, 10))  # формируем набор коэффициентов
    spKoff2.append(random.randint(-10, 10))  # формируем набор коэффициентов
funcwrite('file1.txt', spKoff1)
funcwrite('file2.txt', spKoff2)
spKoff3 = []
spKoff3 = funcread('file1.txt')
print(spKoff3, '- Первый список коэффициентов многочлена')
spKoff4 = []
spKoff4 = funcread('file2.txt')
print(spKoff4, '- Второй список коэффициентов многочлена')
spKoff5 = []
for i in range(0, len(spKoff3)):  # сумма многочленов - это сумма коэффициентов многочленов
    spKoff5.append(spKoff3[i]+spKoff4[i])
print(spKoff5, '- сумма коэффициентов многочленов')
spKoff5.reverse()
line = ''
for i in range(0, k+1):
    if i == 0:
        if spKoff5[i] > 0:
            line = line+'+'+str(spKoff5[i])+'=0'
        elif spKoff5[i] < 0:
            line = line+str(spKoff5[i])+'=0'
        else:
            line = line+'=0'
    elif i == 1:
        if spKoff5[i] > 1:
            line = str(spKoff5[i])+'*x'+line
        if spKoff5[i] < 1:
            line = '('+str(spKoff5[i])+'*x)'+line
        elif spKoff5[i] == 1:
            line = 'x'+line
    else:
        if spKoff5[i] > 1:
            line = str(spKoff5[i])+'*x^'+str(i)+'+'+line
        elif spKoff5[i] < 1:
            line = '('+str(spKoff5[i])+'*x^'+str(i)+')+'+line
        elif spKoff5[i] == 1:
            line = 'x^'+str(i)+'+'+line
print(line)
funcwrite('fileSumma.txt', line)
