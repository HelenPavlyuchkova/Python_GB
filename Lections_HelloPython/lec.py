# print('hello world')

# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n') # второй вариант работы с файлом, причем закрытие делать не нужно, проходит автоматически
# colors = ['red', 'green', 'blue321']
# data = open('file.txt', 'a') #a- данные дописываются, w-перезапись
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close() # закрываем подключение к файлу


# path = 'file.txt'
# data = open(path, 'r') # чтение данных из файла
# for line in data:
#     print(line)
# data.close()

# exit() # позволяет не выполнять тот код, который ниже

# Функции
# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# import hello
# print(hello.f(1))
# import hello as h  # h-алиас, или псевдоним

# print(h.f(2.3))


# def new_string(symbol, count = 3):  # аргументы-символ, число
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # TypeError missing 1 required ... если аргумент-count,  а если count=3, то !!!
# print(new_string(4)) # 12


# def concatenatio(*params): # любое кол-во аргументов
#     res = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # 10


# Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# Кортеж - это неизменяемый список

# a = (3, 1, 41, 4)
# print((a))
# print(a[-2])
# # a[0] = 12 # TypeError...


# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(t[-1])

# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range

# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment


# a = (3, 4, 5)

# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue


# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '↑', # слева-ключи, справа-значения
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)


# for v in dictionary:
#      print(dictionary[v])

# print(dictionary['up']) # ↑
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →


# Множества - Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()



# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
# .union(b) \
# .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a) # неизменяемое множество


# # Списки
# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1 = [1,2,3,4,5]
# print(len(list1))
# print(list1.pop(2)) # удаляет 2й элемент списка, с нуля индексация
# print(list1.insert(2,11)) # [1, 2, 11, 3, 4, 5]
# print(list1.append(5)) # [1, 2, 3, 4, 5, 15]
# print(list1)
# print(list1.pop())# удаляет последний элемент списка
# print(list1)
# print(list1.pop())
# print(list1)


