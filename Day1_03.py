import datetime

a = int(input('тиск у паскалях:'))
b = a / 7.50063755419211
print(b)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
