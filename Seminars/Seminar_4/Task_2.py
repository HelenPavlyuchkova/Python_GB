# 1. Задайте строку из набора чисел(считайте из файла). Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
# split() == split(' ')
# min() max()


# file_path = r'Seminar_4\file.txt'
# with open(file_path, 'r') as f:
#     mystr = f.read()
#     # lst = str(f)
# print(mystr)

file_path = r'file.txt'
with open(file_path, 'r') as f:
    mystr = f.read()
print(mystr)
mystr = mystr.split()
print((mystr))

for i in range(len(mystr)):
    mystr[i] = int(mystr[i])
print(max(mystr))

