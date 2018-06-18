import datetime

a = int(input('Введите число:'))
b = a + 1
c = a * b / 2
print(c)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
