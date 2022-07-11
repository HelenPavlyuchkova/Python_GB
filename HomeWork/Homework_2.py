# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def summary(num: int):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result

print(summary(6782))

# # 2й вариант
print(sum(map(int, str(6782))))



# Задача №2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

n = 4
for i in range(1, n+1):
    print(factorial(i), end=' ')



# Задача №3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

