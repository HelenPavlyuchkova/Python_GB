
# список list=[] - изменяемый и индексируемый
# кортеж tuple=() - не изменяемый, индексируемый
# множество set() - изменяемый, не индексируемый, уникальные элементы (внутри множеств лежит хэш-функция "черный ящик")
# словарь dict() - изменяемый, не индексируемый (пронумеровать с помощью ключа, причем ключ-это уникальный, неизменяемый объект)

# списки, примеры
a = []
b = a
a.append(4)
print(b) # [4]

# # кортежи, примеры
my_tuple = 1, 2, 3
my_tuple = tuple([11, 15, 22, 33]) # запись через ф-цию tuple
print(my_tuple)
print(my_tuple[2])
# my_tuple[1] = 2 # в кортеже это не работает!

a = (1, [123, 123], 88) # переменная это ссылка в памяти
b = a[1]
b.append(5255)
print(a)

a = (1, 2, 8, 6)
b = list(a) # запись через ф-цию list
print(b)

# примеры множеств
# set упорядочивает и выводит уникальные элементы
my_set = set([1, 2, 3, 4, 7, 2, 8, 5])
my_set.add(6)
print(my_set)
my_set2 = set([1, 2, 3, 4, 7, 2, 'ddd', 8, 5])
print(my_set2)

my_set3 = {1, 2, 8, 3}
for item in my_set3:
    print(item)

# примеры словарей
my_dict = {}
print(type(my_dict))

a = 234
my_dict = {
    (12, 11): 'стол',
    24: 'кровать',
    2: [5,6,8],
    'adf': 12,
    a: {5,9,4}
}
my_dict[(12,11)] = 'NEW'
print(my_dict)

for key in my_dict:
    print(key)

# # для вывода значений словаря
for val in my_dict:
    print(my_dict[val])
# или то же самое
for val in my_dict.values():
    print(val)

for dbl in my_dict.items():
    print(dbl)

for key, val in my_dict.items():
    print(f'key -> {key}    val -> {val}')

