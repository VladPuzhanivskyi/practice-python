import datetime
import math

a = int(input('Enter radius:'))
b = math.pi * a**2
c = 4/3 * math.pi * a**3
print('Площа',b)
print('Об`єм круга',c)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
