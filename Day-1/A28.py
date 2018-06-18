import datetime

a = input('Який день?')
if a == 'Вихідний':
  print('будильник можна не вмикати')
elif a == 'Відпустка':
  print('будильник можна не вмикати')
else:
  print('вмикайте будильник')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
