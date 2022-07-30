x = 0
y = 0

def init(a, b): # метод, отвечающий за инициализацию начальных значений x, y
    global x
    global y
    x = a
    y = b

init(11, 12)
# print(x)
# print(y)

def do_it(): # метод нахождения суммы значений x, y
    return x - y
