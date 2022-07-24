
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


my_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = []
for item in my_list:
    if my_list.count(item) == 1:
        res.append(item)
print(res)

res = [item for item in my_list if (my_list.count(item) == 1)]
print(res)

f = lambda item: my_list.count(item) == 1
res = list(filter(f, my_list))
print(res)


