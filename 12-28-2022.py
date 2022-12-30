'''
metin = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the "
buyuk_harfler = []
kucuk_harfler = []
for i in metin:
    if i.isupper():
        buyuk_harfler.append(i)
    elif i.islower():
        kucuk_harfler.append(i)

print("Buyuk Harfler :")
print(buyuk_harfler)
print("\nKucuk Harfler :")
print(kucuk_harfler)
'''


'''
metin = input("Metin GIrin : ")
i=len(metin)-1
yenimetin=""
while i >= 0:
    yenimetin = yenimetin + metin[i]
    i -= 1

print(yenimetin)
'''

'''
sayi = int(input("Sayi Girin : "))
bolen_sayilar = []
mukemmel_sayi = True
for i in range(1,sayi):
    if sayi%i==0 :
        bolen_sayilar.append(i)

toplam = 0
for i in bolen_sayilar:
    toplam += i
if toplam != sayi:
    mukemmel_sayi = False

if mukemmel_sayi:
    print("Mukemmel Sayidir")
else:
    print("Mukemmel Sayi Degildir.")

'''

'''
taban = int(input("Taban Girin : "))
us = int(input("Us Girin : "))
carpim = 1
for i in range (1,us+1):
    carpim*=taban

print(carpim)


def us_al(taban,us):
    if taban == 1 or taban == 0 or us == 0:
        return 1
    elif us == 1:
        return taban
    else:
        return taban * us_al(taban,us-1)

'''


def faktoryel_bul(a):
    if a == 0 or a==1:
        return 1
    else:
        return a * faktoryel_bul(a-1)

sayi = int(input("Sayi Gir : "))
faktoryel = faktoryel_bul(sayi)
print(faktoryel)






