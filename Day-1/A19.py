import datetime
import time

t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
