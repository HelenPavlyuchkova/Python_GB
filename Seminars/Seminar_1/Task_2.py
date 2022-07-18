# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# работает, но нерациональный способ
a = int(input(('Введите a = ')))
b = int(input(('Введите b = ')))
c = int(input(('Введите c = ')))
d = int(input(('Введите d = ')))
e = int(input(('Введите e = ')))
maxx = a
if ((b > maxx)):
    maxx = b
if(c > maxx):
    maxx = c
if(d > maxx):
    maxx = d
if(e > maxx):
    maxx = e
print(maxx)


# через список
# list = [1,2,3,4,5] 
# maxim = list[0]
# for i in list:
#     if (i > maxim):
#         maxim = i
# print(i)

# через ф-цию max
# list = [1,11,56,2,8]
# print(f'Максимальное число: {max(list)}')

# my_list = [0,1,2,4,5]
# print(my_list[-1])

# for i in [0, 1, 2, 3, 4]:
#     # print(i)
#     x = int(input('--> '))
#     my_list.append(x) # добавление чисел в список

# print(my_list)

# for i in range(55, 101, 2):
#     print(i)

# maxx = 0
# for i in range(5):
#     x = int(input('--> '))
#     if i == 0:
#         maxx = x
#     elif x > maxx:
#         maxx = x
# print(maxx)

# my_list = [5, 2, 9, 6, 0]
# print(my_list)
# my_list.pop(1)
# print(my_list)

# while 6 in my_list:
#     my_list.remove(6)

# print(my_list)


# my_list = [5, 2, 9, 6, 0]
# i = 1
# maxx = my_list[0]
# while i < len(my_list):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#     i += 1
# print(maxx)
