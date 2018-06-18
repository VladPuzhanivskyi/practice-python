import datetime

baks = int(input("Vasha zdacha: "))
nominals = [2,1,5,10,50]

nominals.sort()
nominals.reverse()
summ = 0
print (baks, '$ =>')

for k in nominals:
    d = baks//k
    baks = baks -d*k
    print (k,'$ :',int(d))
    summ += d

print ('V summe:', summ)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
