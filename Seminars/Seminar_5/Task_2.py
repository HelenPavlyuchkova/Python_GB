# Задача. удалить из исходной строки слова с "абв"
'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'

str_list = 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'
# str = str.split()
# print(str)

# первый вариант
# str_list = str_list.split()
def strs(str_list):
    for item in str_list:
        if 'абв' in item:
            str_list.remove(item)
    print(str_list)
# strs(str_list)

# второй вариант
res = list(filter(lambda item: 'абв' not in item, str_list.split()))
print(res)