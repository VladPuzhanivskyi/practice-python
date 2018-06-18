import datetime

code = [9,7,8,9,6,0,9,3,1,9,6,1,4]
x = int(code[0]*1) + int(code[1]*3) + int(code[2]*1) + int(code[3]*3) + int(code[4]*1) + int(code[5]*3) + int(code[6]*1) + int(code[7]*3) + int(code[8]*1) + int(code[9]*3) + int(code[10]*1) + int(code[11]*3)

tcd = 10 - (x % 10)
print(tcd)
if tcd == code[12]:
    print("ti vvel pravilnyi cod")
else:
    print("tvoi cod ne pravilnyi")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
