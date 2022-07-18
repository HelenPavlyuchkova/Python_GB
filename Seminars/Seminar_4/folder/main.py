# file_path = r'folder\file.txt' # сырая строка
# f = open(file_path,'a') # чтение
# print(f.read())
# f.close()


# r - чтение
# w - запись (открывает и затирает содержимое файла)
# a - дозапись (изменение)
# w, a - если файла нет, то создаст

file_path = r'folder\file.txt' # сырая строка
f = open(file_path,'a') # чтение
#print(f.read(3))
# for line in f:
#     print(line,end='')
# f.write('123\n')
# print(f.read())
# f.close()
with open(file_path,'w') as f:
    f.write(str(123))
