

# a = 5
# b = 10
# print(a)
# print(b)

a = int(input(('Введите a = ')))
b = int(input(('Введите b = ')))

# if b == a * a:
#     print(f'да, {b} это квадрат {a}')
# elif a == b * b:
#     print(f'да, {b} это квадрат {a}')
# else:
#     print(f'нет, {b} не квадрат {a}')

if ((b == a * a) or (a == b * b)):
    print('да, квадрат')
else:
    print('не квадрат')

# print('yes' if ((a == b*b) or (b == a*a)) else 'no')


