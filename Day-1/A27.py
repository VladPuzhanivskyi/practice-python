import datetime

a = input('Чи говорить зараз папуга?')
b = int(input('Котра година?'))
c = [22,23,24,1,2,3,4,5,6,7,8]
if a =='так' and b in c:
  print('Треба накрити папугу')
elif a == 'ні' and b in c:
  print('Не накривайте клітку')
else:
  print('Хай собі кричить')

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
