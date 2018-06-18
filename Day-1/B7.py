import datetime

a = input('Home')
b = int(input('Home time:'))
if a == 'Будинок' and b > 18:
  print('В’єтнамське порося')
elif a == 'Будинок' and b in range(10,17):
  print('Собака')
elif a == 'Будинок' and b < 10:
  print('Змія')
elif a == 'Квартира' and b > 18:
  print('Кішка')
elif a == 'Квартира' and b < 10:
  print('Хом’як')
elif a == 'Гуртожиток' and b > 6:
  print('Рибки')
elif a == 'Гуртожиток' and b < 6:
  print('Мурашник')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
