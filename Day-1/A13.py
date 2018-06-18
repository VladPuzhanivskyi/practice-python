import datetime

b = list(input('введите 3 числа:'))
b.sort()
print('Мінімальне число списку',min(b))
print('Максимальне число списку',max(b))
print('Відсортований список',b)
print('Сума чисел в списку',sum((int(b[i]) for i in range(0, int(len(b))))))
print('Різниця максимального і мінімального значення',int(max(b)) - int(min(b)))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
