from fractions import Fraction

x = 0 
y = 0 
symbol = ''

def init_num(a, b):
  global x
  global y
  x = Fraction(a)
  y = Fraction(b)

def init_sym(c):
  global symbol
  symbol = c

def calculator_rational(a, b, c):
  if c == '+': 
    return a + b 
  if c == '-':
    return a - b 
  if c == '*':
    return a * b
  if c == '/':
    return a / b
