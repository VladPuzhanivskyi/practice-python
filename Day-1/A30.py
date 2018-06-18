import datetime
import math

M = int(0)
p = float(1.038)
c = float(3.7)
K = float(5.4 * (10 ** 3))
Tw = float(100)
while M == 0:
    a = int(input('Яйце велике чи маленьке? (1/2): '))
    if a == 1:
        M = 67
    elif a == 2:
        M = 47
    else:
        print('Введіть значення 1 або 2')
Ty = float(input('Введіть температуру жовтка: '))
T0 = 0
while T0 == 0:
    b = int(input('Яйце з холодильника чи кімнатної температури? (1/2): '))
    if b == 1:
        T0 = float(4)
    elif b == 2:
        T0 = float(20)
    else:
        print('Введіть значення 1 або 2')

t = ((M ** (2/3)) * c * (p ** (1/3)))/(K * (math.pi ** 2) * (((4 * math.pi)/3) ** (2/3))) * math.log(float(0.76) * ((T0 - Tw)/(Ty - Tw)))
print('Час, коли центр жовтка досягне температури Ty: ' + str(t))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
