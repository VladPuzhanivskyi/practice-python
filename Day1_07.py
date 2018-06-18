import datetime

a = int(float(input('Температуру в Цельсиях:')))
kelvin = int(a) + float(273.15)
farengeit = int(float(a * 9/5 + 32)) 
template = '{:.' + str(2) + 'f}'
print("Температура в Фаренгейтах:",template.format(farengeit))
print("Температура в Кельвинах:",template.format(kelvin))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
