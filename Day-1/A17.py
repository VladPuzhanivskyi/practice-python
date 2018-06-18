import datetime

c = int(float(input('Введите суму:')))
f = int(input('введіть кількість років:'))
r = 0.14 * c
d = c + r
template = '{:.' + str(2) + 'f}'
if f == 1:
  print(template.format(d))
if f == 2:
  print(template.format(c + r * 2))
if f == 3:
  print(template.format(c + r * 3))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
