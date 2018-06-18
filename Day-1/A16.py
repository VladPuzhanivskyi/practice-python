import datetime

a = int(input('Ширина:'))
b = int(input('Довжина:'))
c = a * b
d = int(c) / 100
e = int(c) / 10000
print('ar',d)
print('gektar',e) 

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
