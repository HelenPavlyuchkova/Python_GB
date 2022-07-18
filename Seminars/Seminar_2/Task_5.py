# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.


# без функции
# st1 = 'привиттет!, митре, и, тт'
# st2 = 'т'
# count = 0
# for i in range(len(st1) + len(st2)):
#     if (st1[i : i + len(st2)] == st2):
#         count +=1
# print(count)


# первый вариант
st1 = 'прииивет, мир, т, привет!, и, т, ии'
st2 = 'и'
def str(st1, st2):
    t = 0
    for i in range(len(st1) + len(st2)):
        if (st1[i : i + len(st2)] == st2): # срез индекса
            t += 1
    return t
print(str(st1, st2))


# срезы
# st = 'vn jckl k,o;fb'
# print(st[1:4:2])

# второй вариант решения
# def find_line(string:str, under_strind:str):
#     print(string.count(under_strind))

# user_string = input('Введите текст: ')
# user_understring = input('Введите текст: ')
# find_line(user_string, user_understring)


# третий вариант, не на всех вариантах работает!
# symbol = "oo"
# base_string = "myooooownooriteoo"
# position = 0
# qty = 0
# while (True):
#     position = base_string.find(symbol, position)
#     if position == -1:
#         break
#     else:
#         position += 1
#     qty += 1
# print(qty)

