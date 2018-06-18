import datetime

nomer = input("Nomer: ")

bukvi = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if len(nomer) == 6:
    if nomer[0] in bukvi and nomer[1] in bukvi and nomer[2] in bukvi and nomer[3] in num and nomer[4] in num and nomer[5] in num:
        print("Старий формат(перші три букви решта цифри)")
    else:
        print("Kod nepravilnyi")
if len(nomer) == 7:
    if nomer[0] in num and nomer[1] in num and nomer[2] in num and nomer[3] in num and nomer[4] in bukvi and nomer[5] in bukvi and nomer[6] in bukvi:
        print("Новий формат(Перші 4 букви решта цифри)")
    else:
        print("Kod nepravilnyi")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
