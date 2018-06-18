import datetime 

n = int(input())
m = int(input())
d = 0
if n > m:
    d = m
else:
    d = n

while True:
    if n % d == 0 and m % d == 0:
        break
    d -= 1

print("Naibilshyi spilnii dilnic = " + str(d))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
