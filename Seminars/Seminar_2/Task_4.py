# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# def searchNumber(a: int, b: int) -> list:
#     my_list = [1]
#     i = 1
#     while len(my_list) < a:
#         my_list.append(my_list[-1]*b)
#         i += 1
#     return my_list

# print(searchNumber(5,-3))


def func(x):
    result = 1
    for i in range(x):
        print(result, end=' ')
        result *= -3

n = int(input('Введите число: '))
func(n)

# работает
# def print_numbers(x):
#     vivod = 1
#     for i in range(x):
#         print(vivod)
#         vivod = vivod * -3

# n = int(input('--> '))
# print_numbers(n)


# def searchNumber(num=10, *args):
#     return args

# print(searchNumber(5,10, 123, 5432, 324, 76))

# def print_numbers(x=[]):
#     x.append(5)
#     print(x)

# a = []
# print_numbers(x=a)
# print_numbers(x=a)
# print_numbers(x=a)
# print_numbers(x=a)
# print(f'---> {a}')

