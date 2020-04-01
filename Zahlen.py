
import random
print ("Das Programm bestimmt ein zufällige Zahl zwischen 0 und 100")
num=random.randint(0,100)
print(num)
while True:
    x=input("Errate eine zahl und gib sie ein")

    if x=="exit":
        print("ok")
        break

    elif int(x)==int(num):
        print (" prima, Die Zahl ist korrekt")
        break

    elif int(x)>100 or int (x)<1:
        print ("Fehler, versuch es erneut")
        continue

    elif int(x)<int(num):
        print("Fehler , die Zahl ist größer als die Zufallszahl")
        continue

    elif int(x)>int(num):
        print ("Fehler, die Zahl ist kleiner als die Zufallszahl")
        continue
input("")


