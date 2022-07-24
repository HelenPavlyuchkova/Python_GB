
# my_str = '1 2 54 76 2'.split()
# print(my_str)
# for i in range(len(my_str)):
#     my_str[i] = int(my_str[i])
#     print(my_str)

my_str = '1 2 54 76 2'.split()

my_list = [int(item) for item in my_str if int(item) > 10]
print(my_list)

my_str = '1, 22, 54, 76, 2'.split(',')
#что сделать с элементом, с каким элементом, условие
my_list = [int(item) for item in my_str if int(item) > 10]
print(my_list)


f = lambda x: x**2 if x > 10 else x**3
# print(f(5))

my_list = [12, 54, 3, 65]
# res = list(map(f, my_list))
# res = tuple(map(f, my_list))
res = tuple(map(lambda x: x**2, my_list))
# print(res)

# res = tuple(filter(f, my_list))

f = lambda x: True if x <= 10 else False
my_list = [12, 54, 3, 65]
res = list(filter(f, my_list))
# print(res)

my_list1 = ['A', 'B', "C", "D"]
my_list2 = [12, 54, 2, 8]
my_list3 = [3, 54, 65]

res = dict(zip(my_list1, my_list2))
res = list(zip(my_list1, my_list2, my_list3))
# print(res)

res = list(enumerate(my_list1))
# print(res)

data = list(map(int, input().split())) # в одну строку

