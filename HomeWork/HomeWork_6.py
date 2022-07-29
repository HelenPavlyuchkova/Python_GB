# предложить улучшения кода для уже решённых задач. ПЯТЬ ШТУК:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# 1й вариант для целых чисел
print(sum(map(int, str(6782))))

# 2й вариант(универсальный)
def sumnum (n):
    res = 0
    for num in str(n):
        if num == '.' or num == ',':
            continue
        res = res + int(num)
    return res

number = input('Введите число: ')
res = sum(map(sumnum, number))
print(res)


# Задача №2. Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите количество элементов в списке n = '))
array = [i for i in range(n)]
print(f'исходный список\n{array}')
array_new = map(random.shuffle(array), array)
print('полученный список')
print(array)


# Задача 3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.


from random import randint

list_num = [randint(1, 10) for i in range(6)]
# list_num = [1, 2, 8, 6, 2]
print(list_num)
new_list = [list_num[i] for i in range(1, len(list_num), 2) if i % 2 != 0]
print(sum(new_list))


# # Задача №4. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def list_pos(n):
    my_li = [((1 + 1/i)**i) for i in range(1, n + 1)]
    new_list = dict(enumerate(my_li))
    print(new_list)
    return sum(my_li)

print(list_pos(6))


# Задача №5. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите натуральное число n = '))

def func(x):
    return 3*x+1

spisok = {i: func(i) for i in range(1, n+1)}
print(spisok)
