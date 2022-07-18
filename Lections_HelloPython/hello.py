# типы данных и переменая
# int, float, boolean, str, list, None
# value = None # для объявления переменной, чтобы ее где-то по коду использовать
# print(type(value))

# print(type(a))
# print(type(b))
# value = 12344
# print(type(value))
# t = 'hello \nworld'
# s = 'hello world'

# a = 123
# b = 1.23
# print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s)) # вывод через формат
# print(f'{a} - {b} - {s}') # вывод через интерполяцию

# f = False # True
# print(f)

# list = ['1', '2', '3'] # [1, 2, 3, '1', '2', 'hello', 1,2,3,1.5, True]
# col = ['hello', 1,2,3,1.5, True]
# print(list)
# print(col)


# # Ввод и вывод данных
# # print, input

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a,' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# # Арифметические операции
# # +, -, *, /, %, //, **
# # ** , ⊕, ⊖, *, /, //, %, +, -
# # (), Сокращенные операции

# a = +123
# b = -321
# c = a+b
# print(c)

# a1 = 2.19685301012
# b1 = 3
# c1 = a1 / b1
# c2 = a1 // b1  # в целочисленном формате
# c3 = a1 % b1
# с4 = a1 ** b1
# c5 = round(a1 * b1, 5)
# print(c1)
# print(c2)
# print(c3)
# print(с4)
# print(c5)


# a = 3
# a += 5 # a = a + 5
# print(a)

# # Логические операции
# # >, >=, <, <=, ==, !=
# # not, and, or – не путать с &, |, ^
# # Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 < 8
# print(a)

# b = 1 != 3
# print(b)

# c = 'qawe'
# d = 'qawe'
# print(c == d)

# n = [1, 2]
# m = [1, 2]
# print(n == m)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 223
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)
# print(not 1 in f)

# is_odd = not f[0] % 2 # is_odd = f[0] % 2 == 0, т.к. 0-это False, 1-True(not 0)
# print(is_odd)


# # Управляющие конструкции:
# # if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)


# # Управляющие конструкции: while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# # Управляющие конструкции: for

# for i in 1, 3, -4, 6, 0:
#     # print(i, end=' ') # print(i)
#     print(i**2, end=' ')

# list = [1, 2, 3, -8, 0]
# for i in list:
#     print(i)

# r = range(10) # 0 1 2 3 4 5 6 7 8 9
# for i in r:
#     print(i)

# for i in range(-5, 6, 2):
#     print(i)

# for i in 'qwer - = ty':
#     print(i) # print(i, end=" ") в строку


# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
# print(line)


# # Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)]) # IndexError: string index out of range
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ, от 0 до 2
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


# # Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# # numbers = list(range(1, 6))
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')

# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)
# print(colors.clear())

# # Функции
# # Это фрагмент программы, используемый многократно
# # def function_name(x):
# #   body line 1
# #    . . .
# #    body line n
# #  optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x==2.3:
        return 23
    else:
        return # None
arg = 2.3 # 1--> Целое, 2.3--> 23, 12--> None
# print(f(arg))
# print(type(f(arg)))
