import datetime

a = int(input("Зріст:"))
b = int(input("Маса: "))
c = a**2
d = b / c
print("Ваший ІМТ",d)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
