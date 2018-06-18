import datetime 

x = int(input("year: "))
y = int(input("month: "))
z = int(input("Day: "))
today = datetime.date(x, y, z)
tomorrow = today + datetime.timedelta(days=1)

print("Next day is " + str(tomorrow))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
