def dizi_ortalamasi(dizi):
    return sum(dizi) / len(dizi)
print("-----------Avarage---------")
print(dizi_ortalamasi([10, 20, 30, 40,50,60,70]))


def en_buyuk(sayi1, sayi2):
    return max(sayi1, sayi2)
print("-----------Max value---------")
x=input("Please enter the  number: ")
y=input("Please enter the number: ")
print(en_buyuk(x,y))


def kelime_sayisi(metin):
    return len(metin.split())
print("-----------Number of words---------")
y=input("Please enter the text: ")
print(kelime_sayisi(y))