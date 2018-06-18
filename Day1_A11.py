import datetime

a = list(input().split()) # Пример ввода: "15 cm in foot"
a[0]=float(a[0])
b = ["cm","foot","inch"]
c = [0.01,0.3048,0.0254]
d=c[b.index(a[1])]*a[0]
f = c[b.index(a[3])]
print("{:.2e}".format(d/f))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
