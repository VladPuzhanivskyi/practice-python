import datetime

a = int(input('Введите длину стороны a:'))
b = int(input('Введите длину стороны b:'))
c = int(input('Введите длину стороны c:'))
if a == b and a == c:
  print('рівносторонній трикутник')
elif a == b and c != b and c != a:
  print('рівнобедрений')
else:
  print('Неправильний')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
