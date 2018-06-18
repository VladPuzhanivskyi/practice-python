import datetime
import math

s = int(input('Введите длину стороны:'))
n = int(input('Введите количество сторон:'))
r = s**2 * n
v = math.pi / int(n)
e = (math.tan(math.radians(v))) * 4
w = r / e
print(round(w,2))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
