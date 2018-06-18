import datetime

def main():
    
    sequence = [3, 9, 13, 15, 17]

    for num in sequence:

        print(("x"*num).center(20))

    for num in reversed(sequence):

        print(("x"*num).center(20))

main()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
