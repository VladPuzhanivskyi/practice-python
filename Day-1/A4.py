import datetime

a = input('Введите букву: ')
if a =="a":
  print("Буква голосна")
elif a =="e":
  print("Буква голосна")
elif a =="i":
  print("Буква голосна")
elif a =="o":
  print("Буква голосна")
elif a =="u":
  print("Буква голосна")
elif a == "y":
  print("Буква голосна,а інколи приголосна")
else:
  print("Буква приголосна")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Puzhanivskyi Vladislav'
printTimeStamp(name)
