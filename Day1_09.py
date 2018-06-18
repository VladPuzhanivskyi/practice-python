import datetime

a = int(input('People years:'))
b = a * 4
c = 10.5
if a == 1:
  print(5.25)
if a == 2:
  print(c)
if a > 2:
  c += 4 * (a - 2)
  print(c) 
if a < 0:
  print('Помилка'

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
