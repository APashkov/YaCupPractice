from Big_data import big_data as big
from random import randrange

a = 100000


def data_range():
    d = ''
    for _ in range(a):
        d += '1 '
        #d += str(randrange(10)) + ' '
    return d


data = f'{a} {a} \n'
data += data_range() + '\n'
data += data_range()

big.write_file(result=data, file='input.txt')