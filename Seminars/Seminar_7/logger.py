from calendar import c
from datetime import datetime as dt
from time import time


def math_oper_logger(data=0):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};{}\n'
                    .format(time, data))
    return

math_oper_logger()