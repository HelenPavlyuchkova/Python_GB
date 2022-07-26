# Задача №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Приветствую здеабвсь вас! Кабвк добрый вабвши вечер!'
del_text = 'абв'

# первый вариант
def mod_del(text, del_text):
    text = text.split()
    for item in text:
        if del_text in item:
            text.remove(item)
    return text

print(f'Исходный текст:\n"{text}"')
new_text = mod_del(text, del_text)
print(f'Полученный текст:')
print(' '.join(new_text))


# второй вариант
clean_text = list(filter(lambda item: del_text not in item, text.split()))
print(clean_text)


# третий вариант
result = [word for word in text.split() if del_text not in word]
print(result)



# Задача №2. Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента? 


from random import randint

def game(name):
    x = int(input(f"{name}, Возьмите конфеты, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def res(name, k, counter, end_cnd):
    print(f"Ходил игрок {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {end_cnd} конфет.")

player1 = input("Введите имя игрока 1: ")
player2 = input("Введите имя игрока 2: ")
fst_cnd = int(input("Сколько всего имеем конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первым ходит игрок {player1}")
else:
    print(f"Первым ходит игрок {player2}")

counter1 = 0 
counter2 = 0

while fst_cnd > 28:
    if flag:
        k = game(player1)
        counter1 += k
        fst_cnd -= k
        flag = False
        res(player1, k, counter1, fst_cnd)
    else:
        k = game(player2)
        counter2 += k
        fst_cnd -= k
        flag = True
        res(player2, k, counter2, fst_cnd)

if flag:
    print(f"Поздавляем! Выиграл игрок {player1}")
else:
    print(f"Поздравляем! Выиграл игрок {player2}")


# Задача №3. Создайте программу для игры в ""Крестики-нолики"".

def strateg_Win(field):
    if field[:5] == 'X X X' or\
            field[6:11] == 'X X X' or\
            field[12:17] == 'X X X' or\
            field[::6] == 'X X X' or\
            field[2::6] == 'X X X' or\
            field[4::6] == 'X X X' or\
            field[::8] == 'X X X' or\
            field[4:13:4] == 'X X X':
        print('Х победили!')
        return 'X'
    elif field[:5] == 'O O O' or\
            field[6:11] == 'O O O' or\
            field[12:17] == 'O O O' or\
            field[::6] == 'O O O' or\
            field[2::6] == 'O O O' or\
            field[4::6] == 'O O O' or\
            field[::8] == 'O O O' or\
            field[4:13:4] == 'O O O':
        print('O победили!')
        return 'O'
    else:
        return

# исходное поле
field = 'a b c d e f g h i'
print(field[:5])
print(field[6:11])
print(field[12:17])

for k in range(1, 10):
    k = 1
    while k == 1:
        x = input('Введите место (от a до i), куда поставить Х:')
        if x in field:
            field = field.replace(x, 'X')
            k += 1
        else:
            print('Это место занято')
    print(field[:5])
    print(field[6:11])
    print(field[12:17])
    if strateg_Win(field):
        break
    if 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' not in field:
        print('Игра окончена! Ничья')
        break
    k = 1
    while k == 1:
        o = input('Введите место (от a до i), куда поставить O:')
        if o in field:
            field = field.replace(o, 'O')
            k += 1
        else:
            print('Это место занято')
    print(field[:5])
    print(field[6:11])
    print(field[12:17])
    if strateg_Win(field):
        break
    if 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' not in field:
        print('Игра окончена! Ничья')
        break


# Задача №4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('/Users/Admin/Desktop/python/HomeWork/HW_5/first_file.txt', 'r') as data:
    my_str = data.read()

def code_rle(sl):
    str_code = ''
    prev_char = ''
    count = 1
    for char in sl:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = code_rle(my_str)
print(str_code)
one_str = str_code

with open('/Users/Admin/Desktop/python/HomeWork/HW_5/cod_file.txt', 'w') as data:
    data.write(one_str)