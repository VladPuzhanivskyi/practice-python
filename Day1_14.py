import datetime

month = input('введіть назву місяця: ')
if month == 'Січень':
  print(31)
elif month == 'Лютий':
  print('28 або 29')
elif month == 'Березень':
  print(31)
elif month == 'Квітень':
  print(30)
elif month == 'Травень':
  print(31)
elif month == 'Червень':
  print(30)
elif month == 'Липень':
  print(31)
elif month == 'Серпень':
  print(31)
elif month == 'Вересень':
  print(30)
elif month == 'Жовтень':
  print(31)
elif month == 'Листопад':
  print(30)
elif month == 'Грудень':
  print(31)
else:
  print('Помилка вводу')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
