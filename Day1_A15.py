import datetime

list_nums = [2,3,4,5,6]
print(sum(list_nums) / len(list_nums))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
