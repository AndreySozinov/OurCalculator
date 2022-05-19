
def complex_num(x, y, action):
    a = x.replace('j', '')
    a = a.split()
    a = complex(int(a[0]), int(a[2]))
    b = y.replace('j', '')
    b = b.split()
    b = complex(int(b[0]), int(b[2]))
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b
    else:
        print('Ошибка ввода данных')
        
#print(complex_num('5 + 10j', '5 + 10j', '+'))