import datetime

magn = int(float(input('Введите магнитуду:')))
if magn < 2:
  print('micro')
elif magn in range(2,3):
  print('Дуже слабкий (very minor)')
elif magn in range(3,4):
  print('Слабкий (minor)')
elif magn in range(4,5):
  print('Легкий (light)')
elif magn in range(5,6):
  print('Помірний (moderate)')
elif magn in range(6,7):
  print('Сильний (strong)')
elif magn in range(7,8):
  print('Дуже сильний (major)')
elif magn in range(8,10):
  print('Великий (great)')
elif magn >= 10:
  print('Рідкісно великий (meteoric)')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
