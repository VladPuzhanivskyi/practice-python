import datetime

a = int(input('Введіть кількість буханок вчорашнього хліба: '))
b = 8.50
c = a * b
d = c * 0.6
f = c - d
template = '{:.' + str(2) + 'f}'
if a > 0:
  print('Звичайна ціна:',template.format(c))
  print('Ціна із знижкою:',template.format(f))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
