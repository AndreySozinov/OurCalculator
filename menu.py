import complex_num as comp
import ratio as rat


a = complex(input('Введите первое число'))
b = complex(input('Введите второе число'))
znak = input('Введите знак арифметической операции')

if type(a) == 'float':
    print(f'{a} {znak} {b} = {rat(a, b, znak)}')

if type(a) == 'complex':
    print(f'{a} {znak} {b} = {comp(a, b, znak)}')