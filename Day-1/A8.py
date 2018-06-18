import datetime

c = input('Enter number:') 
print(sum((int(c[i]) for i in range(0, int(len(c))))))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
