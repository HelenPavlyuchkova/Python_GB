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



# # Задача №4. Задайте последовательность чисел. Напишите программу, которая выведет список
# # неповторяющихся элементов исходной последовательности.
# # пример: [0, 4, 2, 5, 4, 5, 3, 5, 2] -> [0, 4, 2, 5, 3]

# spisok = input('Задайте последовательность чисел через пробел: ').split(' ')
# spisok = [int(x) for x in spisok]
# spisok_new = [0]
# for i in range(1,len(spisok)):
#     for j in range(0, i):
#         val = True
#         if spisok[j] == spisok[i]:
#             val = False
#             break
#     if val == True:
#         spisok_new.append(spisok[i])
# print(spisok, '->', spisok_new)