'''
#Sum the numbers between 1 to 10 with while
toplam = 0
for i in range(1,11):
    toplam += i
print("Toplam = ",toplam)
'''

'''
Sum the numbers between 1 to 10 with while
i=1
toplam = 0
while i<11:
    toplam+=i
    i = i + 1
print(toplam)
'''

'''
Sum the numbers between 1 to input
i = int(input("Sayi Gir : "))
toplam = 0
for i in range (1,i+1):
    toplam += i
    i = i+1
print(toplam)
'''

'''
Sum the numbers between 1 to input with while
i = int(input("Sayi Gir : "))
toplam = 0
while i>0:
    toplam+=i
    i=i-1
print(toplam)
'''

'''
Sum the numbers between 1 to 10 by dividing to 2
tek_toplam = 0
cift_toplam = 0
for i in range (1,11):
    if i%2==1:
        tek_toplam = tek_toplam+i
    else :
        cift_toplam = cift_toplam+i

print("Cift Toplam = ",cift_toplam, "\nTek Toplam = ",tek_toplam)
'''

'''
Sum the numbers between 1 to 10 by dividing to 2 with while
tek_toplam = 0
cift_toplam = 0
i=11
while i > 0:
    i=i-1
    if i%2==1:
        tek_toplam = tek_toplam+i
    else :
        cift_toplam = cift_toplam+i

print("Cift Toplam = ",cift_toplam, "\nTek Toplam = ",tek_toplam)
'''

'''
Sum every numeral
sayi = int(input("3 Basamakli Bir Sayi Girin : "))
if sayi < 100 or sayi > 999:
    while sayi < 100 or sayi > 999:
        sayi = int(input("3 Basamakli Bir Sayi Girin : "))
toplam = 0
for i in range(1,4):
    toplam = toplam + (sayi%10)
    sayi = int(sayi/10)
    i = i+1
print(toplam)
'''
'''
fact = int(input("Faktoryelinin Hesaplanmasini Istediginiz Sayiyi Girin : "))
carpim = 1
for i in range(1, fact+1):
    carpim = carpim*i
print(carpim)


fact = int(input("Faktoryelinin Hesaplanmasini Istediginiz Sayiyi Girin : "))
carpim = 1
while fact > 1:
    carpim = carpim*fact
    fact = fact-1
print(carpim)
'''

'''
doru = 10
yanlis = -5

dogru_sayisi = int(input("Dogru Sayisi Girin : "))
yanlis_sayisi = int(input("Yanlis Sayisi Girin : "))

if dogru_sayisi+yanlis_sayisi!=10:
    while dogru_sayisi+yanlis_sayisi != 10 :
        dogru_sayisi = int(input("Dogru Sayisi Girin : "))
        yanlis_sayisi = int(input("Yanlis Sayisi Girin : "))

print("Toplam Puaniniz : ",dogru_sayisi*doru+yanlis_sayisi*yanlis)
'''

'''
sayi = int(input("Sayi Girin : "))
toplam = sayi
sayac = 0
if sayi != 0 :
    while sayi != 0:
        sayi = int(input("Sayi Girin : "))
        sayac = sayac + 1
        toplam = toplam + sayi
else :
    print("Ortalama = 0")
print("Ortalam = ",toplam/sayac)
'''

'''
import random
sayi = random.randint(0,100)
print(sayi)
for i in range (1,4):
    tahmin = int(input("Tahmin : "))
    if tahmin==sayi:
        print("kazandiniz")
        break
    else:print("tekrar deneyin")
'''
'''
sayi = int(input("Sayi Girin : "))
asalsayi = True
for i in range(2,sayi):
    if sayi%i==0:
        asalsayi = False
        print("Asal Sayi Degildir.")

if asalsayi == True:
    print("Asal Sayidir.")
'''














