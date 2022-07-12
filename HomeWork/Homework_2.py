# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# 1й вариант,только для целых чисел
# def summary(num: int):
#     result = 0
#     while num > 0:
#         result += num % 10
#         num = num // 10
#     return result

# n = int(input('Введите целое число n: '))
# print('Сумма цифр числа равна {}'.format(summary(n)))

# 2й вариант(универсальный)
# def sumnum (n):
#     res = 0
#     for num in str(n):
#         if num == '.' or num == ',':
#             continue
#         res = res + int(num)
#     return res

# number = input('Введите число: ')
# print(f'Сумма цифр числа {number} равна {sumnum(number)}')


# 2й вариант, в одну строку
# print(sum(map(int, str(6782))))



# Задача №2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def factorial(n: int) -> int:
#     if n == 1:
#         return 1
#     else: 
#         return n * factorial(n - 1)

# n = 4
# for i in range(1, n+1):
#     print(factorial(i), end=' ')



# Задача №3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Введите число n = "))

dict_num = {}
for i in range(1,num+1):
    dict_num[i] = (1+1/i)**i
print(dict_num)

result = 0
for i in dict_num:
    result += float(dict_num[i])
print(f"Сумма элементов: {result:.3f}")  


# Задача №4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры пользователем.



# Задача №5. Реализуйте алгоритм перемешивания списка.

