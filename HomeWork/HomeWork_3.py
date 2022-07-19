# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# первый вариант
summ = 0
list_num = [2, 5, 9, 4, 12, 3, 1, 6]
for i in range(len(list_num)):
    print(list_num[i], end=' ')
    if i % 2: # i % 2 != 0
        summ += list_num[i]
print(f'\nСумма элементов на нечетных позициях: {summ}')

# второй вариант
list_num = [2, 5, 9, 4, 12, 3, 1, 6]
def sumlist(list_num):
    res = 0
    for i in range(1, len(list_num), 2):
        res += list_num[i]
    return res

print(list_num)
print(f'Сумма элементов на нечетных позициях: {sumlist(list_num)}')


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# первый вариант
list_n = [1, 3, 6, 7, 9, 6, 5]
list_res = []
i = 0
print(list_n)
while i < len(list_n)/2:
    list_res = list_n[i] * list_n[len(list_n)-1-i]
    i += 1
    print(list_res, end=' ')

# второй вариант
def func(num: list) -> list:
    spres=[]
    for i in range(round((len(num)+1)/2)):
        spres.append(num[i]*num[-i-1])
    return spres

num1=[2, 10, 4, 3, 1, 9]
num2=[1, 3, 4, 2, 6]
print(func(num1))
print(func(num2))


# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def func(sp):
    min = sp[0] % 1
    max = sp[0] % 1
    sp1 = []
    for i in range(len(sp)):
        sp1.append(round(sp[i] % 1, 2))
        if sp1[i] < min and sp1[i] != 0:
            min = sp1[i]
        if sp1[i] > max:
            max = sp1[i]
    return max, min

sp_num = [1.1, 1.2, 3.1, 5, 10.01]
max, min = func(sp_num)
print(sp_num)
print(f'Максимальное значение дробной части: {max}\nМинимальное значение дробной части: {min}\nРазница между ними: {round((max-min), 2)}')


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def func(n: int) -> str:
    bin_num = ''
    while n > 0:
        bin_num = str(int(n % 2)) + bin_num
        n //= 2
    return bin_num

number = int(input('Введите десятичное число n:'))
print(f'{number} -> {func(number)}')

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n < 0:
        if n in [-1]:
            return 1
        elif n in [-2]:
            return -1
        else:
            return fib(n+2)-fib(n+1)
    else:
        if n in [1, 2]:
            return 1
        else:
            return fib(n-1)+fib(n-2)


n = int(input('Введите число n:'))
list = []

for i in range(-n, n+1):
    list.append(fib(i))
print(list)
