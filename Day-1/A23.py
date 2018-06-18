import datetime
import math

print('Welcome to the Calculator Python!')
a = int(float(input('Введите число a: ')))
b = int(float(input('Введите число b: ')))
c = input('Яку операцію ви хочете виконати?:')
if c == '+':
    print(int(float(a + b)))
if c == '-':
    print(int(float(b - a)))
if c == '/':
    print(int(float(a / b)))
if c == '*':
    print(int(float(a * b)))
if c == '**':
    print(int(float(a ** b)))
if c == '%':
    print(int(float(a % b)))
if c == 'log10':
  print(math.log10(a))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
