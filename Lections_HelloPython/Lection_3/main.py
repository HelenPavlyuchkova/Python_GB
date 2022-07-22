# def f(x):
#     return x ** 2

# g = f
# print(type(f)) # <class 'function'>
# print(type(g))
# print(f(4))
# print(g(4))


# def calc1(x):
#     return x+10

# # print(calc(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))


# def math(op, x):
#     print(op(x))

# math(calc2, 10) # 100
# math(calc1, 10) # 20

# def sum(x, y):
# return x+y

# f = sum
# sum = lambda x, y: x + y +1


# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# # calc(sum, 4, 5) # 9

# calc(lambda x, y: x + y, 4, 5)

# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list = []

# for i in range(1, 101):
#     # if(i % 2 == 0):
#         list.append(i)
# print(list)

# def f(x):
#     return x**3


# list = [(i, f(i)) i in range(1, 21) if i % 2 == 0]

# # list = [(i,i) for i in range(1, 21) if i % 2 == 0]
# print(list)


# Задача. В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]


# path = '/Users/Admin/Desktop/python/Lections_HelloPython/Lection_3/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)


# упростим
# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Функция map()
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#           ↓ ↓ ↓ ↓ ↓
#       [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# li = [x for x in range(1, 20)]
# print(li)

# li = map(lambda x: x + 10, li)
# print(li) # <map object at 0x000002229D96AE60>

# li = list(map(lambda x: x+10, li))
# print(li)


# data = list(map(int, input().split())) # # приглашение к вводу чисел через пробел и вывод списка этих чисел
# print(data)

# data = map(int, '9 1 8 7 1 2 33'.split())

# for e in data:
#     print(e)

# print('---')
# for e in data:
#     print(e)


# вернемся к предыдущему примеру, скорректируем решение

# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# data = [x for x in range(10)]

# res = filter(lambda x: x % 2 == 0, data) # <filter object at 0x00000149CEE2AE90>
# print(res)

# res = list(filter(lambda x: not x % 2, data)) # [0, 2, 4, 6, 8]
# print(res)

# вернемся к предыдущему примеру, еще раз скорректируем решение

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 555, 777]
# # data = zip(users, ids) # <zip object at 0x000001BB4F031240>
# data = list(zip(users, ids, salary)) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# print(data)


# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 555, 777]

# data = enumerate(users) # <enumerate object at 0x00000263FE280980>
data = list(enumerate(users)) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
data = list(enumerate(ids)) # [(0, 4), (1, 5), (2, 9), (3, 14), (4, 7)]
print(data)
