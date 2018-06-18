import datetime
import math

weight = int(input('Висота:'))
vi = 0
a = 9.8
form = vi + 2 * float(a) * weight
print(math.sqrt(form))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
