import random

liste = []

'''
eleman_sayisi = int(input("Eleman Sayisi Girin : "))
for i in range(0,eleman_sayisi):
    eleman = int(input("Eleman Girin : "))
    liste.append(eleman)
    liste.insert(i,eleman)

for i in liste:
    print(i)

'''


eleman_sayisi = int(input("Eleman Sayisi Girin : "))
toplam = 0

'''
for i in range(0,eleman_sayisi):
    liste.append(random.randint(0,100))

for i in liste:
    print(i)
    
print(toplam)

'''
'''
for i in range(0,eleman_sayisi):
    eleman = random.randint(0,100)
    liste.append(eleman)
    toplam+=eleman

ortalama = toplam/eleman_sayisi

print(f"Ortalama : {ortalama}\nOrtalamanin Uzerindeki Sayilar : \n")
for i in liste:
    if i >= ortalama:
        print(i)


print("\n"+"Toplam : "+str(toplam))
'''

elemanlar1 = []
elemanlar2 = []

for i in range(0,3):
    eleman = int(input(f"1. Liste Icin {i+1}'nci Elemani Sayi Girin : "))
    elemanlar1.append(eleman)


for i in range(0,3):
    eleman = int(input(f"2. Liste Icin {i+1}'nci Elemani Sayi Girin : "))
    elemanlar1.append(eleman)

ayni = True
for i in range(0,3):
    if elemanlar1[i] != elemanlar2[i]:
        ayni = False

if ayni:
    print("Elemanlar Aynidir.")
else:
    print("Elemanlar Farklidir.")
