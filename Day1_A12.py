import datetime

import datetime
now = datetime.datetime.now()
then = datetime.datetime(2018, 6, 10)
# Кол-во времени между датами.
delta = now - then
print(delta.days)
print(delta.seconds)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
