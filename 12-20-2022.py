"""
def faktoryel(a):
    carpim = 1
    for i in range(1,a+1):
        carpim = carpim * i
    print(carpim)

"""

"""
def faktoryel(a):
    carpim=1
    for i in range(1,a+1):
        carpim = carpim * i
    return carpim

sayi = int(input("Bir Sayi Girin : "))
#faktoryel(sayi)
print(faktoryel(sayi))
"""

"""
import random

dizi = []
for i in range(0, 10):
    sayi = random.randint(0, 100)
    dizi.append(sayi)


def ort_bul(dizi):
    ort = sum(dizi) / 10
    return ort


ort = ort_bul(dizi)
sayac = 0
for i in range(0,len(dizi)):
    if dizi[i] > ort:
        sayac+=1

print(f"{sayac} tane sayi ortalamadan buyuktur")
"""

"""
liste = ["GeeksforGeeks","Geeky","Computers","Algoruthms"]
str = input("Ifade Girin : ")
sayac=0
for i in range(0,len(liste)):
    if str in liste[i]:
        sayac+=1
print(f"Girdiginiz ifade listede {sayac} tane vardir.")
"""