import datetime

shtuchka = int(input('Введите количество штучек: '))
shtukencia = int(input('Введите количество штукенций: '))
shtuchka1 = 75 * shtuchka
shtukencia1 = 112 * shtukencia
print("Штучек:", shtuchka1)
print("Штукенций:",shtukencia1)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
