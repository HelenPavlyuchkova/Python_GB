from init import input_num
from view import print_num
from calc import summ, d, m, sub
from logger import math_oper_logger
from data import init_data


def get_num():
    a = input_num()
    b = input_num()
    c = input('введите знак необходимого действия: ')
    init_data(a,b,c)# инициализация из data
    math_oper_logger((a, c, b))# логирование
    if c == '+':
        print_num(summ(a,b))
    elif c == '-':
        print_num(sub(a,b))
    elif c == '*':
        print_num(m(a,b))
    else:
        print_num(d(a,b))