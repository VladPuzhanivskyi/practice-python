import datetime

a = int(input('Кількість хвилин:'))
b = int(input('Кількість смс:'))
c = 15.00
d = 200
f = 50
e = a - d 
r = int(e) * 0.17 
g = b - f
n = int(g) * 0.15
z = r + n + c
template = '{:.' + str(2) + 'f}'
if a <= d and b <= f:
  print('З вас',c)
elif a > d and b > f:
  print(template.format(z))
elif a > d:
  print(template.format(r + c))
elif b > f:
  print(template.format(n + c))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
