# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

import time

# a = str(time.time())
# b = a[-1] + a[-2]
# print(int(b))

# # второе решение
# ms = int(((time.time() % 1)* 100) % 10)
# print(ms)

# третье 
def find_num(x):
    a = str(time.time())
    b = ''
    count = 1
    while count <= x:
        b += a[-count]
        count += 1
    return int(b)

print(find_num(3))

# четвертый
l = int(input('Введите длину числа: '))
a = time.time()
print(a)
ms = int(((a % 1) * (10 ** (l+1))) % (10**l))
print(ms)