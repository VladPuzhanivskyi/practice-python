import datetime

tarif = int(input("Vvedite kakoi u vas tarif: "))
mb = int(input("Vvedite scolko vi potratili mb: "))

if tarif == 5000:
    if mb <= 5000:
        print("You must pay 85 grn")
    else:
        print("You must pay " + str(85 + (mb - 5000) * 0.02) + " grn")
elif tarif == 2000:
    if mb <= 2000:
        print("You must pay 35 grn")
    else:
        print("You must pay " + str(35 + (mb - 2000) * 0.04) + " grn")
        if mb > 5000:
            print("With tarif 5000 you will pay " + str(85 + (mb - 5000) * 0.02) + " grn")

elif tarif == 1000:
    if mb <= 1000:
        print("You must pay 20 grn")
    else:
        print("You must pay " + str(20 + (mb - 1000) * 0.05) + " grn")
        if mb > 5000:
            print("With tarif 5000 you will pay " + str(85 + (mb - 5000) * 0.02) + " grn")
        if mb > 2000:
            print("With tarif 2000 you will pay " + str(35 + (mb - 2000) * 0.04) + " grn")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
