# ещё вариант записи решения
my_str = 'Привет, мир! Мы очеабвнь любим Пайтомаабвба! Семинары'

res = [word for word in my_str.split() if 'абв' not in word]
print(res)
print(' '.join(res))
