# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python
# disc x1, x2
 


path = 'file1.txt'
with open(path, 'r') as my_file:
    data = my_file.read()
data = data.split()
print(data)
data = data[:-2]
print(data)
# new_data = [data[0], data[1] + data[2], int(data[3] + data[4])]
new_data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
print(new_data)
# d = b**2 - 4*a*c
d = new_data[1] ** 2 - 4 * new_data[0] * new_data[2]
print(d)
# x= ((-b+d^(1/2))/(2*a))
x_1 = (-new_data[1] + d**0.5) / (2 * new_data[0])
x_2 = (-new_data[1] - d**0.5) / (2 * new_data[0])
print(x_1)
print(x_2)
