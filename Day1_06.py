import datetime

a = int(float(input('Введите стоимость:')))
podatok = int(18 / 100 * a)
chayovi = int(14 / 100 * a)
suma = int(float(podatok + chayovi + a))
template = '{:.' + str(2) + 'f}'
print("Податок:",template.format(podatok))
print("Чайові:",template.format(chayovi))
print("Підсумкова вартість:",template.format(suma))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
